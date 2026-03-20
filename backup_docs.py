#!/usr/bin/env python3
"""
Ecp-ui-plus 文档备份工具
爬取知识库网站所有页面，转换为结构化的 Markdown 文件

依赖安装:
    pip install requests beautifulsoup4 markdownify

用法:
    python backup_docs.py
"""

import os
import re
import time
import sys
import requests
from bs4 import BeautifulSoup, Tag
from markdownify import markdownify as md
from urllib.parse import urljoin, urlparse, urlunparse

# ────────────────────────────────────────────────────────────────────────────────
#  配置区（可根据需要修改）
# ────────────────────────────────────────────────────────────────────────────────

BASE_URL = "http://frontend.pcitech.online/ecp-ui-plus/"
OUTPUT_DIR = "./ecp-ui-plus-docs"
REQUEST_DELAY = 0.5      # 每次请求间隔（秒），避免对内部服务器造成压力
REQUEST_TIMEOUT = 15     # 请求超时时间（秒）

# 各章节入口页面（脚本从这里找侧边栏的全部链接）
SECTION_ENTRIES = {
    "指南": "http://frontend.pcitech.online/ecp-ui-plus/docs/instruction/quickstart.html",
    "组件": "http://frontend.pcitech.online/ecp-ui-plus/docs/components/overview/summary.html",
    "Api":  "http://frontend.pcitech.online/ecp-ui-plus/docs/api/directives/v-loading.html",
    "微前端": "http://frontend.pcitech.online/ecp-ui-plus/docs/micro-frontends/introduction.html",
}

# ────────────────────────────────────────────────────────────────────────────────
#  全局状态
# ────────────────────────────────────────────────────────────────────────────────

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9",
})
# 绕过系统代理（内网站点不应走 Clash/V2Ray 等本地代理，否则会 502）
session.trust_env = False

visited_urls: set[str] = set()
all_pages: list[dict] = []
stats = {"success": 0, "skip": 0, "error": 0}


# ────────────────────────────────────────────────────────────────────────────────
#  工具函数
# ────────────────────────────────────────────────────────────────────────────────

def fetch_html(url: str) -> str | None:
    """获取页面 HTML，失败返回 None"""
    try:
        resp = session.get(url, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        resp.encoding = "utf-8"
        return resp.text
    except requests.RequestException as e:
        print(f"    [错误] 请求失败: {e}")
        stats["error"] += 1
        return None


def normalize_url(url: str) -> str:
    """去除 URL 中的 hash 锚点，返回规范化地址"""
    p = urlparse(url)
    return urlunparse(p._replace(fragment=""))


def is_internal_doc(url: str) -> bool:
    """判断是否属于站内文档页面（以 BASE_URL 开头且是 .html）"""
    return url.startswith(BASE_URL) and url.endswith(".html")


def url_to_output_path(url: str) -> str:
    """将文档 URL 映射为本地 Markdown 文件路径"""
    path = urlparse(url).path          # e.g. /ecp-ui-plus/docs/instruction/quickstart.html
    path = re.sub(r"^/ecp-ui-plus/", "", path)   # docs/instruction/quickstart.html
    path = re.sub(r"\.html$", ".md", path)        # docs/instruction/quickstart.md
    return os.path.join(OUTPUT_DIR, path)


# ────────────────────────────────────────────────────────────────────────────────
#  侧边栏解析
# ────────────────────────────────────────────────────────────────────────────────

def extract_sidebar_links(soup: BeautifulSoup, base_url: str) -> list[str]:
    """从侧边栏导航提取当前章节所有页面链接"""
    sidebar = soup.find("nav", {"id": "VPSidebarNav"})
    if not sidebar:
        return []

    seen: set[str] = set()
    links: list[str] = []
    for a in sidebar.find_all("a", href=True):
        url = normalize_url(urljoin(base_url, a["href"]))
        if is_internal_doc(url) and url not in seen:
            seen.add(url)
            links.append(url)
    return links


# ────────────────────────────────────────────────────────────────────────────────
#  HTML 清理（VitePress 特有元素处理）
# ────────────────────────────────────────────────────────────────────────────────

def clean_vitepress_html(main_el: Tag) -> Tag:
    """
    清理 VitePress 生成的特有元素，使转换后的 Markdown 更干净：
    1. 代码块：移除 Copy Code 按钮、lang 标签，合并深/浅色两个 <pre> 为一个
    2. 标题：移除 Permalink 锚点（# 零宽空格链接）
    3. 页脚导航：移除上一页/下一页区域
    """
    # 1. 删除 "Copy Code" 按钮、语言标签、代码组 Tab 标签
    for el in main_el.select("button.copy, span.lang, .vp-code-group .tabs"):
        el.decompose()

    # 2. 处理代码块 div.language-xxx
    #    VitePress 会生成两个 <pre>（暗色/亮色），内容相同，只保留第一个并提取纯文本
    for wrapper in main_el.select('[class*="language-"]'):
        # 提取语言名（如 language-js → js）
        lang = ""
        for cls in wrapper.get("class", []):
            m = re.match(r"language-(\w+)", cls)
            if m:
                lang = m.group(1)
                if lang not in ("vp", "adaptive"):   # 过滤 VitePress 内部类名
                    break

        pres = wrapper.find_all("pre")
        if not pres:
            continue

        # 取第一个 <pre> 的纯文本（get_text 自动处理 HTML 实体转义）
        code_text = pres[0].get_text()

        # 重建干净的 <pre><code> 结构
        clean_pre = BeautifulSoup(
            f'<pre><code class="language-{lang}"></code></pre>',
            "html.parser",
        ).pre
        clean_pre.code.string = code_text

        wrapper.clear()
        wrapper.append(clean_pre)

    # 3. 删除标题内的 Permalink 锚点链接
    for heading in main_el.select("h1, h2, h3, h4, h5, h6"):
        for a in heading.find_all("a"):
            a.decompose()

    # 4. 删除页脚上一页/下一页导航
    for el in main_el.select(".VPDocFooter, .pager"):
        el.decompose()

    return main_el


# ────────────────────────────────────────────────────────────────────────────────
#  HTML → Markdown 转换
# ────────────────────────────────────────────────────────────────────────────────

def _extract_code_language(pre_el: Tag) -> str:
    """从 <pre> 的子 <code class="language-xxx"> 中提取语言名"""
    code = pre_el.find("code")
    if not code:
        return ""
    for cls in code.get("class", []):
        m = re.match(r"language-(\w+)", cls)
        if m:
            lang = m.group(1)
            if lang not in ("vp", "adaptive", "theme"):   # 过滤 VitePress 内部类名
                return lang
    return ""


def convert_to_markdown(main_el: Tag) -> str:
    """将清理后的 <main> 元素转换为 Markdown 字符串"""
    raw = md(
        str(main_el),
        heading_style="ATX",                        # ## 风格标题
        bullets="-",                                # 无序列表使用 -
        strip=["script", "style"],                  # 直接删除这些标签
        code_language_callback=_extract_code_language,  # 提取代码块语言
    )
    # 合并超过 2 个连续空行
    clean = re.sub(r"\n{3,}", "\n\n", raw)
    return clean.strip()


# ────────────────────────────────────────────────────────────────────────────────
#  页面处理
# ────────────────────────────────────────────────────────────────────────────────

def process_page(url: str, section_name: str):
    """爬取并保存单个文档页面"""
    url = normalize_url(url)
    if url in visited_urls:
        stats["skip"] += 1
        return
    visited_urls.add(url)

    print(f"  ↓  {url}")
    html = fetch_html(url)
    if not html:
        return

    soup = BeautifulSoup(html, "html.parser")

    # 获取页面标题（h1 文本）
    h1 = soup.find("h1")
    page_title = h1.get_text(strip=True) if h1 else url

    # 定位主内容区域
    main_el: Tag | None = soup.find("main")
    if main_el is None:
        print(f"    [跳过] 未找到 <main> 元素")
        stats["skip"] += 1
        return

    # 清理 → 转换
    clean_vitepress_html(main_el)
    markdown_content = convert_to_markdown(main_el)

    # 写入文件
    output_path = url_to_output_path(url)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        # 添加来源注释，方便追溯
        f.write(f"<!-- source: {url} -->\n\n")
        f.write(markdown_content)
        f.write("\n")

    print(f"     [OK] {output_path}")
    stats["success"] += 1

    all_pages.append({
        "section": section_name,
        "title": page_title,
        "url": url,
        "path": output_path,
    })

    time.sleep(REQUEST_DELAY)


# ────────────────────────────────────────────────────────────────────────────────
#  生成索引
# ────────────────────────────────────────────────────────────────────────────────

def generate_index():
    """在输出目录根部生成 README.md 总索引"""
    index_path = os.path.join(OUTPUT_DIR, "README.md")

    # 按章节分组
    sections: dict[str, list[dict]] = {}
    for page in all_pages:
        sections.setdefault(page["section"], []).append(page)

    lines = [
        "# Ecp-ui-plus 文档备份",
        "",
        f"> 备份来源: {BASE_URL}  ",
        f"> 共 {len(all_pages)} 个页面",
        "",
    ]

    for section_name, pages in sections.items():
        lines.append(f"## {section_name}")
        lines.append("")
        for page in pages:
            # 生成相对路径链接
            rel = os.path.relpath(page["path"], OUTPUT_DIR).replace("\\", "/")
            lines.append(f"- [{page['title']}]({rel})")
        lines.append("")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\n  索引: {index_path}")


# ────────────────────────────────────────────────────────────────────────────────
#  主流程
# ────────────────────────────────────────────────────────────────────────────────

def check_dependencies():
    """检查依赖包是否安装"""
    missing = []
    for pkg in ("requests", "bs4", "markdownify"):
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg if pkg != "bs4" else "beautifulsoup4")
    if missing:
        print(f"[错误] 缺少依赖包，请先运行:\n  pip install {' '.join(missing)}")
        sys.exit(1)


def main():
    check_dependencies()

    abs_output = os.path.abspath(OUTPUT_DIR)
    print("=" * 60)
    print("  Ecp-ui-plus 文档备份工具")
    print(f"  输出目录: {abs_output}")
    print("=" * 60)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for section_name, entry_url in SECTION_ENTRIES.items():
        print(f"\n>> [{section_name}]")

        html = fetch_html(entry_url)
        if not html:
            print(f"  [错误] 无法加载章节入口，已跳过")
            continue

        soup = BeautifulSoup(html, "html.parser")
        links = extract_sidebar_links(soup, entry_url)
        print(f"  发现 {len(links)} 个页面\n")

        for link in links:
            process_page(link, section_name)

    # 汇总
    print("\n" + "=" * 60)
    print(f"  完成！成功 {stats['success']} 页  |  跳过 {stats['skip']} 页  |  失败 {stats['error']} 页")
    generate_index()
    print(f"  输出目录: {abs_output}")
    print("=" * 60)


if __name__ == "__main__":
    main()

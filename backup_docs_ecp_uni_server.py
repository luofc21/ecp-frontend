#!/usr/bin/env python3
"""
ecp-uni-server 文档备份工具
备份 http://frontend.pcitech.online/docs/ecp-uni-server/ 下的所有文档页面

依赖安装:
    pip install requests beautifulsoup4 markdownify

用法:
    python backup_docs_ecp_uni_server.py
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
#  配置区
# ────────────────────────────────────────────────────────────────────────────────

BASE_URL    = "http://frontend.pcitech.online/docs/ecp-uni-server/"
OUTPUT_DIR  = "./ecp-ui-plus-docs/docs/ecp-uni-server"
ENTRY_URL   = "http://frontend.pcitech.online/docs/ecp-uni-server/index.html"
REQUEST_DELAY   = 0.5
REQUEST_TIMEOUT = 15

# ────────────────────────────────────────────────────────────────────────────────
#  全局状态
# ────────────────────────────────────────────────────────────────────────────────

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9",
})
session.trust_env = False   # 绕过代理

visited_urls: set[str] = set()
stats = {"success": 0, "skip": 0, "error": 0}


# ────────────────────────────────────────────────────────────────────────────────
#  工具函数
# ────────────────────────────────────────────────────────────────────────────────

def fetch_html(url: str) -> str | None:
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
    p = urlparse(url)
    return urlunparse(p._replace(fragment=""))


def is_internal_doc(url: str) -> bool:
    if not url.startswith(BASE_URL):
        return False
    path = urlparse(url).path
    if any(path.endswith(ext) for ext in (".png", ".jpg", ".gif", ".svg", ".pdf", ".css", ".js", ".woff2", ".woff")):
        return False
    return True


def url_to_output_path(url: str) -> str:
    path = urlparse(url).path
    path = re.sub(r"^/docs/ecp-uni-server/", "", path)
    path = re.sub(r"\.html$", "", path)
    if not path:
        path = "index"
    path += ".md"
    return os.path.join(OUTPUT_DIR, path)


# ────────────────────────────────────────────────────────────────────────────────
#  侧边栏解析
# ────────────────────────────────────────────────────────────────────────────────

def extract_sidebar_links(soup: BeautifulSoup, base_url: str) -> list[str]:
    """
    从 <div class="nav-side-content"> 提取所有 .html 页面链接
    """
    sidebar = soup.find("div", {"class": "nav-side-content"})
    if not sidebar:
        print("    [警告] 未找到 div.nav-side-content")
        return []

    seen: set[str] = set()
    links: list[str] = []

    for a in sidebar.find_all("a", href=True):
        href = a["href"]
        if href.startswith("http://") or href.startswith("https://"):
            continue
        if href.endswith(".pdf") or ".pdf#" in href:
            continue

        full_href = href if href.startswith("/") else "/" + href
        url = normalize_url(urljoin(BASE_URL, full_href))
        if not url.endswith(".html"):
            # 路径以 / 结尾的是首页，补充 index.html
            if url.endswith("/"):
                url = url + "index.html"
            else:
                url += ".html"

        if url not in seen and url.startswith(BASE_URL):
            seen.add(url)
            links.append(url)

    return links


# ────────────────────────────────────────────────────────────────────────────────
#  HTML 清理
# ────────────────────────────────────────────────────────────────────────────────

def clean_vitepress_html(main_el: Tag) -> Tag:
    for el in main_el.select("button.copy, span.lang, .vp-code-group .tabs"):
        el.decompose()

    for wrapper in main_el.select('[class*="language-"]'):
        lang = ""
        for cls in wrapper.get("class", []):
            m = re.match(r"language-(\w+)", cls)
            if m:
                lang = m.group(1)
                if lang not in ("vp", "adaptive", "theme"):
                    break

        pres = wrapper.find_all("pre")
        if pres:
            code_text = pres[0].get_text()
            clean_pre = BeautifulSoup(
                f'<pre><code class="language-{lang}"></code></pre>',
                "html.parser",
            ).pre
            clean_pre.code.string = code_text
            wrapper.clear()
            wrapper.append(clean_pre)

    for heading in main_el.select("h1,h2,h3,h4,h5,h6"):
        for a in heading.find_all("a"):
            a.decompose()

    for el in main_el.select(".VPDocFooter, .pager, .footer-nav"):
        el.decompose()

    return main_el


# ────────────────────────────────────────────────────────────────────────────────
#  HTML → Markdown
# ────────────────────────────────────────────────────────────────────────────────

def _extract_code_language(pre_el: Tag) -> str:
    code = pre_el.find("code")
    if not code:
        return ""
    for cls in code.get("class", []):
        m = re.match(r"language-(\w+)", cls)
        if m:
            lang = m.group(1)
            if lang not in ("vp", "adaptive", "theme"):
                return lang
    return ""


def convert_to_markdown(main_el: Tag) -> str:
    raw = md(
        str(main_el),
        heading_style="ATX",
        bullets="-",
        strip=["script", "style"],
        code_language_callback=_extract_code_language,
    )
    clean = re.sub(r"\n{3,}", "\n\n", raw)
    return clean.strip()


# ────────────────────────────────────────────────────────────────────────────────
#  页面处理
# ────────────────────────────────────────────────────────────────────────────────

def process_page(url: str):
    url = normalize_url(url)
    if url in visited_urls:
        stats["skip"] += 1
        return
    visited_urls.add(url)

    print(f"  -- {url}")
    html = fetch_html(url)
    if not html:
        return

    soup = BeautifulSoup(html, "html.parser")

    main_el: Tag | None = soup.find("div", {"class": "doc-layout-body"})
    if main_el is None:
        main_el = soup.find("div", {"class": "VPDoc"})

    if main_el is None:
        print(f"    [跳过] 未找到主内容区域")
        stats["skip"] += 1
        return

    h1 = main_el.find("h1")
    page_title = h1.get_text(strip=True) if h1 else url

    clean_vitepress_html(main_el)
    markdown_content = convert_to_markdown(main_el)

    output_path = url_to_output_path(url)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"<!-- source: {url} -->\n\n")
        f.write(markdown_content)
        f.write("\n")

    print(f"     [OK] {output_path}")
    stats["success"] += 1
    time.sleep(REQUEST_DELAY)


# ────────────────────────────────────────────────────────────────────────────────
#  主流程
# ────────────────────────────────────────────────────────────────────────────────

def main():
    abs_output = os.path.abspath(OUTPUT_DIR)
    print("=" * 60)
    print("  ecp-uni-server 文档备份工具")
    print(f"  输出目录: {abs_output}")
    print("=" * 60)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"\n>> 获取侧边栏链接...")
    html = fetch_html(ENTRY_URL)
    if not html:
        print("  [错误] 无法加载入口页面，退出。")
        sys.exit(1)

    soup = BeautifulSoup(html, "html.parser")
    links = extract_sidebar_links(soup, ENTRY_URL)
    print(f"  发现 {len(links)} 个页面\n")

    for link in links:
        process_page(link)

    print("\n" + "=" * 60)
    print(f"  完成! 成功 {stats['success']} 页  |  跳过 {stats['skip']} 页  |  失败 {stats['error']} 页")
    print(f"  输出目录: {abs_output}")
    print("=" * 60)


if __name__ == "__main__":
    main()

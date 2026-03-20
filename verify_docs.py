#!/usr/bin/env python3
"""
Ecp-ui-plus 文档备份验证工具
检查 backup_docs.py 的输出质量，包括：
  1. 文件数量与目录结构
  2. 文件大小分布（空文件 / 内容过少 / 正常）
  3. 代码块语言标识完整性
  4. 已知坏模式检测（Tab 标签泄露、Permalink 残留等）
  5. 缺失页面检测（对比侧边栏与本地文件）
  6. 抽样展示关键文件内容

用法:
    python verify_docs.py
"""

import os
import re
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse
from collections import defaultdict

# ────────────────────────────────────────────────────────────────────────────────
#  配置（与 backup_docs.py 保持一致）
# ────────────────────────────────────────────────────────────────────────────────

OUTPUT_DIR = "./ecp-ui-plus-docs"
BASE_URL   = "http://frontend.pcitech.online/ecp-ui-plus/"

SECTION_ENTRIES = {
    "指南":  "http://frontend.pcitech.online/ecp-ui-plus/docs/instruction/quickstart.html",
    "组件":  "http://frontend.pcitech.online/ecp-ui-plus/docs/components/overview/summary.html",
    "Api":   "http://frontend.pcitech.online/ecp-ui-plus/docs/api/directives/v-loading.html",
    "微前端": "http://frontend.pcitech.online/ecp-ui-plus/docs/micro-frontends/introduction.html",
}

# 文件大小阈值（字节）
THRESHOLD_EMPTY  = 200   # 低于此值视为"几乎为空"
THRESHOLD_SMALL  = 800   # 低于此值视为"内容偏少"

# 已知坏模式（正则 → 描述）
BAD_PATTERNS = {
    r"[A-Za-z\.]+[A-Z][a-z]+ component":   "疑似 VitePress Tab 标签泄露（如 'main.jsVue component'）",
    r"Permalink to":                         "Permalink 文字残留",
    r"Copy Code":                            "Copy Code 按钮文字残留",
    r"Skip to content":                      "导航栏文字残留",
    r"On this page":                         "目录区文字残留",
    r"Next page|Prev page":                  "翻页导航文字残留",
}

# 抽样检查的文件（相对于 OUTPUT_DIR）
SAMPLE_FILES = [
    "docs/instruction/quickstart.md",
    "docs/components/basic/button.md",
    "docs/api/directives/v-loading.md",
    "docs/micro-frontends/introduction.md",
]

# ────────────────────────────────────────────────────────────────────────────────
#  工具
# ────────────────────────────────────────────────────────────────────────────────

def sep(title="", width=60):
    if title:
        pad = width - len(title) - 4
        print(f"\n{'=' * 2} {title} {'=' * max(pad, 2)}")
    else:
        print("=" * width)


def ok(msg):   print(f"  [OK]   {msg}")
def warn(msg): print(f"  [WARN] {msg}")
def err(msg):  print(f"  [FAIL] {msg}")
def info(msg): print(f"         {msg}")


def collect_md_files(root: str) -> list[str]:
    """递归收集所有 .md 文件的绝对路径"""
    result = []
    for dirpath, _, files in os.walk(root):
        for f in files:
            if f.endswith(".md"):
                result.append(os.path.join(dirpath, f))
    return sorted(result)


def url_to_local_path(url: str, out_dir: str) -> str:
    """将文档 URL 转为本地 .md 路径"""
    path = urlparse(url).path
    path = re.sub(r"^/ecp-ui-plus/", "", path)
    path = re.sub(r"\.html$", ".md", path)
    return os.path.join(out_dir, path)


# ────────────────────────────────────────────────────────────────────────────────
#  检查 1：文件数量与目录结构
# ────────────────────────────────────────────────────────────────────────────────

def check_file_count(md_files: list[str]) -> dict[str, list[str]]:
    sep("1. 文件数量与目录结构")

    by_section: dict[str, list[str]] = defaultdict(list)
    for f in md_files:
        rel = os.path.relpath(f, OUTPUT_DIR)
        parts = rel.replace("\\", "/").split("/")
        section = parts[1] if len(parts) >= 2 else "root"
        by_section[section].append(f)

    total = len(md_files)
    if total == 0:
        err(f"输出目录为空，未找到任何 .md 文件: {os.path.abspath(OUTPUT_DIR)}")
    else:
        ok(f"共找到 {total} 个 .md 文件")

    for section, files in sorted(by_section.items()):
        info(f"{section:30s} {len(files):3d} 个文件")

    return dict(by_section)


# ────────────────────────────────────────────────────────────────────────────────
#  检查 2：文件大小分布
# ────────────────────────────────────────────────────────────────────────────────

def check_file_sizes(md_files: list[str]):
    sep("2. 文件大小分布")

    empty, small, normal = [], [], []
    for f in md_files:
        size = os.path.getsize(f)
        rel  = os.path.relpath(f, OUTPUT_DIR).replace("\\", "/")
        if size < THRESHOLD_EMPTY:
            empty.append((size, rel))
        elif size < THRESHOLD_SMALL:
            small.append((size, rel))
        else:
            normal.append((size, rel))

    ok(f"正常文件 (>= {THRESHOLD_SMALL}B): {len(normal)}")

    if small:
        warn(f"内容偏少 ({THRESHOLD_EMPTY}-{THRESHOLD_SMALL}B): {len(small)} 个")
        for size, rel in small:
            info(f"  {size:5d}B  {rel}")
    else:
        ok(f"无内容偏少文件")

    if empty:
        err(f"几乎为空 (< {THRESHOLD_EMPTY}B): {len(empty)} 个")
        for size, rel in empty:
            info(f"  {size:5d}B  {rel}")
    else:
        ok(f"无空文件")


# ────────────────────────────────────────────────────────────────────────────────
#  检查 3：代码块语言标识
# ────────────────────────────────────────────────────────────────────────────────

def check_code_blocks(md_files: list[str]):
    sep("3. 代码块语言标识")

    total_blocks = 0
    missing_lang = 0
    files_with_missing: list[tuple[str, int]] = []

    for f in md_files:
        with open(f, encoding="utf-8") as fh:
            content = fh.read()

        # 匹配所有 ``` 行（开/闭各半），偶数下标为开始行，奇数下标为结束行
        all_fences = re.findall(r"^```(\w*)$", content, re.MULTILINE)
        openings = all_fences[::2]    # 0, 2, 4... 是开始行
        if not openings:
            continue

        total_blocks += len(openings)
        no_lang = sum(1 for lang in openings if not lang)
        if no_lang:
            missing_lang += no_lang
            rel = os.path.relpath(f, OUTPUT_DIR).replace("\\", "/")
            files_with_missing.append((rel, no_lang))

    if total_blocks == 0:
        info("未发现代码块")
        return

    ratio = (total_blocks - missing_lang) / total_blocks * 100
    ok(f"共 {total_blocks} 个代码块，{total_blocks - missing_lang} 个有语言标识 ({ratio:.0f}%)")

    if files_with_missing:
        warn(f"{len(files_with_missing)} 个文件含无语言标识的代码块：")
        for rel, count in sorted(files_with_missing, key=lambda x: -x[1])[:10]:
            info(f"  {count:3d} 个无标识  {rel}")
        if len(files_with_missing) > 10:
            info(f"  ...（共 {len(files_with_missing)} 个文件）")
    else:
        ok("所有代码块均有语言标识")


# ────────────────────────────────────────────────────────────────────────────────
#  检查 4：已知坏模式
# ────────────────────────────────────────────────────────────────────────────────

def check_bad_patterns(md_files: list[str]):
    sep("4. 已知坏模式检测")

    found_any = False
    for pattern, desc in BAD_PATTERNS.items():
        hits: list[tuple[str, str]] = []
        regex = re.compile(pattern)
        for f in md_files:
            with open(f, encoding="utf-8") as fh:
                content = fh.read()
            for line in content.splitlines():
                # 跳过 source 注释行
                if line.startswith("<!-- source:"):
                    continue
                if regex.search(line):
                    rel = os.path.relpath(f, OUTPUT_DIR).replace("\\", "/")
                    hits.append((rel, line.strip()[:80]))
                    break   # 每文件只报告一次

        if hits:
            found_any = True
            err(f"{desc}")
            for rel, snippet in hits[:5]:
                info(f"  {rel}")
                info(f"    >> {snippet}")
            if len(hits) > 5:
                info(f"  ...（共 {len(hits)} 个文件）")

    if not found_any:
        ok("未发现已知坏模式")


# ────────────────────────────────────────────────────────────────────────────────
#  检查 5：缺失页面（对比侧边栏与本地文件）
# ────────────────────────────────────────────────────────────────────────────────

def check_missing_pages():
    sep("5. 缺失页面检测（对比侧边栏）")

    session = requests.Session()
    session.trust_env = False

    all_sidebar_urls: list[str] = []
    for section, entry_url in SECTION_ENTRIES.items():
        try:
            r = session.get(entry_url, timeout=10)
            r.raise_for_status()
        except Exception as e:
            warn(f"[{section}] 无法访问入口页（跳过）: {e}")
            continue

        soup = BeautifulSoup(r.text, "html.parser")
        sidebar = soup.find("nav", {"id": "VPSidebarNav"})
        if not sidebar:
            warn(f"[{section}] 未找到侧边栏")
            continue

        seen: set[str] = set()
        for a in sidebar.find_all("a", href=True):
            url = urlunparse(urlparse(urljoin(entry_url, a["href"]))._replace(fragment=""))
            if url.startswith(BASE_URL) and url.endswith(".html") and url not in seen:
                seen.add(url)
                all_sidebar_urls.append(url)

    ok(f"侧边栏共 {len(all_sidebar_urls)} 个链接")

    missing, exists = [], []
    for url in all_sidebar_urls:
        local = url_to_local_path(url, OUTPUT_DIR)
        if os.path.exists(local):
            exists.append(url)
        else:
            missing.append(url)

    ok(f"已备份: {len(exists)}")
    if missing:
        err(f"缺失 {len(missing)} 个页面:")
        for url in missing:
            # 尝试探测是否真的 404
            try:
                r = session.get(url, timeout=8)
                status = r.status_code
            except Exception:
                status = "?"
            info(f"  [HTTP {status}]  {url}")
    else:
        ok("所有侧边栏页面均已备份")


# ────────────────────────────────────────────────────────────────────────────────
#  检查 6：关键文件内容抽样
# ────────────────────────────────────────────────────────────────────────────────

def check_sample_content():
    sep("6. 关键文件内容抽样（前 30 行）")

    for rel_path in SAMPLE_FILES:
        full = os.path.join(OUTPUT_DIR, rel_path)
        print(f"\n  -- {rel_path} --")
        if not os.path.exists(full):
            err(f"文件不存在: {full}")
            continue

        size = os.path.getsize(full)
        with open(full, encoding="utf-8") as f:
            lines = f.readlines()

        print(f"  大小: {size} B  |  行数: {len(lines)}")
        print()
        for i, line in enumerate(lines[:30], 1):
            print(f"  {i:3d} | {line}", end="")
        if len(lines) > 30:
            print(f"\n  ... (共 {len(lines)} 行)")


# ────────────────────────────────────────────────────────────────────────────────
#  主流程
# ────────────────────────────────────────────────────────────────────────────────

def main():
    sep()
    print("  Ecp-ui-plus 文档备份验证工具")
    print(f"  输出目录: {os.path.abspath(OUTPUT_DIR)}")
    # 修复 Windows 终端 GBK 编码问题（支持中文、emoji 等 Unicode 字符输出）
    if sys.stdout.encoding and sys.stdout.encoding.lower() in ("gbk", "cp936", "gb2312"):
        sys.stdout = open(sys.stdout.fileno(), mode="w", encoding="utf-8", buffering=1)

    sep()

    if not os.path.isdir(OUTPUT_DIR):
        print(f"\n[FAIL] 输出目录不存在: {os.path.abspath(OUTPUT_DIR)}")
        print("       请先运行 backup_docs.py 生成备份文件。")
        sys.exit(1)

    md_files = collect_md_files(OUTPUT_DIR)

    check_file_count(md_files)
    check_file_sizes(md_files)
    check_code_blocks(md_files)
    check_bad_patterns(md_files)
    check_missing_pages()
    check_sample_content()

    sep()
    print("  验证完成")
    sep()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
下载 guidance 站点所有静态资源（PDF 和图片），并修正 markdown 文件中的引用路径

依赖:
    pip install requests

用法:
    python download_assets.py
"""

import os
import re
import sys
import time
import requests
from urllib.parse import urljoin, urlparse

# ────────────────────────────────────────────────────────────────────────────────
#  配置
# ────────────────────────────────────────────────────────────────────────────────

BASE_URL       = "http://frontend.pcitech.online"
GUIDANCE_ROOT  = "./ecp-ui-plus-docs/docs/guidance"
ASSETS_ROOT    = "./ecp-ui-plus-docs/assets"

PDF_DIR        = os.path.join(ASSETS_ROOT, "pdf")
IMG_DIR        = os.path.join(ASSETS_ROOT, "images")   # 最终路径: ./ecp-ui-plus-docs/assets/images/...
# 注意: img_url 形如 /images/guidance/...，lstrip("/") 后为 images/guidance/...
#       os.path.join(IMG_DIR, "images/guidance/...") 会变成 assets/images/images/...，需跳过前缀 images/
_IMG_PREFIX    = "images/"
REQUEST_DELAY  = 0.3
REQUEST_TIMEOUT = 20

# ────────────────────────────────────────────────────────────────────────────────
#  扫描：收集所有 PDF 和图片资源
# ────────────────────────────────────────────────────────────────────────────────

def scan_guidance_pages():
    """从入口页抓取所有 guidance 页面，收集其中引用的 PDF 和图片"""
    session = requests.Session()
    session.trust_env = False
    session.headers["User-Agent"] = "Mozilla/5.0"

    entry = (f"{BASE_URL}/docs/guidance/induction/chapter-technic/"
             "architecture-technical/basics/micro-frontend.html")
    r = session.get(entry, timeout=REQUEST_TIMEOUT)
    soup = __import__("bs4").BeautifulSoup(r.text, "html.parser")

    nsc = soup.find("div", {"class": "nav-side-content"})
    links = []
    for a in nsc.find_all("a", href=True):
        h = a["href"]
        if h.startswith("http://") or h.startswith("https://") or h.endswith(".pdf"):
            continue
        full = h if h.startswith("/") else "/" + h
        if not full.endswith(".html"):
            full += ".html"
        if full.startswith("/docs/guidance") and full not in links:
            links.append(full)

    pdfs, imgs = set(), set()
    for path in links:
        try:
            r2 = session.get(BASE_URL + path, timeout=REQUEST_TIMEOUT)
            s2 = __import__("bs4").BeautifulSoup(r2.text, "html.parser")
            main = s2.find("div", {"class": "doc-layout-body"})
            # 收集图片（来自主内容区）
            if main:
                for img in main.find_all("img"):
                    src = img.get("src", "")
                    if src.startswith("/"):
                        imgs.add(src)
            # 收集 PDF（来自 sidebar 和页面任何位置）
            for a in s2.find_all("a", href=True):
                if a["href"].endswith(".pdf"):
                    pdfs.add(a["href"])
        except Exception:
            pass

    return list(pdfs), list(imgs)


# ────────────────────────────────────────────────────────────────────────────────
#  下载单个文件
# ────────────────────────────────────────────────────────────────────────────────

_session = None

def _get_session():
    global _session
    if _session is None:
        _session = requests.Session()
        _session.trust_env = False   # 绕过代理
        _session.headers["User-Agent"] = "Mozilla/5.0"
    return _session


def download_file(url: str, dest_path: str) -> bool:
    """下载文件到 dest_path，返回是否成功"""
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    if os.path.exists(dest_path):
        return True   # 已存在则跳过
    try:
        r = _get_session().get(url, timeout=REQUEST_TIMEOUT, stream=True)
        r.raise_for_status()
        with open(dest_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    except Exception as e:
        print(f"    [FAIL] {url}  ->  {e}")
        return False


def guess_ext_from_url(url: str) -> str:
    """从 URL 猜测文件扩展名"""
    path = urlparse(url).path
    ext = os.path.splitext(path)[1]
    return ext if ext else ".bin"


# ────────────────────────────────────────────────────────────────────────────────
#  下载 PDF
# ────────────────────────────────────────────────────────────────────────────────

def download_pdfs(pdf_urls: list[str]):
    print("\n== 下载 PDF ==")
    os.makedirs(PDF_DIR, exist_ok=True)
    success, fail = 0, 0
    for pdf_url in pdf_urls:
        filename = urlparse(pdf_url).path.split("/")[-1]
        dest = os.path.join(PDF_DIR, filename)
        local_rel = f"../../../assets/pdf/{filename}"   # 相对路径（从 docs/guidance/.../*.md 出发）
        print(f"  {pdf_url}")
        if download_file(BASE_URL + pdf_url, dest):
            print(f"     -> {dest}")
            success += 1
        else:
            fail += 1
        time.sleep(REQUEST_DELAY)
    print(f"  PDF 完成: {success} 成功, {fail} 失败")
    return success, fail


# ────────────────────────────────────────────────────────────────────────────────
#  下载图片
# ────────────────────────────────────────────────────────────────────────────────

def download_images(img_urls: list[str]):
    print("\n== 下载图片 ==")
    success, fail = 0, 0
    for img_url in img_urls:
        # img_url 形如 /images/guidance/induction/xxx.png
        # 去掉前导 / 得到 images/guidance/...
        # 再去掉 images/ 前缀，得到 guidance/induction/xxx.png
        path_part = img_url.lstrip("/")
        if path_part.startswith(_IMG_PREFIX):
            path_part = path_part[len(_IMG_PREFIX):]
        dest = os.path.join(IMG_DIR, path_part)
        print(f"  {img_url}")
        if download_file(BASE_URL + img_url, dest):
            print(f"     -> {dest}")
            success += 1
        else:
            fail += 1
        time.sleep(REQUEST_DELAY)
    print(f"  图片完成: {success} 成功, {fail} 失败")
    return success, fail


# ────────────────────────────────────────────────────────────────────────────────
#  修正 markdown 中的引用路径（图片和 PDF）
# ────────────────────────────────────────────────────────────────────────────────

def fix_markdown_refs():
    """
    遍历所有 .md 文件，将图片和 PDF 的远程引用替换为本地相对路径：
      /images/...  -> ../../../assets/images/...
      /devops/...pdf  -> ../../../assets/pdf/filename.pdf
    """
    print("\n== 修正 markdown 引用路径 ==")
    changed, total = 0, 0

    for dirpath, _, filenames in os.walk(GUIDANCE_ROOT):
        for filename in filenames:
            if not filename.endswith(".md"):
                continue
            filepath = os.path.join(dirpath, filename)
            total += 1

            with open(filepath, encoding="utf-8") as f:
                content = f.read()

            original = content

            # 图片路径：将 /images/... 替换为相对于 markdown 文件的路径
            # markdown 在 docs/guidance/induction/xxx/yyy.md
            # 目标: ../../../assets/images/...
            def replace_img(m):
                # m.group(0) = 完整匹配 ![alt](url)
                # 从匹配中提取 alt 文本（去掉 ![ 和 ] 之间的部分）
                full_match = m.group(0)
                alt_end = full_match.index("](")
                alt = full_match[2:alt_end]   # 去掉 ![ 前缀，取 ] 之前的内容
                src = m.group(1)
                # 去掉前导 / 和可能的 Windows \，确保是干净的相对路径
                path_part = src.lstrip("/").replace("\\", "/")
                # path_part 形如 images/guidance/xxx，url 是 /images/xxx
                # 目标相对路径是 ../../../assets/images/guidance/xxx
                # 即去掉 path_part 前缀 images/ -> guidance/xxx
                if path_part.startswith("images/"):
                    path_part = path_part[7:]   # 去掉 images/
                new_src = f"../../../assets/images/{path_part}"
                return f"![{alt}]({new_src})"

            content = re.sub(r'!\[[^\]]*\]\((/[^\)]+)\)', replace_img, content)

            # PDF 路径：将 /devops/xxx.pdf 替换为本地 PDF 相对路径
            def replace_pdf(m):
                # m.group(0) = 完整匹配 [text](/devops/xxx.pdf)
                # 提取方括号内的文本
                full_match = m.group(0)
                bracket_end = full_match.index("](")
                link_text = full_match[1:bracket_end]   # 去掉首尾 []
                href = m.group(1)
                filename = urlparse(href).path.split("/")[-1]
                new_href = f"../../../assets/pdf/{filename}"
                return f"[{link_text}]({new_href})"

            content = re.sub(r'\]\((/devops/[^)]+\.pdf)\)', replace_pdf, content)

            if content != original:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                changed += 1
                print(f"  更新: {filepath.replace(GUIDANCE_ROOT+'/', '')}")

    print(f"  修正完成: {changed}/{total} 个文件有路径更新")


# ────────────────────────────────────────────────────────────────────────────────
#  主流程
# ────────────────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  Guidance 静态资源下载工具")
    print(f"  BASE: {BASE_URL}")
    print("=" * 60)

    pdfs, imgs = scan_guidance_pages()
    print(f"\n扫描完成: PDF={len(pdfs)} 个, 图片={len(imgs)} 个")

    s_pdf, f_pdf = download_pdfs(pdfs)
    s_img, f_img = download_images(imgs)

    fix_markdown_refs()

    print("\n" + "=" * 60)
    print(f"  完成! PDF {s_pdf}/{len(pdfs)} | 图片 {s_img}/{len(imgs)}")
    print(f"  PDF 目录:  {os.path.abspath(PDF_DIR)}")
    print(f"  图片目录:  {os.path.abspath(IMG_DIR)}")
    print("=" * 60)


if __name__ == "__main__":
    main()

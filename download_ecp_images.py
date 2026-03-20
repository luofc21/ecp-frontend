#!/usr/bin/env python3
"""下载 ecp-ui-plus 文档中的图片资源"""

import os, requests

BASE_URL = "http://frontend.pcitech.online"
OUTPUT_DIR = "./ecp-ui-plus-docs/assets/ecp-ui-plus/images"
REQUEST_DELAY = 0.3

_session = None

def _get_session():
    global _session
    if _session is None:
        _session = requests.Session()
        _session.trust_env = False
        _session.headers["User-Agent"] = "Mozilla/5.0"
    return _session

images = [
    "/ecp-ui-plus/images/example/PC端微前端加载-Wujie版-组件式加载.png",
    "/ecp-ui-plus/images/example/PC端微前端加载-Wujie版.png",
    "/ecp-ui-plus/images/example/ecp-portal-tabs-01.png",
    "/ecp-ui-plus/images/example/ecp-portal-tabs-02.png",
    "/ecp-ui-plus/images/example/web-ui.jpg",
]

os.makedirs(OUTPUT_DIR, exist_ok=True)
for img_path in images:
    filename = os.path.basename(img_path)
    dest = os.path.join(OUTPUT_DIR, filename)
    url = BASE_URL + img_path
    print(f"  {url}")
    try:
        r = _get_session().get(url, timeout=20, stream=True)
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"     -> {dest}")
    except Exception as e:
        print(f"     [FAIL] {e}")
    import time; time.sleep(REQUEST_DELAY)

print("\n完成")

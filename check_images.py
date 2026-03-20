import os, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

root = 'E:/Documents/frontend-online/ecp-ui-plus-docs/docs'
image_refs = {}

for dirpath, _, files in os.walk(root):
    normalized = dirpath.replace(chr(92), '/')
    if '/guidance/' in normalized:
        continue
    for fn in files:
        if not fn.endswith('.md'):
            continue
        fp = os.path.join(dirpath, fn)
        with open(fp, encoding='utf-8') as f:
            content = f.read()
        for m in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)', content):
            url = m.group(1)
            if url.startswith('http://') or url.startswith('https://'):
                continue
            if url.startswith('../../'):
                continue   # already local relative
            rel_dir = os.path.relpath(fp, root).replace(chr(92), '/')
            image_refs.setdefault(url, []).append(rel_dir)

if not image_refs:
    print('ecp-ui-plus 文档（除 guidance）中无外部图片引用')
else:
    print(f'发现 {len(image_refs)} 个图片引用:')
    for url in sorted(image_refs):
        print(f'  {url}')
        for r in image_refs[url]:
            print(f'    <- {r}')

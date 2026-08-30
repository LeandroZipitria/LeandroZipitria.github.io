#!/usr/bin/env python3
from pathlib import Path
import base64, mimetypes, re, shutil

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'site_preview'
OUT = ROOT / 'standalone_preview'
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
css = (ROOT/'styles.css').read_text(encoding='utf-8')

def data_uri(path: Path):
    mime = mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
    return f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode('ascii')

def inline_file(doc: str):
    doc = re.sub(r'<link rel="stylesheet" href="styles\.css">', lambda m: '<style>\n'+css+'\n</style>', doc)
    pat = re.compile(r'src="(assets/[^"]+)"')
    def repl(m):
        rel=m.group(1)
        p=ROOT/rel
        if p.exists():
            return f'src="{data_uri(p)}"'
        return m.group(0)
    return pat.sub(repl, doc)

for p in SRC.glob('*.html'):
    out=OUT/p.name
    out.write_text(inline_file(p.read_text(encoding='utf-8')),encoding='utf-8')
print(OUT)

# Keep the published regulation book available from standalone preview links.
if (ROOT/'libro-regulacion').exists():
    shutil.copytree(ROOT/'libro-regulacion', OUT/'libro-regulacion')

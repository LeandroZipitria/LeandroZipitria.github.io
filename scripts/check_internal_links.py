#!/usr/bin/env python3
"""Check internal links in the Quarto source without touching external URLs."""
from pathlib import Path
import argparse, re, sys
from urllib.parse import unquote

parser = argparse.ArgumentParser()
parser.add_argument('--root', default='.')
parser.add_argument('--include-files', action='store_true', help='also require files/... targets to exist')
args = parser.parse_args()
root = Path(args.root).resolve()

sources = list(root.glob('*.qmd')) + [root/'_quarto.yml']
pattern = re.compile(r'(?:href=["\']|\]\()([^"\')#?]+)')
missing=[]
checked=0

for src in sources:
    if not src.exists():
        continue
    text=src.read_text(encoding='utf-8')
    for raw in pattern.findall(text):
        target=unquote(raw.strip().strip('<>'))
        if not target or target.startswith(('http://','https://','mailto:','tel:','javascript:')):
            continue
        if target.startswith('#'):
            continue
        if target.startswith('files/') and not args.include_files:
            continue
        # Public .html page links correspond to .qmd sources during authoring.
        p = root/target
        if target.endswith('.html'):
            q = root/(target[:-5]+'.qmd')
            exists = p.exists() or q.exists()
        else:
            exists = p.exists()
        checked += 1
        if not exists:
            missing.append((src.name,target))

print(f'Checked {checked} internal targets.')
if missing:
    print('Missing targets:')
    for src,target in missing:
        print(f'  {src}: {target}')
    sys.exit(1)
print('PASS: all checked internal targets exist.')

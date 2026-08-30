#!/usr/bin/env python3
from pathlib import Path
import subprocess, shutil, re, html

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'site_preview'
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
shutil.copytree(ROOT/'assets', OUT/'assets')
shutil.copy2(ROOT/'styles.css', OUT/'styles.css')
# Current teaching PDFs are copied so their links work in the offline preview.
if (ROOT/'files').exists():
    shutil.copytree(ROOT/'files', OUT/'files')
if (ROOT/'libro-regulacion').exists():
    shutil.copytree(ROOT/'libro-regulacion', OUT/'libro-regulacion')

pages=['index','bio','research','teaching','professional','texflow','blog','personal','reading','contact','404']
main_nav=[('About','bio.html'),('Research','research.html'),('Teaching','teaching.html'),('Professional','professional.html'),('TeXFlow','texflow.html')]
more_nav=[('Writing & Media','blog.html'),('Personal','personal.html'),('Reading','reading.html'),('Contact','contact.html')]

def meta_title(text,name):
    m=re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', text, re.M)
    return m.group(1) if m else name.title()

def strip_front_matter(text):
    if text.startswith('---'):
        parts=text.split('---',2)
        if len(parts)==3: return parts[2]
    return text

for name in pages:
    src=ROOT/f'{name}.qmd'
    txt=src.read_text(encoding='utf-8')
    title=meta_title(txt,name)
    body_src=OUT/f'.{name}.md'
    body_src.write_text(strip_front_matter(txt),encoding='utf-8')
    body=subprocess.check_output(['pandoc',str(body_src),'-f','markdown+raw_html+fenced_divs','-t','html5'],text=True)
    body_src.unlink()
    links=''.join(f'<a href="{href}">{label}</a>' for label,href in main_nav)
    more=''.join(f'<a href="{href}">{label}</a>' for label,href in more_nav)
    nav=f'''<nav class="preview-nav"><div class="preview-nav-inner"><a class="preview-brand" href="index.html"><img src="assets/site/lz-mark.svg" alt=""><span>Leandro Zipitría</span></a><div class="preview-links">{links}<details class="preview-more"><summary>More</summary><div class="preview-more-menu">{more}</div></details></div></div></nav>'''
    doc=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · Leandro Zipitría</title><link rel="stylesheet" href="styles.css"></head><body>{nav}<main>{body}</main><footer class="preview-footer"><div class="preview-footer-inner"><span>© Leandro Zipitría</span><span>Industrial Organization · Applied Microeconomics</span></div></footer></body></html>'''
    (OUT/f'{name}.html').write_text(doc,encoding='utf-8')
print(OUT)

"""Dependency-free checks for the static GitHub Pages site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re

ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.refs, self.errors = set(), [], []
        self.h1 = 0
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids: self.errors.append('duplicate id: '+a['id'])
            self.ids.add(a['id'])
        if tag == 'h1': self.h1 += 1
        if tag == 'img' and 'alt' not in a: self.errors.append('missing image alt')
        for key in ('href','src'):
            if a.get(key): self.refs.append(a[key])

pages = {f: Page(f.read_text()) for f in ROOT.glob('*.html')}
errors=[]
for file, page in pages.items():
    errors.extend(f'{file.name}: {e}' for e in page.errors)
    if page.h1 != 1: errors.append(f'{file.name}: expected one h1')
    for ref in page.refs:
        u=urlsplit(ref)
        if u.scheme or u.netloc: continue
        target=(file.parent / unquote(u.path)).resolve() if u.path else file
        if not target.is_file(): errors.append(f'{file.name}: missing {ref}')
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
            errors.append(f'{file.name}: missing anchor {ref}')
for f in ROOT.glob('*.css'):
    for ref in re.findall(r'url\([\"\']?([^\)\"\']+)',f.read_text()):
        if not urlsplit(ref).scheme and not (f.parent/ref).is_file(): errors.append(f'{f.name}: missing {ref}')
if errors: raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} pages; local links, anchors, assets, heading counts and image alt attributes.')

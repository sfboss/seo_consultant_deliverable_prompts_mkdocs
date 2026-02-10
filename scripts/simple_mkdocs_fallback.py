#!/usr/bin/env python3
from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
SITE = ROOT / 'site'

NAV_RE = re.compile(r"^\s*-\s+([^:]+):\s+(.+\.md)\s*$")


def parse_nav(mkdocs_file: Path):
    pages = []
    for line in mkdocs_file.read_text(encoding='utf-8').splitlines():
        m = NAV_RE.match(line)
        if m:
            title = m.group(1).strip()
            md_path = m.group(2).strip()
            pages.append((title, md_path))
    return pages


def md_to_html(md_text: str):
    out = []
    in_list = False
    in_code = False
    for raw in md_text.splitlines():
        line = raw.rstrip('\n')
        if line.strip().startswith('```'):
            if not in_code:
                out.append('<pre><code>')
                in_code = True
            else:
                out.append('</code></pre>')
                in_code = False
            continue
        if in_code:
            out.append(html.escape(line))
            continue

        if not line.strip():
            if in_list:
                out.append('</ul>')
                in_list = False
            continue

        if line.startswith('#'):
            if in_list:
                out.append('</ul>')
                in_list = False
            level = len(line) - len(line.lstrip('#'))
            text = line[level:].strip()
            out.append(f'<h{level}>{html.escape(text)}</h{level}>')
            continue

        if line.lstrip().startswith(('- ', '* ')):
            if not in_list:
                out.append('<ul>')
                in_list = True
            li = line.lstrip()[2:].strip()
            out.append(f'<li>{html.escape(li)}</li>')
            continue

        if in_list:
            out.append('</ul>')
            in_list = False
        out.append(f'<p>{html.escape(line)}</p>')

    if in_list:
        out.append('</ul>')
    if in_code:
        out.append('</code></pre>')

    body = '\n'.join(out)
    return body


def render_page(title: str, nav, body_html: str):
    nav_items = []
    for nav_title, rel_html in nav:
        nav_items.append(f'<li><a href="{html.escape(rel_html)}">{html.escape(nav_title)}</a></li>')
    nav_html = '\n'.join(nav_items)
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)}</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 0; background: #f7f7fb; color: #111; }}
    .layout {{ display: grid; grid-template-columns: 280px 1fr; min-height: 100vh; }}
    nav {{ background: #1f2a44; color: #fff; padding: 20px; }}
    nav h2 {{ margin-top: 0; font-size: 18px; }}
    nav a {{ color: #cfe0ff; text-decoration: none; }}
    nav li {{ margin: 8px 0; line-height: 1.4; }}
    main {{ padding: 30px 40px; max-width: 1000px; }}
    h1,h2,h3,h4 {{ color: #223357; }}
    pre {{ background: #232a36; color: #f4f6ff; padding: 12px; overflow-x: auto; border-radius: 6px; }}
    p, li {{ line-height: 1.6; }}
    @media (max-width: 900px) {{ .layout {{ grid-template-columns: 1fr; }} nav {{ position: sticky; top: 0; }} }}
  </style>
</head>
<body>
  <div class="layout">
    <nav>
      <h2>SEO Deliverable Prompt Library</h2>
      <ul>{nav_html}</ul>
    </nav>
    <main>{body_html}</main>
  </div>
</body>
</html>'''


def main():
    mkdocs_file = ROOT / 'mkdocs.yml'
    pages = parse_nav(mkdocs_file)
    SITE.mkdir(exist_ok=True)

    nav = []
    for title, md in pages:
        rel_html = str(Path(md).with_suffix('.html')).replace('\\', '/')
        nav.append((title, rel_html))

    for title, md in pages:
        src = DOCS / md
        if not src.exists():
            continue
        rel_html = Path(md).with_suffix('.html')
        out_path = SITE / rel_html
        out_path.parent.mkdir(parents=True, exist_ok=True)
        body = md_to_html(src.read_text(encoding='utf-8'))
        out_path.write_text(render_page(title, nav, body), encoding='utf-8')

    # index redirect
    index = SITE / 'index.html'
    if not index.exists() and pages:
        first = str(Path(pages[0][1]).with_suffix('.html')).replace('\\', '/')
        index.write_text(f'<meta http-equiv="refresh" content="0; url={html.escape(first)}">', encoding='utf-8')

    print(f'Generated {len(pages)} pages in {SITE}')


if __name__ == '__main__':
    main()

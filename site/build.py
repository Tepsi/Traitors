#!/usr/bin/env python3
"""Statikus oldal építése a fejezetekből. Csak az elérkezett megjelenési dátumú fejezetek kerülnek ki."""
import datetime, html, pathlib, re, shutil, zoneinfo
import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"
TITLE = "Árulók – Halálos kastély"
today = datetime.datetime.now(zoneinfo.ZoneInfo("Europe/Budapest")).date()

chapters = []
for line in (ROOT / "site" / "menetrend.txt").read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    name, date = [x.strip() for x in line.split(";")]
    if datetime.date.fromisoformat(date) <= today:
        src = ROOT / "fejezetek" / name
        if not src.exists():
            continue
        text = src.read_text(encoding="utf-8")
        m = re.search(r"^#\s+(\d+)\.\s*fejezet:\s*(.+)$", text, re.M)
        num, title = (m.group(1), m.group(2).strip()) if m else (str(len(chapters) + 1), name)
        chapters.append(dict(name=name, slug=name[:-3], text=text, num=num, title=title, date=date))

CSS = """
:root{--bg:#fbf8f3;--fg:#1d1a17;--mut:#6b625a;--acc:#7a1f1f;--line:#e2d9cd}
@media (prefers-color-scheme:dark){:root{--bg:#161412;--fg:#e8e1d8;--mut:#9a8f84;--acc:#d06a5f;--line:#2e2924}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:19px/1.7 Georgia,'Times New Roman',serif}
main{max-width:40rem;margin:0 auto;padding:2rem 16px 4rem}
header.site{max-width:40rem;margin:0 auto;padding:1.2rem 16px 0;font-size:.9rem}
header.site a{color:var(--mut);text-decoration:none}
a{color:var(--acc)}
h1{font-size:1.9rem;line-height:1.25;margin:1.5rem 0 1rem}
p{margin:0 0 1.1rem}
hr{border:0;border-top:1px solid var(--line);margin:2rem 0}
nav.pn{display:flex;justify-content:space-between;gap:1rem;margin-top:3rem;padding-top:1rem;border-top:1px solid var(--line);font-size:.95rem}
ul.toc{list-style:none;padding:0}
ul.toc li{padding:.6rem 0;border-bottom:1px solid var(--line)}
.date{color:var(--mut);font-size:.85rem;margin-left:.5rem}
.note{color:var(--mut);font-size:.85rem;margin-top:3rem}
"""

def page(title, body, is_index=False):
    return f"""<!doctype html>
<html lang="hu"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{'' if is_index else '../'}style.css">
</head><body>
<header class="site"><a href="{'' if is_index else '../'}index.html">{TITLE}</a></header>
<main>{body}</main></body></html>"""

OUT.mkdir(exist_ok=True)
(OUT / "style.css").write_text(CSS, encoding="utf-8")

md = markdown.Markdown(extensions=["smarty"], extension_configs={"smarty": {"smart_dashes": False}})
for i, c in enumerate(chapters):
    md.reset()
    body = md.convert(c["text"])
    prev_ = chapters[i - 1] if i > 0 else None
    next_ = chapters[i + 1] if i + 1 < len(chapters) else None
    nav = '<nav class="pn"><span>%s</span><span><a href="../index.html">Fejezetek</a></span><span>%s</span></nav>' % (
        f'<a href="../{prev_["slug"]}/index.html">← {html.escape(prev_["title"])}</a>' if prev_ else "",
        f'<a href="../{next_["slug"]}/index.html">{html.escape(next_["title"])} →</a>' if next_ else "")
    d = OUT / c["slug"]
    d.mkdir(exist_ok=True)
    (d / "index.html").write_text(page(f'{c["num"]}. fejezet: {c["title"]} – {TITLE}', body + nav), encoding="utf-8")

toc = "".join(
    f'<li><a href="{c["slug"]}/index.html">{c["num"]}. {html.escape(c["title"])}</a><span class="date">{c["date"]}</span></li>'
    for c in chapters)
intro = (ROOT / "site" / "bevezeto.html").read_text(encoding="utf-8")
(OUT / "index.html").write_text(page(TITLE, f"<h1>{TITLE}</h1>{intro}<h2>Fejezetek</h2><ul class=\"toc\">{toc}</ul>", True), encoding="utf-8")
print(f"{len(chapters)} fejezet kész ({today})")

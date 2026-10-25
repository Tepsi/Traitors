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
img{max-width:100%;height:auto;display:block;margin:1.5rem auto;border-radius:2px}
.cover{text-align:center}
.cover img{max-width:28rem;width:100%;margin:0 auto 1rem}
.cover h1{font-size:2.6rem;letter-spacing:.04em;margin:.5rem 0}
.cover h1 span{display:block;font-size:1.4rem;font-weight:normal;color:var(--mut);letter-spacing:.2em;text-transform:uppercase;margin-top:.4rem}
.tag{color:var(--mut);font-style:italic}
.btn{display:inline-block;padding:.6rem 1.6rem;margin:.3rem;background:var(--acc);color:#fff;text-decoration:none;border-radius:2px;font-size:1rem}
.btn.alt{background:transparent;color:var(--acc);border:1px solid var(--acc)}
.legal{margin-top:3rem;padding-top:1.2rem;border-top:1px solid var(--line);font-size:.8rem;line-height:1.55;color:var(--mut)}
.legal h2{font-size:.9rem;text-transform:uppercase;letter-spacing:.1em;margin:0 0 .6rem}
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
<main>{body}</main>
<script data-goatcounter="https://tepsi.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
</body></html>"""

OUT.mkdir(exist_ok=True)
if (ROOT / "kepek").exists():
    shutil.copytree(ROOT / "kepek", OUT / "kepek", ignore=shutil.ignore_patterns("*.md", "*.svg", "*.png"), dirs_exist_ok=True)
shutil.copy(ROOT / "site" / "borito.png", OUT / "borito.png")
(OUT / "style.css").write_text(CSS, encoding="utf-8")

md = markdown.Markdown(extensions=["smarty"], extension_configs={"smarty": {"smart_dashes": False}})
for i, c in enumerate(chapters):
    md.reset()
    body = md.convert(c["text"])
    prev_ = chapters[i - 1] if i > 0 else None
    next_ = chapters[i + 1] if i + 1 < len(chapters) else None
    nav = '<nav class="pn"><span>%s</span><span><a href="../fejezetek.html">Fejezetek</a></span><span>%s</span></nav>' % (
        f'<a href="../{prev_["slug"]}/index.html">← {html.escape(prev_["title"])}</a>' if prev_ else "",
        f'<a href="../{next_["slug"]}/index.html">{html.escape(next_["title"])} →</a>' if next_ else "")
    d = OUT / c["slug"]
    d.mkdir(exist_ok=True)
    (d / "index.html").write_text(page(f'{c["num"]}. fejezet: {c["title"]} – {TITLE}', body + nav), encoding="utf-8")

toc = "".join(
    f'<li><a href="{c["slug"]}/index.html">{c["num"]}. {html.escape(c["title"])}</a><span class="date">{c["date"]}</span></li>'
    for c in chapters)
intro = (ROOT / "site" / "bevezeto.html").read_text(encoding="utf-8")
legal = (ROOT / "site" / "jogi.html").read_text(encoding="utf-8")
(OUT / "fejezetek.html").write_text(page("Fejezetek – " + TITLE, f"{intro}<hr><h1>Fejezetek</h1><ul class=\"toc\">{toc}</ul>", True), encoding="utf-8")
first = f'<a class="btn" href="{chapters[0]["slug"]}/index.html">Olvasás</a> ' if chapters else ""
cover = f"""<div class="cover"><img src="borito.png" alt="A Holdvári-kastély sziluettje a telihold előtt">
<h1>Árulók<br><span>Halálos kastély</span></h1>
<p class="tag">Huszonkét híresség. Egy kastély. Minden éjjel egy üres szék.</p>
<p>{first}<a class="btn alt" href="fejezetek.html">Fejezetek</a></p></div>
<section class="legal">{legal}</section>"""
(OUT / "index.html").write_text(page(TITLE, cover, True), encoding="utf-8")
print(f"{len(chapters)} fejezet kész ({today})")

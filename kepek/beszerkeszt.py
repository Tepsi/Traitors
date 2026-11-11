#!/usr/bin/env python3
"""A kész illusztrációk beszerkesztése (CLAUDE.md, 6. lépés).

Használat a repó gyökeréből (FF a fejezet száma, például 08):
  python3 kepek/beszerkeszt.py 08                  # 1. .jfif/.jpeg/.JPG -> .jpg átnevezés, jelentés
  (a képeket ezután meg kell nézni a Read eszközzel, és ha valamelyik nem illik, nem szabad beszerkeszteni)
  python3 kepek/beszerkeszt.py 08 --beszerkeszt    # 2. beszerkesztés, README, teendők, build

A beszerkesztés a promptfájl 4. sorában idézett mondatot tartalmazó bekezdés alá teszi a képet.
Ha az idézet nem szerepel szó szerint a fejezetben, hibával leáll. Többször is futtatható:
ami már benne van, azt nem duplázza meg. Kiegészítő: --kihagy NEV[,NEV] a megadott képek (a fájlnév
`FF-SS-cim` része) kihagyásához, ha valamelyik kép nem megfelelő."""
import pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
KEPEK = ROOT / "kepek"
EXTS = {".jfif", ".jpeg", ".JPG", ".JPEG", ".jpe"}


def norm(s):
    return re.sub(r"\s+", " ", s)


def rename(ff):
    out = []
    for p in sorted(KEPEK.glob(f"{ff}-*")):
        if p.suffix in EXTS:
            new = p.with_suffix(".jpg")
            r = subprocess.run(["git", "mv", str(p), str(new)], cwd=ROOT, capture_output=True)
            if r.returncode != 0:
                p.rename(new)
            out.append(new)
    return out


def prompts(ff):
    return sorted(p for p in KEPEK.glob(f"{ff}-*.md") if p.name != "README.md")


def parse(md):
    lines = md.read_text(encoding="utf8").split("\n")
    quote = lines[3].strip()
    quote = quote[1:-1] if quote[:1] in "„\"" else quote
    scene = next((l for l in lines if l.startswith("**Jelenet:**")), "")
    alt = scene.replace("**Jelenet:**", "").strip().split(". ")[0].rstrip(".")
    alt = alt.replace("[", "").replace("]", "")[:110]
    return quote, alt


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    ff = sys.argv[1].zfill(2)
    skip = set()
    if "--kihagy" in sys.argv:
        skip = set(sys.argv[sys.argv.index("--kihagy") + 1].split(","))
    renamed = rename(ff)
    for r in renamed:
        print("átnevezve:", r.name)
    mds = [m for m in prompts(ff) if m.stem not in skip]
    for m in mds:
        has = (KEPEK / f"{m.stem}.jpg").exists()
        print(("van kép:  " if has else "NINCS kép: ") + m.stem)
    if "--beszerkeszt" not in sys.argv:
        return
    chap = next(iter(sorted((ROOT / "fejezetek").glob(f"{ff}-*.md"))), None)
    if chap is None:
        sys.exit("nincs ilyen fejezet")
    lines = chap.read_text(encoding="utf8").split("\n")
    done = []
    for m in mds:
        if not (KEPEK / f"{m.stem}.jpg").exists():
            continue
        quote, alt = parse(m)
        ref = f"../kepek/{m.stem}.jpg"
        if any(ref in l for l in lines):
            print("már benne van:", m.stem)
            done.append(m.stem)
            continue
        idx = [i for i, l in enumerate(lines) if quote in norm(l)]
        if len(idx) != 1:
            sys.exit(f"HIBA: a(z) {m.stem} idézete {len(idx)} helyen található a fejezetben: {quote[:70]}")
        lines[idx[0] + 1:idx[0] + 1] = ["", f"![{alt}]({ref})"]
        print("beszerkesztve:", m.stem, "-> sor", idx[0] + 1)
        done.append(m.stem)
    chap.write_text("\n".join(lines), encoding="utf8")
    readme = KEPEK / "README.md"
    txt = readme.read_text(encoding="utf8").split("\n")
    for i, l in enumerate(txt):
        for name in done:
            if l.startswith(f"| `{name}`") and "kész, beszerkesztve" not in l:
                txt[i] = re.sub(r"\|[^|]*\|\s*$", "| kész, beszerkesztve |", l)
    readme.write_text("\n".join(txt), encoding="utf8")
    todo = ROOT / "projekt" / "teendok.md"
    t = todo.read_text(encoding="utf8")
    n = int(ff)
    t2 = re.sub(rf"- \[ \] {n}\. fejezet illusztrációi[^\n]*", f"- [x] {n}. fejezet illusztrációi: a képek `.jpg`-re átnevezve és beszerkesztve. (C)", t)
    if t2 != t:
        todo.write_text(t2, encoding="utf8")
    r = subprocess.run([sys.executable, "site/build.py"], cwd=ROOT, capture_output=True, text=True)
    missing = [n for n in done if not (ROOT / "_site" / "kepek" / f"{n}.jpg").exists()]
    print("build:", "rendben" if r.returncode == 0 and not missing else f"HIBA {missing} {r.stderr[-200:]}")


if __name__ == "__main__":
    main()

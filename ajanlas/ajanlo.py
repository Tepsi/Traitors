#!/usr/bin/env python3
"""Az ajánlókép elkészítése a projekt/kiesettek.txt alapján.

Használat a repó gyökeréből:
  python3 ajanlas/ajanlo.py N [kimenet.png]

Az N. fejezet ajánlóképe az N−1. fejezet végéig kiesetteket húzza ki (a kiesettek.txt
N−1. sora, ez mindig az olvasói szövegből látszó, kumulatív lista). Az 1. és 2. fejezetnél
senki sem esett ki, ezekhez az eredeti borítót másolja."""
import pathlib, re, shutil, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    n = int(sys.argv[1])
    out = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "ajanlas" / f"ajanlas-{n}.png"
    if n <= 2:
        shutil.copy(ROOT / "site" / "borito.png", out)
        print("eredeti borító másolva:", out)
        return
    rows = {}
    for line in (ROOT / "projekt" / "kiesettek.txt").read_text(encoding="utf8").split("\n"):
        m = re.match(r"^(\d+):\s*(.*)$", line.strip())
        if m:
            rows[int(m.group(1))] = [x.strip() for x in m.group(2).split(",") if x.strip()]
    if n - 1 not in rows:
        sys.exit(f"HIBA: a projekt/kiesettek.txt-ben nincs {n - 1}. sor. Vedd fel a(z) {n - 1}. fejezet végéig kiesetteket az olvasói szöveg alapján.")
    r = subprocess.run([sys.executable, str(ROOT / "ajanlas" / "kihuzas.py"), str(out)] + rows[n - 1], cwd=ROOT)
    sys.exit(r.returncode)


if __name__ == "__main__":
    main()

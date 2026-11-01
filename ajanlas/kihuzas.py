#!/usr/bin/env python3
"""Vörös zsírkrétás kihúzás a borítótáblán.

Használat (a repó gyökeréből):
  python3 ajanlas/kihuzas.py ajanlas/ajanlas-2.png Armstrong Latabar
A nevek a vezetéknevek (ékezet nélkül is jó, kis-nagybetű mindegy). A kimenet a megadott PNG.
Csak azokat add meg, akik az olvasói szöveg szerint addigra kiestek."""
import random, sys, unicodedata, pathlib
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Keretek (x0, y0, x1, y1) az 1024x1024-es borítón, soronként balról jobbra.
NAMES = ["Kabos", "Latabar", "Hofi", "Psota", "Puskas", "Neumann", "Bessenyei", "Zsazsa",
         "Mercury", "Hitchcock", "Dali", "Christie", "Einstein", "Dietrich", "deFunes", "Armstrong",
         "Welles", "Taylor", "Brando", "Spencer", "Callas", "Hepburn"]
ROW1 = [(50, 295, 152, 460), (165, 295, 270, 460), (282, 295, 388, 460), (400, 295, 505, 460),
        (516, 295, 620, 460), (633, 295, 738, 460), (750, 295, 855, 460), (868, 295, 973, 460)]
ROW2 = [(46, 475, 152, 640), (163, 475, 270, 640), (280, 475, 388, 640), (398, 475, 506, 640),
        (516, 475, 622, 640), (633, 475, 740, 640), (752, 475, 858, 640), (868, 475, 975, 640)]
ROW3 = [(103, 655, 222, 830), (235, 655, 352, 830), (365, 655, 483, 830),
        (493, 655, 635, 830), (650, 655, 773, 830), (788, 655, 910, 830)]
BOXES = dict(zip(NAMES, ROW1 + ROW2 + ROW3))

def norm(s):
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).replace(" ", "").lower()
KEYS = {norm(n): n for n in NAMES}

def stroke(layer, p0, p1, rnd, width):
    """Egy kézzel húzott, enyhén hullámzó vonás több átfedő menettel."""
    d = ImageDraw.Draw(layer)
    for _ in range(3):
        n = 14
        pts = []
        off = rnd.uniform(-2.5, 2.5)
        for i in range(n + 1):
            t = i / n
            x = p0[0] + (p1[0] - p0[0]) * t + rnd.uniform(-1.6, 1.6) + off
            y = p0[1] + (p1[1] - p0[1]) * t + rnd.uniform(-1.6, 1.6)
            pts.append((x, y))
        d.line(pts, fill=255, width=width, joint="curve")

def cross(img, box, rnd):
    x0, y0, x1, y1 = box
    mx, my = 7, 7
    w = img.size
    mask = Image.new("L", w, 0)
    a = (x0 - mx + rnd.uniform(-3, 3), y0 - my + rnd.uniform(-3, 3))
    b = (x1 + mx + rnd.uniform(-3, 3), y1 + my + rnd.uniform(-3, 3))
    c = (x1 + mx + rnd.uniform(-3, 3), y0 - my + rnd.uniform(-3, 3))
    e = (x0 - mx + rnd.uniform(-3, 3), y1 + my + rnd.uniform(-3, 3))
    stroke(mask, a, b, rnd, 13)
    stroke(mask, c, e, rnd, 13)
    m = np.asarray(mask.filter(ImageFilter.GaussianBlur(0.8)), dtype=np.float32) / 255.0
    # viaszos szemcsésség: a vonás belsejében is maradnak apró kihagyások
    grain = np.random.default_rng(rnd.randint(0, 10**6)).random(m.shape).astype(np.float32)
    grain = np.asarray(Image.fromarray((grain * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.7)), dtype=np.float32) / 255.0
    grain = np.clip((grain - 0.25) * 2.2, 0, 1)
    alpha = np.clip(m * (0.55 + 0.45 * grain), 0, 1) * 0.96
    base = np.asarray(img, dtype=np.float32)
    red = np.array([196, 22, 28], dtype=np.float32)
    dark = np.array([140, 10, 18], dtype=np.float32)
    col = red * (0.8 + 0.2 * grain[..., None]) + dark * (1 - m[..., None]) * 0.0
    out = base * (1 - alpha[..., None]) + col * alpha[..., None]
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))

def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    out, names = sys.argv[1], sys.argv[2:]
    img = Image.open(ROOT / "site" / "borito.png").convert("RGB")
    for n in names:
        key = KEYS.get(norm(n))
        if not key:
            sys.exit(f"Ismeretlen név: {n}. Lehetséges: {', '.join(NAMES)}")
        img = cross(img, BOXES[key], random.Random(key))
    img.save(out, optimize=True)
    print(f"{out}: {len(names)} kihúzva")

if __name__ == "__main__":
    main()

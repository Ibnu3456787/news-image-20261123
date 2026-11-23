#!/usr/bin/env python3
"""Draw the 11 front-page vignettes for news-image-20261123.

Each vignette is a small flat newspaper-style illustration drawn with PIL
primitives only -- no external images, no randomness, no timestamps, and
NO words or letters inside any picture, so the output is byte-for-byte
reproducible. Run standalone to save PNGs into candidates/ for inspection;
compose.py imports the draw_* functions.

Canvas: 480x300 for every vignette. Art is concentrated in the middle
band (y ~60-240) because compose.py centre-crops the vignettes to wide
tile aspect ratios.
"""

import math
import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 480, 300

INK = (26, 26, 26)
PAPER = (253, 252, 247)
RED = (176, 42, 32)
DARKRED = (130, 28, 22)
GREEN = (34, 120, 70)
BLUE = (30, 80, 140)
NAVY = (18, 38, 66)
SKY = (205, 224, 235)
SAND = (232, 222, 196)
GOLD = (214, 164, 48)
WHITE = (255, 255, 255)
GREY = (120, 118, 112)


def blank(bg):
    img = Image.new("RGB", (W, H), bg)
    return img, ImageDraw.Draw(img)


def seismograph(d, x0, y0, x1, y1, fill, amp=26):
    """Zig-zag seismograph trace between two points."""
    pts = [(x0, (y0 + y1) // 2)]
    n = 26
    steps = [0, 4, -6, 10, -16, 22, -30, 38, -34, 26, -18, 12, -8, 5,
             -3, 2, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    mid = (y0 + y1) // 2
    for i in range(1, n + 1):
        x = x0 + (x1 - x0) * i // n
        pts.append((x, mid + steps[i - 1] * amp // 30))
    d.line(pts, fill=fill, width=5, joint="curve")


def star(d, cx, cy, r, fill):
    """Five-pointed star centred on (cx, cy)."""
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rad = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    d.polygon(pts, fill=fill)


# ------------------------------------------------------------------ 1 lead
def draw_markets():
    """Falling Asian markets, US futures bouncing: red plunge, green dash."""
    img, d = blank(NAVY)
    # grid
    for gy in range(40, H - 40, 40):
        d.line([20, gy, W - 20, gy], fill=(34, 62, 96), width=1)
    # candlesticks falling left to right
    x = 40
    tops = [70, 90, 110, 130, 150, 165, 185, 200]
    for i, t in enumerate(tops):
        col = RED if i % 2 == 0 else DARKRED
        d.rectangle([x, t, x + 26, t + 46], fill=col)
        d.line([x + 13, t - 18, x + 13, t + 64], fill=col, width=4)
        x += 44
    # plunging red line
    d.line([(30, 60), (120, 110), (200, 150), (290, 195), (380, 235),
            (450, 260)], fill=(255, 90, 70), width=7, joint="curve")
    # bouncing green dashed line (US futures)
    for i in range(6):
        x0 = 30 + i * 70
        d.line([x0, 250 - i * 8, x0 + 44, 242 - i * 8],
               fill=(90, 220, 130), width=6)
    # chip
    d.rectangle([392, 24, 452, 84], fill=INK, outline=GOLD, width=3)
    d.rectangle([406, 38, 438, 70], fill=GOLD)
    return img


# ------------------------------------------------------------------ 2 Nepal
def draw_nepal_india():
    """Two flags over a meeting table: Nepal's pennant, India's tricolour."""
    img, d = blank(SKY)
    d.rectangle([0, 230, W, H], fill=SAND)
    # flag poles
    d.rectangle([120, 40, 128, 230], fill=INK)
    d.rectangle([352, 40, 360, 230], fill=INK)
    # Nepal flag (simplified double pennant, crimson with blue edge)
    d.polygon([(128, 48), (128, 150), (208, 108), (168, 108), (208, 88),
               (168, 88)], fill=(220, 20, 60), outline=(0, 0, 150))
    d.ellipse([140, 66, 152, 78], fill=WHITE)
    d.ellipse([140, 116, 152, 128], fill=WHITE)
    # India flag
    d.rectangle([232, 48, 352, 82], fill=(255, 153, 51))
    d.rectangle([232, 82, 352, 116], fill=WHITE)
    d.rectangle([232, 116, 352, 150], fill=(19, 136, 8))
    d.ellipse([284, 88, 308, 112], outline=NAVY, width=3)
    for a in range(0, 360, 30):
        r = math.radians(a)
        d.line([296, 100, 296 + 10 * math.cos(r), 100 + 10 * math.sin(r)],
               fill=NAVY, width=1)
    # table + two chairs
    d.rectangle([150, 190, 330, 206], fill=(120, 72, 30))
    d.rectangle([160, 206, 172, 240], fill=(120, 72, 30))
    d.rectangle([308, 206, 320, 240], fill=(120, 72, 30))
    d.ellipse([205, 150, 235, 180], fill=INK)   # head 1
    d.ellipse([245, 150, 275, 180], fill=INK)   # head 2
    d.rectangle([195, 180, 245, 192], fill=NAVY)
    d.rectangle([235, 180, 285, 192], fill=DARKRED)
    return img


# ------------------------------------------------------------------ 8 Kyiv
def draw_kyiv():
    """Night rescue at a damaged apartment block: broken corner, crane,
    searchlight beam, rubble."""
    img, d = blank((20, 30, 52))
    # stars
    for sx, sy in [(30, 30), (70, 60), (430, 26), (455, 70), (400, 110),
                   (20, 120), (250, 24), (350, 44)]:
        d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=WHITE)
    # searchlight beam from lower left
    d.polygon([(40, 280), (170, 90), (235, 120), (130, 280)],
              fill=(88, 86, 58))
    # apartment block, five storeys
    d.rectangle([90, 80, 330, 260], fill=(198, 196, 188))
    for row in range(4):
        for col in range(3):
            wx = 110 + col * 70
            wy = 100 + row * 38
            d.rectangle([wx, wy, wx + 34, wy + 24], fill=(60, 66, 80))
    # jagged collapsed top-right corner (sky colour bites into the block)
    d.polygon([(250, 80), (330, 80), (330, 160), (305, 138), (290, 165),
               (268, 142), (252, 168)], fill=(20, 30, 52))
    # rubble at the base
    d.polygon([(270, 260), (400, 260), (345, 205)], fill=(120, 118, 112))
    d.polygon([(320, 260), (420, 260), (385, 225)], fill=(100, 98, 92))
    d.polygon([(230, 260), (300, 260), (268, 232)], fill=(140, 138, 130))
    # rescue crane
    d.rectangle([404, 60, 416, 260], fill=(230, 180, 40))
    d.rectangle([300, 54, 416, 66], fill=(230, 180, 40))
    d.line([312, 66, 312, 130], fill=INK, width=3)
    d.rectangle([302, 130, 322, 146], fill=INK)
    # dust clouds near the rubble
    d.ellipse([330, 215, 380, 240], fill=(150, 148, 140))
    d.ellipse([360, 205, 410, 228], fill=(135, 133, 126))
    return img


# ------------------------------------------------------------------ 9 Belgium
def draw_belgium_strike():
    """A grounded plane under a red prohibition ring, a stopped train
    and blank picket signs: the nationwide strike."""
    img, d = blank(SKY)
    # tarmac
    d.rectangle([0, 210, W, H], fill=(150, 148, 142))
    d.line([0, 210, W, 210], fill=WHITE, width=2)
    # aeroplane on the ground, nose right
    d.rounded_rectangle([70, 120, 350, 168], radius=22, fill=WHITE,
                        outline=INK, width=2)
    d.polygon([(340, 128), (385, 138), (385, 152), (340, 160)],
              fill=WHITE, outline=INK)
    d.polygon([(110, 120), (130, 78), (160, 78), (150, 120)],
              fill=(200, 40, 40), outline=INK)
    d.polygon([(190, 166), (250, 210), (285, 210), (240, 166)],
              fill=(180, 180, 180), outline=INK)
    for wx in range(100, 340, 26):
        d.ellipse([wx, 132, wx + 12, 144], fill=BLUE)
    d.rectangle([205, 168, 225, 210], fill=INK)
    d.rectangle([300, 168, 320, 210], fill=INK)
    # red prohibition ring + slash over the plane
    d.ellipse([88, 52, 372, 236], outline=RED, width=9)
    d.line([128, 82, 332, 206], fill=RED, width=9)
    # stopped train, lower right
    d.rectangle([330, 226, 470, 272], fill=(70, 110, 160), outline=INK,
                width=2)
    for wx in range(342, 460, 30):
        d.rectangle([wx, 236, wx + 20, 254], fill=(200, 225, 245))
    d.line([320, 282, W, 282], fill=INK, width=3)
    d.line([320, 292, W, 292], fill=INK, width=3)
    # blank picket signs
    d.line([48, 180, 48, 250], fill=INK, width=5)
    d.rectangle([22, 140, 76, 182], fill=WHITE, outline=RED, width=3)
    d.line([436, 60, 436, 130], fill=INK, width=5)
    d.rectangle([408, 22, 464, 62], fill=WHITE, outline=RED, width=3)
    return img


# ------------------------------------------------------------------ 13 Ghana
def draw_ghana():
    """Amputee World Cup winners: Ghana flag bands, black star, gold
    trophy and a football on the pitch."""
    img, d = blank((44, 130, 70))
    # flag bands across the top
    d.rectangle([0, 0, W, 44], fill=(206, 17, 38))
    d.rectangle([0, 44, W, 88], fill=(244, 194, 0))
    d.rectangle([0, 88, W, 132], fill=(0, 107, 60))
    star(d, 240, 66, 26, INK)
    # pitch lines
    d.ellipse([180, 190, 300, 290], outline=WHITE, width=3)
    d.line([0, 240, W, 240], fill=WHITE, width=2)
    # gold trophy, centre
    d.polygon([(200, 140), (280, 140), (268, 200), (212, 200)],
              fill=GOLD, outline=(150, 110, 20))
    d.arc([188, 140, 212, 190], start=90, end=270, fill=GOLD, width=8)
    d.arc([268, 140, 292, 190], start=270, end=90, fill=GOLD, width=8)
    d.rectangle([232, 200, 248, 224], fill=GOLD)
    d.rectangle([212, 224, 268, 238], fill=(150, 110, 20))
    # football, lower left
    d.ellipse([78, 198, 142, 262], fill=WHITE, outline=INK, width=3)
    d.polygon([(104, 216), (118, 224), (112, 240), (96, 240), (90, 224)],
              fill=INK)
    d.ellipse([84, 246, 96, 258], fill=INK)
    d.ellipse([122, 246, 134, 258], fill=INK)
    # confetti
    for cx, cy, col in [(60, 150, RED), (90, 170, GOLD), (420, 150, RED),
                        (400, 190, WHITE), (360, 150, GOLD),
                        (120, 150, WHITE), (440, 230, GOLD)]:
        d.rectangle([cx, cy, cx + 12, cy + 6], fill=col)
    return img


# ------------------------------------------------------------------ 16 House
def draw_house():
    """US Capitol dome with stars."""
    img, d = blank(NAVY)
    # stars
    for sx, sy in [(40, 40), (90, 24), (400, 30), (440, 60), (60, 90),
                   (420, 100), (30, 140), (450, 150)]:
        d.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=WHITE)
    # Capitol: base + dome
    d.rectangle([90, 200, 390, 260], fill=WHITE)
    d.rectangle([70, 260, 410, 280], fill=(200, 200, 200))
    d.rectangle([120, 170, 360, 200], fill=WHITE)
    d.pieslice([180, 70, 300, 190], start=180, end=360, fill=WHITE)
    d.rectangle([236, 56, 244, 78], fill=WHITE)
    d.ellipse([234, 48, 246, 60], fill=GOLD)
    # columns
    for cx in range(110, 380, 30):
        d.rectangle([cx, 205, cx + 12, 258], fill=(180, 180, 180))
    return img


# ------------------------------------------------------------------ 17 Skubal
def draw_skubal():
    """Baseball diamond, ball and bat."""
    img, d = blank((44, 130, 70))
    # diamond
    d.polygon([(240, 60), (420, 200), (240, 290), (60, 200)],
              fill=(150, 200, 120))
    d.polygon([(240, 110), (350, 195), (240, 260), (130, 195)],
              fill=(205, 175, 120))
    # pitcher's mound + home plate
    d.ellipse([215, 175, 265, 205], fill=(205, 175, 120))
    d.polygon([(232, 252), (248, 252), (248, 262), (240, 268), (232, 262)],
              fill=WHITE)
    # baseball
    d.ellipse([150, 30, 250, 130], fill=WHITE, outline=INK, width=3)
    d.arc([160, 40, 240, 120], start=300, end=60, fill=RED, width=5)
    d.arc([160, 40, 240, 120], start=120, end=240, fill=RED, width=5)
    # bat
    d.line([330, 40, 420, 130], fill=(190, 140, 80), width=14)
    d.ellipse([318, 28, 342, 52], fill=(190, 140, 80))
    return img


# ------------------------------------------------------------------ 20 49ers
def draw_49ers():
    """American football under floodlights: ball, goalpost, red and
    gold end zones."""
    img, d = blank((20, 32, 60))
    # floodlight towers
    for tx in (40, 400):
        d.rectangle([tx, 30, tx + 8, 120], fill=(120, 120, 120))
        d.rectangle([tx - 14, 18, tx + 22, 44], fill=(230, 230, 230),
                    outline=INK, width=2)
        for lx in range(tx - 8, tx + 18, 10):
            d.ellipse([lx, 24, lx + 6, 30], fill=GOLD)
    # red and gold stripes across the top
    d.rectangle([0, 0, W, 12], fill=(170, 0, 0))
    d.rectangle([0, 12, W, 20], fill=GOLD)
    # field
    d.rectangle([0, 120, W, H], fill=(44, 130, 70))
    for y in range(150, 290, 40):
        d.line([0, y, W, y], fill=WHITE, width=3)
    # football, centre
    d.ellipse([140, 150, 340, 240], fill=(140, 70, 30), outline=INK,
              width=3)
    d.line([200, 195, 280, 195], fill=WHITE, width=5)
    for lx in range(210, 280, 14):
        d.line([lx, 185, lx, 205], fill=WHITE, width=4)
    # goalpost, right
    d.line([420, 100, 420, 250], fill=(230, 200, 60), width=10)
    d.line([380, 100, 460, 100], fill=(230, 200, 60), width=10)
    d.line([380, 100, 380, 150], fill=(230, 200, 60), width=8)
    d.line([460, 100, 460, 150], fill=(230, 200, 60), width=8)
    return img


# ------------------------------------------------------------------ 24 Fit to Lead
def draw_fit_to_lead():
    """Parliament House, Canberra, and a stressed silhouette."""
    img, d = blank(SKY)
    # grass roof + flag mast
    d.polygon([(0, 260), (120, 190), (360, 190), (480, 260)],
              fill=(70, 140, 70))
    d.rectangle([236, 60, 244, 195], fill=INK)
    d.rectangle([244, 60, 300, 92], fill=NAVY)
    d.ellipse([252, 68, 264, 80], fill=WHITE)
    d.ellipse([272, 72, 280, 80], fill=WHITE)
    # head silhouette with stress lines
    d.ellipse([150, 60, 230, 150], fill=NAVY)
    d.rectangle([140, 140, 240, 190], fill=NAVY)
    for lx, ly in [(120, 80), (112, 112), (252, 84), (256, 116)]:
        d.line([lx, ly, lx + 18, ly + 6], fill=RED, width=4)
    return img


# ------------------------------------------------------------------ 26 Cricket
def draw_cricket():
    """Bat, ball and stumps on the final day -- a drawn Test: both
    sets of stumps stand, nobody wins."""
    img, d = blank((44, 130, 70))
    # pitch
    d.rectangle([150, 40, 330, 260], fill=(205, 175, 120))
    # stumps, top end
    for sx in (215, 232, 249):
        d.rectangle([sx, 60, sx + 8, 110], fill=(230, 200, 120))
    d.rectangle([213, 56, 259, 62], fill=(230, 200, 120))
    # stumps, bottom end -- still standing at the close
    for sx in (215, 232, 249):
        d.rectangle([sx, 210, sx + 8, 252], fill=(230, 200, 120))
    d.rectangle([213, 252, 259, 258], fill=(230, 200, 120))
    # bat, leaning
    d.polygon([(290, 120), (320, 120), (330, 220), (300, 230), (282, 200)],
              fill=(220, 180, 110), outline=INK)
    d.rectangle([300, 96, 312, 124], fill=INK)
    # red ball
    d.ellipse([160, 150, 200, 190], fill=RED, outline=INK, width=2)
    d.arc([164, 154, 196, 186], start=200, end=340, fill=WHITE, width=2)
    return img


# ------------------------------------------------------------------ 27 Meldrum
def draw_meldrum():
    """A stage falls quiet: spotlight, microphone, vinyl record and a
    wide-brimmed hat."""
    img, d = blank((28, 28, 38))
    # spotlight cone
    d.polygon([(240, 0), (120, 300), (360, 300)], fill=(74, 70, 52))
    # small stars
    for sx, sy in [(40, 40), (80, 90), (430, 50), (400, 100), (30, 150),
                   (450, 160)]:
        d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(200, 200, 200))
    # vinyl record, left
    d.ellipse([48, 150, 158, 260], fill=INK, outline=(90, 90, 100), width=2)
    d.ellipse([70, 172, 136, 238], outline=(90, 90, 100), width=2)
    d.ellipse([88, 190, 118, 220], fill=RED)
    d.ellipse([99, 201, 107, 209], fill=PAPER)
    # microphone on its stand, centre
    d.line([240, 130, 240, 262], fill=(150, 150, 150), width=6)
    d.ellipse([212, 262, 268, 274], fill=(150, 150, 150))
    d.ellipse([212, 78, 268, 134], fill=(200, 200, 205), outline=INK,
              width=2)
    for gy in range(88, 128, 10):
        d.line([218, gy, 262, gy], fill=(120, 120, 125), width=2)
    d.rectangle([228, 132, 252, 148], fill=(120, 120, 125))
    # wide-brimmed hat, right
    d.ellipse([322, 196, 452, 226], fill=(70, 50, 30))
    d.pieslice([348, 140, 426, 210], start=180, end=360, fill=(90, 65, 40))
    d.rectangle([348, 192, 426, 202], fill=INK)
    return img


# ------------------------------------------------------------------ unused
# The stories below appear in the index, not as tiles; their vignettes
# are kept (text-free) for reference and are not rendered on the page.

def draw_cop31():
    """Globe and a failed climate deal: thermometer and leaf."""
    img, d = blank(SKY)
    d.ellipse([110, 40, 370, 260], fill=(90, 160, 220), outline=NAVY, width=4)
    d.ellipse([150, 80, 230, 150], fill=GREEN)
    d.ellipse([250, 150, 330, 220], fill=GREEN)
    d.ellipse([200, 180, 260, 230], fill=GREEN)
    d.rectangle([400, 60, 424, 200], fill=WHITE, outline=INK, width=3)
    d.ellipse([390, 190, 434, 234], fill=WHITE, outline=INK, width=3)
    d.rectangle([404, 130, 420, 200], fill=RED)
    d.ellipse([396, 196, 428, 228], fill=RED)
    d.polygon([(60, 200), (110, 160), (120, 210), (70, 230)], fill=GREEN)
    return img


def draw_jets():
    """American football and a goalpost."""
    img, d = blank((44, 130, 70))
    for y in range(50, 280, 46):
        d.line([0, y, W, y], fill=WHITE, width=3)
    d.ellipse([140, 90, 340, 210], fill=(140, 70, 30), outline=INK, width=3)
    d.line([200, 150, 280, 150], fill=WHITE, width=5)
    for lx in range(210, 280, 14):
        d.line([lx, 140, lx, 160], fill=WHITE, width=4)
    d.line([420, 40, 420, 200], fill=(230, 200, 60), width=10)
    d.line([380, 40, 460, 40], fill=(230, 200, 60), width=10)
    d.line([380, 40, 380, 90], fill=(230, 200, 60), width=8)
    d.line([460, 40, 460, 90], fill=(230, 200, 60), width=8)
    return img


def draw_anthropic():
    """Ticker screen with candlesticks."""
    img, d = blank(INK)
    d.rectangle([0, 0, W, 64], fill=(20, 20, 20))
    d.rectangle([0, 64, W, 68], fill=GOLD)
    x = 50
    for i, (t, b) in enumerate([(90, 150), (120, 180), (100, 140),
                                (140, 200), (110, 160), (90, 130)]):
        col = GREEN if i % 2 else RED
        d.rectangle([x, t, x + 34, b], fill=col)
        d.line([x + 17, t - 20, x + 17, b + 20], fill=col, width=4)
        x += 62
    return img


def draw_peru_quake():
    """Andes peaks and a seismograph trace."""
    img, d = blank(SKY)
    d.polygon([(0, 260), (120, 90), (220, 260)], fill=(110, 90, 70))
    d.polygon([(120, 90), (160, 140), (120, 155), (90, 135)], fill=WHITE)
    d.polygon([(180, 260), (320, 60), (440, 260)], fill=(140, 115, 85))
    d.polygon([(320, 60), (360, 120), (320, 135), (288, 115)], fill=WHITE)
    d.polygon([(380, 260), (470, 130), (480, 150), (480, 260)],
              fill=(110, 90, 70))
    d.rectangle([0, 260, W, H], fill=(90, 120, 60))
    d.rectangle([20, 20, 460, 80], fill=WHITE, outline=INK, width=2)
    seismograph(d, 30, 30, 450, 70, RED)
    return img


def draw_aegean_quake():
    """Aegean waves and a seismograph trace."""
    img, d = blank(SKY)
    d.ellipse([380, 24, 440, 84], fill=GOLD)
    d.rectangle([0, 150, W, H], fill=(60, 130, 190))
    for row, y0 in enumerate([170, 205, 240, 275]):
        for x in range(0, W, 60):
            d.arc([x, y0, x + 60, y0 + 30], start=180, end=360,
                  fill=WHITE, width=4)
    d.polygon([(0, 150), (160, 90), (300, 150)], fill=SAND)
    d.rectangle([60, 110, 100, 150], fill=WHITE, outline=INK, width=2)
    d.rectangle([110, 118, 145, 150], fill=WHITE, outline=INK, width=2)
    d.rectangle([20, 20, 340, 70], fill=WHITE, outline=INK, width=2)
    seismograph(d, 30, 28, 330, 62, RED)
    return img


# Illustrated stories only: lead + 10 tiles, keyed by story number.
VIGNETTES = {
    1: draw_markets,
    2: draw_nepal_india,
    8: draw_kyiv,
    9: draw_belgium_strike,
    13: draw_ghana,
    16: draw_house,
    17: draw_skubal,
    20: draw_49ers,
    24: draw_fit_to_lead,
    26: draw_cricket,
    27: draw_meldrum,
}


def main():
    out = os.path.join(HERE, "candidates")
    os.makedirs(out, exist_ok=True)
    for num, fn in sorted(VIGNETTES.items()):
        path = os.path.join(out, "vignette_%02d.png" % num)
        fn().save(path, optimize=True)
        print("wrote %s" % path)


if __name__ == "__main__":
    main()

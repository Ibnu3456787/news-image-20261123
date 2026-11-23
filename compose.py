#!/usr/bin/env python3
"""Build entry.png: a newspaper front page summing up Monday 23 Nov 2026.

Layout (proven by the news-image-20261122 entry): masthead, lead band,
ten illustrated tiles in two rows of five, then a bottom band with a
world map (left) and an index of the remaining stories (right), plus
continent counts, a BY THE NUMBERS line and a sources footer.

Deterministic: the same inputs always produce the same bytes.  Prints a
warning for any text-wrap overflow, tile overflow, font shrink-floor
miss, map pin outside the frame, pin collision, page overflow, or
>1 MiB output.  The shipped build must print zero warnings.

Usage: python3 compose.py [output-path]   (default: entry.png next to
this file)
"""

import hashlib
import json
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFont

from vignettes import VIGNETTES

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- page setup
W, H = 1024, 1024
MARGIN = 16
CW = W - 2 * MARGIN  # 992

PAPER = (250, 246, 236)
INK = (22, 22, 22)
RED = (176, 42, 32)
GREY = (112, 106, 96)

FONT_DIR = "/usr/share/fonts/truetype/liberation"
SERIF_B = os.path.join(FONT_DIR, "LiberationSerif-Bold.ttf")
SERIF_I = os.path.join(FONT_DIR, "LiberationSerif-Italic.ttf")
SANS_R = os.path.join(FONT_DIR, "LiberationSans-Regular.ttf")
SANS_B = os.path.join(FONT_DIR, "LiberationSans-Bold.ttf")

WARNINGS = []


def warn(msg):
    WARNINGS.append(msg)
    print("WARNING: " + msg, file=sys.stderr)


def font(path, size):
    return ImageFont.truetype(path, size)


def crop_to(img, w, h):
    """Centre-crop to the target aspect ratio, then resize."""
    iw, ih = img.size
    target = w / h
    src = iw / ih
    if src > target:  # too wide: trim sides
        nw = int(ih * target)
        x0 = (iw - nw) // 2
        img = img.crop((x0, 0, x0 + nw, ih))
    else:  # too tall: trim top/bottom
        nh = int(iw / target)
        y0 = (ih - nh) // 2
        img = img.crop((0, y0, iw, y0 + nh))
    return img.resize((w, h), Image.LANCZOS)


# ------------------------------------------------------------------- content
# Every figure below is taken from research-notes.md and must match it.

LEAD = {
    "num": 1,
    "region": "ASIA",
    "headline": "AI sell-off deepens as Asia slides",
    "account": ("Seoul's KOSPI plunges 5.41% intraday to 4,606.44, "
                "halting program selling for five minutes; Taiwan falls "
                "0.93% in morning trade. Seoul readies about 10 trillion "
                "won in stabilisation funds."),
    "dateline": "SEOUL \u00b7 MONDAY",
}

# 10 illustrated tiles, in reading order (row 1, then row 2).
TILES = [
    {"num": 2, "region": "ASIA",
     "headline": "Nepal's PM holds talks with Modi in Delhi",
     "sub": "Nepal seeks a $2 billion package; joint vision document due."},
    {"num": 8, "region": "EUROPE",
     "headline": "Kyiv toll rises to 12 as rescuers dig on",
     "sub": "Dymer toll reaches nine of 12 dead across the Kyiv region."},
    {"num": 13, "region": "AFRICA",
     "headline": "Ghana win Amputee World Cup",
     "sub": "Opentil's 32nd-minute goal beats Morocco 1\u20130 in Mexico."},
    {"num": 16, "region": "N. AMERICA",
     "headline": "Democrats clinch 258 House seats",
     "sub": "Hubbard beats Foxx by 330 votes after a recount; most "
            "since 1992."},
    {"num": 24, "region": "OCEANIA",
     "headline": "Fit to Lead study launches in Canberra",
     "sub": "71% of parliamentarians affected; 97% of them blame online "
            "abuse."},
    {"num": 9, "region": "EUROPE",
     "headline": "Belgium grinds to a halt in nationwide strike",
     "sub": "Most of 429 Brussels flights cancelled; Charleroi grounds "
            "all."},
    {"num": 17, "region": "N. AMERICA",
     "headline": "Skubal signs record $450M Mets deal",
     "sub": "Nine years, $50M a year \u2014 the richest pitcher deal in "
            "history."},
    {"num": 20, "region": "N. AMERICA",
     "headline": "49ers rout Vikings 35\u201310 in Mexico City",
     "sub": "Purdy throws three first-half TD passes; 49ers move to 9\u20131."},
    {"num": 26, "region": "OCEANIA",
     "headline": "New Zealand bat out a draw after India's record 720/9",
     "sub": "Mitchell and Phillips bat 43 overs together to force the "
            "draw."},
    {"num": 27, "region": "OCEANIA",
     "headline": "Molly Meldrum dies aged 83",
     "sub": "Countdown host dies at 5:30am in Melbourne; state funeral "
            "to follow."},
]

# One line per remaining story: (number, headline, region).
# Headlines match research-notes.md; #19, #21 and #28 are shortened
# here to fit one index line (full headlines in research-notes.md).
INDEX = [
    (3, "China\u2013Singapore council meets in Singapore", "ASIA"),
    (4, "Seoul silent on spy chief replacement reports", "ASIA"),
    (5, "Lee's approval rating rises to 37.3%", "ASIA"),
    (6, "Saudi hand seen behind failed COP31 deal", "ASIA"),
    (7, "Three killed in Gaza as truce frays", "ASIA"),
    (10, "M4.2 quake in the Aegean off Bodrum", "EUROPE"),
    (11, "Burnham asks MPs to back his EU deal", "EUROPE"),
    (12, "At least 46 killed in Niger State attacks and reprisals", "AFRICA"),
    (14, "Ex-councillors sue ActionSA for R3.1m", "AFRICA"),
    (15, "Hung Joburg council sits for first time", "AFRICA"),
    (18, "Jets end five-game skid, 27\u201324 over Chargers", "N. AMERICA"),
    (19, "Anthropic options debut; volatility seen at 100\u2013150%",
     "N. AMERICA"),
    (21, "Murray's 45, Jokic's 202nd triple-double win OT thriller",
     "N. AMERICA"),
    (22, "M5.4 quake shakes Peru's Andes as toll rises", "S. AMERICA"),
    (23, "Brazil's lower house votes on Lula's fiscal package",
     "S. AMERICA"),
    (25, "COP31 failure a sign of 'difficult times', says Albanese",
     "OCEANIA"),
    (28, "NZ retail sales surge 2.2%, best in nearly five years",
     "OCEANIA"),
    (29, "Northland's first wind farm opens", "OCEANIA"),
    (30, "Former Silver Ferns captain Julie Carter dies aged 60",
     "OCEANIA"),
    (31, "Albanese runs biggest, best-paid PM's office in 13 years",
     "OCEANIA"),
]

CONTINENT_COUNTS = ("ASIA 7 \u00b7 EUROPE 4 \u00b7 N. AMERICA 6 \u00b7 "
                    "S. AMERICA 2 \u00b7 AFRICA 4 \u00b7 OCEANIA 8")

BY_NUMBERS = ("BY THE NUMBERS \u2014 KOSPI \u22125.41% intraday \u00b7 "
              "$450M Skubal deal \u00b7 258 House seats \u00b7 71% of MPs")

SOURCES = ("Sources: Reuters \u00b7 AP \u00b7 AFP \u00b7 BBC \u00b7 IANS "
           "\u00b7 ABC \u00b7 AAP \u00b7 ESPN \u00b7 NBC Sports \u00b7 "
           "Cricinfo \u00b7 USGS \u00b7 AFAD \u00b7 Stats NZ \u00b7 RNZ "
           "\u00b7 Korea JoongAng Daily \u00b7 Seeking Alpha \u00b7 "
           "Sowetan \u00b7 TimesLIVE \u00b7 Ghana FA \u00b7 Cboe \u00b7 "
           "Anadolu \u00b7 Better Politics Foundation")

# Map pins for the 11 illustrated stories: (lon, lat, offset dx, dy in px).
# Offsets (with leader lines) only where pins would collide or leave the
# frame: Washington/New York, and Canberra/Melbourne/Wellington.
PINS = {
    1: (126.9780, 37.5665, 0, 0),     # Seoul
    2: (77.2090, 28.6139, 0, 0),      # New Delhi
    8: (30.3124, 50.7840, 0, 0),      # Dymer, Kyiv Oblast
    9: (4.3517, 50.8503, 0, 0),       # Brussels
    13: (-0.1870, 5.6037, 0, 0),      # Accra
    16: (-77.0091, 38.8899, 0, 14),   # Washington DC (offset down)
    17: (-73.8458, 40.7571, 0, -14),  # New York (offset up)
    20: (-99.1505, 19.3029, 0, 0),    # Mexico City
    24: (149.1244, -35.3081, 14, -14),  # Canberra (offset right-up)
    26: (174.7803, -41.3005, -16, 0),   # Wellington (offset left)
    27: (144.9983, -37.8230, -18, 14),  # Melbourne (offset left-down)
}

# ---------------------------------------------------------------- text tools

def text_w(d, s, f):
    return d.textlength(s, font=f)


def wrap(d, text, f, max_w):
    """Greedy word wrap; returns a list of lines.

    Long hyphenated words may break after a hyphen, so a word like
    "record-equalling" never forces an extra line on its own.
    """
    frags = []
    for word in text.split():
        parts = word.split("-")
        for i, part in enumerate(parts):
            piece = part + ("-" if i < len(parts) - 1 else "")
            frags.append((piece, len(frags) > 0 and i == 0))
    lines, cur = [], ""
    for piece, spaced in frags:
        trial = cur + (" " if spaced and cur else "") + piece
        if d.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = piece
    if cur:
        lines.append(cur)
    return lines


def draw_centered(d, cx, y, text, f, fill):
    d.text((cx, y), text, font=f, fill=fill, anchor="ma")


def draw_tracked_centered(d, cx, y, text, f, fill, tracking):
    """Draw text centred with extra space between characters."""
    widths = [d.textlength(ch, font=f) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2.0
    for ch, wch in zip(text, widths):
        d.text((x, y), ch, font=f, fill=fill, anchor="la")
        x += wch + tracking


def draw_badge(d, x, y, size, num, num_font):
    d.rectangle([x, y, x + size, y + size], fill=RED)
    d.text((x + size / 2.0, y + size / 2.0 + 0.5), str(num),
           font=num_font, fill=(255, 255, 255), anchor="mm")


def check_bottom(label, bottom, limit):
    if bottom > limit:
        warn("%s overflows its area: bottom %d > %d" % (label, bottom, limit))


# ---------------------------------------------------------------------- map

def load_land():
    with open(os.path.join(HERE, "ne_110m_land.geojson"), "r") as fh:
        data = json.load(fh)
    rings = []
    for feat in data["features"]:
        geom = feat["geometry"]
        if geom["type"] == "Polygon":
            rings.extend(geom["coordinates"])
        elif geom["type"] == "MultiPolygon":
            for poly in geom["coordinates"]:
                rings.extend(poly)
    return rings


def unwrap_ring(ring):
    """Unwrap a lon/lat ring so consecutive longitudes differ by <=180.

    Rings crossing the antimeridian (eastern Russia, Fiji) then draw as
    one continuous shape instead of a line across the whole map.
    """
    out = []
    offset = 0.0
    prev = None
    for lon, lat in ring:
        if prev is not None:
            if lon - prev > 180:
                offset -= 360.0
            elif lon - prev < -180:
                offset += 360.0
        out.append((lon + offset, lat))
        prev = lon
    return out


def draw_map(page, d, fx, fy, fw, fh):
    """Equirectangular world map inside the frame (fx, fy, fw, fh).

    Latitude range is clipped to -60..85 so Antarctica never appears.
    The map is drawn on its own image so shapes crossing the frame edge
    are clipped cleanly.  Returns the projected pin centres.
    """
    ocean = (205, 224, 236)
    land_fill = (232, 222, 196)
    land_edge = (168, 156, 126)
    grid_col = (186, 206, 220)

    lat_top, lat_bot = 85.0, -60.0
    scale = fw / 360.0
    map_h = (lat_top - lat_bot) * scale
    y0 = (fh - map_h) / 2.0

    mimg = Image.new("RGB", (fw, fh), ocean)
    md = ImageDraw.Draw(mimg)

    def proj(lon, lat):
        return ((lon + 180.0) * scale, y0 + (lat_top - lat) * scale)

    # graticule every 30 degrees
    for lon in range(-150, 181, 30):
        x = (lon + 180.0) * scale
        md.line([(x, y0), (x, y0 + map_h)], fill=grid_col, width=1)
    for lat in range(-60, 86, 30):
        _, y = proj(0, lat)
        md.line([(0, y), (fw, y)], fill=grid_col, width=1)

    # land: unwrap each ring, clamp latitude, draw at three shifts so
    # shapes crossing the antimeridian appear on both map edges.
    for ring in load_land():
        if all(lat < lat_bot for _, lat in ring):
            continue  # Antarctica and other far-southern land: skip
        pts = [(lon, min(max(lat, lat_bot), lat_top))
               for lon, lat in unwrap_ring(ring)]
        if len(pts) < 3:
            continue
        for shift in (-360.0, 0.0, 360.0):
            xy = [proj(lon + shift, lat) for lon, lat in pts]
            md.polygon(xy, fill=land_fill, outline=land_edge)

    page.paste(mimg, (fx, fy))
    d.rectangle([fx, fy, fx + fw, fy + fh], outline=INK, width=1)

    def proj_page(lon, lat):
        px, py = proj(lon, lat)
        return (fx + px, fy + py)

    # pins
    pin_font = font(SANS_B, 11)
    centres = {}
    for num, (lon, lat, dx, dy) in sorted(PINS.items()):
        px, py = proj_page(lon, lat)
        cx, cy = px + dx, py + dy
        centres[num] = (cx, cy)
        if not (fx + 4 <= cx <= fx + fw - 4 and fy + 4 <= cy <= fy + fh - 4):
            warn("map pin %d outside frame at (%.0f, %.0f)" % (num, cx, cy))
        if dx or dy:
            d.line([(px, py), (cx, cy)], fill=RED, width=1)
            d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=RED)
        r = 10 if num >= 10 else 9
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RED,
                  outline=(255, 255, 255), width=1)
        d.text((cx, cy + 0.5), str(num), font=pin_font,
               fill=(255, 255, 255), anchor="mm")
    # pairwise pin separation check
    nums = sorted(centres)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            ax, ay = centres[nums[i]]
            bx, by = centres[nums[j]]
            dist = math.hypot(ax - bx, ay - by)
            if dist < 19:
                warn("map pins %d and %d too close (%.1f px)"
                     % (nums[i], nums[j], dist))
    return centres


# -------------------------------------------------------------------- build

def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    vig = {n: fn() for n, fn in VIGNETTES.items()}

    # ---- masthead ----
    draw_centered(d, W / 2, 2, "THE WORLD TODAY", font(SERIF_B, 60), INK)
    draw_tracked_centered(d, W / 2, 70, "MONDAY 23 NOVEMBER 2026",
                          font(SANS_B, 16), INK, 2)
    draw_centered(d, W / 2, 91, "31 STORIES \u00b7 6 CONTINENTS \u00b7 ONE DAY",
                  font(SANS_B, 14), RED)
    draw_centered(d, W / 2, 110,
                  "Every story below happened, or was first reported, "
                  "on 23 November 2026.",
                  font(SERIF_I, 14), INK)
    d.rectangle([MARGIN, 129, W - MARGIN, 131], fill=INK)
    d.rectangle([MARGIN, 134, W - MARGIN, 134], fill=INK)

    # ---- lead story ----
    lead_y, lead_h = 141, 110
    lead_img_w = 232
    img.paste(crop_to(vig[1], lead_img_w, lead_h), (MARGIN, lead_y))
    d.rectangle([MARGIN, lead_y, MARGIN + lead_img_w, lead_y + lead_h],
                outline=INK, width=1)
    tx = MARGIN + lead_img_w + 12
    text_w_avail = W - MARGIN - tx
    draw_badge(d, tx, lead_y + 1, 20, LEAD["num"], font(SANS_B, 13))
    d.text((tx + 26, lead_y + 2), LEAD["region"], font=font(SANS_B, 12),
           fill=INK, anchor="la")
    head_f = font(SERIF_B, 30)
    if text_w(d, LEAD["headline"], head_f) > text_w_avail:
        head_f = font(SERIF_B, 27)
        if text_w(d, LEAD["headline"], head_f) > text_w_avail:
            warn("lead headline does not fit on one line")
    d.text((tx, lead_y + 24), LEAD["headline"], font=head_f, fill=INK,
           anchor="la")
    acct_f = font(SANS_R, 14)
    acct_lines = wrap(d, LEAD["account"], acct_f, text_w_avail)
    if len(acct_lines) > 2:
        warn("lead account wraps to %d lines" % len(acct_lines))
    for i, line in enumerate(acct_lines[:2]):
        d.text((tx, lead_y + 58 + i * 18), line, font=acct_f, fill=INK,
               anchor="la")
    d.text((tx, lead_y + 94), LEAD["dateline"], font=font(SANS_B, 11),
           fill=GREY, anchor="la")
    check_bottom("lead band", lead_y + lead_h, 258)

    # ---- illustrated tiles: 2 rows of 5 ----
    tile_gap = 8
    tile_w = (CW - 4 * tile_gap) // 5  # 192
    row_h = 158
    img_h = 74
    rows_y = [258, 424]
    for row_i, row_y in enumerate(rows_y):
        for col_i in range(5):
            tile = TILES[row_i * 5 + col_i]
            x = MARGIN + col_i * (tile_w + tile_gap)
            img.paste(crop_to(vig[tile["num"]], tile_w, img_h), (x, row_y))
            d.rectangle([x, row_y, x + tile_w, row_y + img_h],
                        outline=INK, width=1)
            by = row_y + img_h + 4
            draw_badge(d, x, by, 15, tile["num"], font(SANS_B, 10))
            d.text((x + 19, by + 1), tile["region"], font=font(SANS_B, 10),
                   fill=INK, anchor="la")
            # headline: shrink until it fits in 2 lines (13 is the
            # floor; a headline that fits at 13 is fine, no warning)
            head_lines = None
            for size in (15, 14, 13):
                hf = font(SERIF_B, size)
                cand = wrap(d, tile["headline"], hf, tile_w)
                if len(cand) <= 2:
                    head_lines = cand
                    break
            if head_lines is None:
                warn("tile #%d headline still >2 lines at size 13"
                     % tile["num"])
                hf = font(SERIF_B, 13)
                head_lines = wrap(d, tile["headline"], hf, tile_w)[:2]
            hy = by + 19
            for i, line in enumerate(head_lines):
                d.text((x, hy + i * 16), line, font=hf, fill=INK, anchor="la")
            # sub: 2 lines
            sub_f = font(SANS_R, 11)
            sub_lines = wrap(d, tile["sub"], sub_f, tile_w)
            if len(sub_lines) > 2:
                warn("tile #%d sub wraps to %d lines"
                     % (tile["num"], len(sub_lines)))
            sy = hy + 34
            for i, line in enumerate(sub_lines[:2]):
                d.text((x, sy + i * 13), line, font=sub_f, fill=INK,
                       anchor="la")
            check_bottom("tile #%d" % tile["num"], sy + 24, row_y + row_h)

    # ---- bottom section headers ----
    head_y = 590
    map_w = 584
    idx_x = MARGIN + map_w + 16
    idx_w = W - MARGIN - idx_x
    sec_f = font(SANS_B, 13)
    d.text((MARGIN, head_y), "WHERE IT HAPPENED", font=sec_f, fill=INK,
           anchor="la")
    d.text((idx_x, head_y), "ALSO ON THIS DAY", font=sec_f, fill=INK,
           anchor="la")
    rule_y = head_y + 17
    d.rectangle([MARGIN, rule_y, MARGIN + map_w, rule_y + 1], fill=INK)
    d.rectangle([idx_x, rule_y, W - MARGIN, rule_y + 1], fill=INK)

    # ---- world map ----
    map_y, map_h = 614, 268
    draw_map(img, d, MARGIN, map_y, map_w, map_h)

    # map footnotes + counts + numbers, under the map
    foot_f = font(SANS_R, 10)
    d.text((MARGIN, map_y + map_h + 6),
           "Pins mark the 11 illustrated stories; 16, 17, 24, 26 and 27 "
           "are offset for clarity.",
           font=foot_f, fill=GREY, anchor="la")
    d.text((MARGIN, map_y + map_h + 19),
           "Washington and New York, and Canberra, Melbourne and "
           "Wellington, sit close together.",
           font=foot_f, fill=GREY, anchor="la")
    d.text((MARGIN, map_y + map_h + 38), CONTINENT_COUNTS,
           font=font(SANS_B, 12), fill=INK, anchor="la")
    d.text((MARGIN, map_y + map_h + 57), BY_NUMBERS,
           font=font(SANS_R, 10), fill=INK, anchor="la")
    check_bottom("map column", map_y + map_h + 70, 956)

    # ---- index ----
    idx_y0 = 614
    idx_y1 = 956
    n_lines = len(INDEX)
    line_h = (idx_y1 - idx_y0) / float(n_lines)
    for i, (num, headline, region) in enumerate(INDEX):
        y = idx_y0 + i * line_h
        num_s = "%d. " % num
        reg_s = " \u00b7 " + region
        chosen = None
        for size in (11, 10):
            nf = font(SANS_B, size)
            hf = font(SANS_R, size)
            total = (text_w(d, num_s, nf) + text_w(d, headline, hf)
                     + text_w(d, reg_s, hf))
            if total <= idx_w:
                chosen = (nf, hf)
                break
        if chosen is None:
            warn("index #%d overflows at size 10" % num)
            chosen = (font(SANS_B, 10), font(SANS_R, 10))
        nf, hf = chosen
        x = idx_x
        d.text((x, y), num_s, font=nf, fill=RED, anchor="la")
        x += text_w(d, num_s, nf)
        d.text((x, y), headline, font=hf, fill=INK, anchor="la")
        x += text_w(d, headline, hf)
        d.text((x, y), reg_s, font=hf, fill=GREY, anchor="la")

    # ---- sources footer ----
    src_y = 964
    d.rectangle([MARGIN, src_y - 5, W - MARGIN, src_y - 4], fill=INK)
    src_f = font(SANS_R, 10)
    src_lines = wrap(d, SOURCES, src_f, CW)
    if len(src_lines) > 2:
        warn("sources footer wraps to %d lines" % len(src_lines))
    for i, line in enumerate(src_lines[:2]):
        d.text((MARGIN, src_y + i * 13), line, font=src_f, fill=GREY,
               anchor="la")
    check_bottom("page", src_y + len(src_lines[:2]) * 13, H - 8)

    return img


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "entry.png")
    img = build()
    img.save(out, "PNG", optimize=True)
    size = os.path.getsize(out)
    if size > 1048576:
        warn("output is %d bytes (> 1 MiB)" % size)
    with open(out, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    print("wrote %s (%d bytes, sha256 %s)" % (out, size, digest[:16]))
    if WARNINGS:
        print("WARNINGS: %d" % len(WARNINGS))
    else:
        print("no warnings")
    return 0


if __name__ == "__main__":
    sys.exit(main())

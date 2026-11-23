# Test report — news-image-20261123 (fix round, 23 Nov 2026 ~08:10 UTC)

Entry: `entry.png`, 1024×1024, 238,621 bytes,
sha256 `afe84a5db0224c966875e3a4c0a2209922e968f168ac9846067d60f02f165d1a`.

This supersedes the rebuild report below (sha256 `a9f14be9…58ef0`,
239,793 bytes). The fix round applied audit pass 2's three WEAK fixes
(#1 Taiex morning-trade qualifier, #24 launch reframe, #30 sourcing
firm-up) plus the optional #12 "At least" index change and all of the
audit's notes-only corrections. Page-text changes vs the audited build:
lead account ("Taiwan falls 0.93% in morning trade"), tile #24 headline
("Fit to Lead study launches in Canberra"), index #12 ("At least 46
killed…"). Nothing else on the page changed.

## Fix-round re-verification

```
$ python3 compose.py
wrote .../entry.png (238621 bytes, sha256 afe84a5db0224c96)
no warnings
```

- Build: zero warnings; 238,621 bytes ≤ 1 MiB; 1024×1024 RGB.
- Determinism: `compose.py /tmp/fix-det1.png` and `/tmp/fix-det2.png`
  both sha256 `afe84a5db0224c96…` — byte-identical to each other and to
  `entry.png`.
- Entrypoint: `python3 main.py` twice with `MAKEFUN_OUTPUT_DIR` set to
  two different temp dirs: exit 0 both times, output byte-identical
  (sha256 `afe84a5db0224c96…`) both times.
- Grader simulation: repo copied to `/tmp/fix-grader-repo` (no
  `__pycache__`/`candidates/`), made read-only (`chmod -R a+rX,a-w`),
  run as uid 65534 with a separate writable output dir under
  `timeout 10`: exit 0 in 0.09 s, output byte-identical
  (sha256 `afe84a5db0224c96…`).
- Legibility (rebuilt page read at full size + crops): lead account
  reads "…Taiwan falls 0.93% in morning trade. Seoul readies about 10
  trillion won in stabilisation funds." on two lines, no clipping;
  tile #24 headline "Fit to Lead study launches in Canberra" wraps to
  two lines at size 15 (no shrink needed), sub unchanged on two lines;
  index #12 "At least 46 killed in Niger State attacks and reprisals ·
  AFRICA" fits one line at size 11; full page re-read — masthead, all
  10 tiles, map pins, counts, BY THE NUMBERS and sources footer all
  legible, no clipping or overlap.
- Programmatic check re-run: story numbers 1–31 each exactly once
  (lead + 10 tiles + 20 index lines); map pins keyed 1:1 to the 11
  illustrated stories.
- No-secrets grep re-run over `*.py`/`*.md`: no matches (only the
  test-report's own description of the grep pattern).

# Test report — news-image-20261123 (rebuild, 23 Nov 2026 ~07:00 UTC)

Entry: `entry.png`, 1024×1024, 239,793 bytes,
sha256 `a9f14be9759353372bdc0bf3c8f130eb726d0c29b54e06cb028f68b8e1c58ef0`.

## a. Build — zero warnings, size and dimensions

```
$ python3 compose.py
wrote .../entry.png (239793 bytes, sha256 a9f14be975935337)
no warnings
```

- 239,793 bytes ≤ 1 MiB (1,048,576). Dimensions 1024×1024, RGB.
- The build checks and warns on: lead headline/account overflow, tile
  headline >2 lines at the 13 px shrink floor, tile sub >2 lines, tile
  overflow past its row, map pin outside the frame, map pins <19 px
  apart, map-column overflow, index line overflow at 10 px, sources
  footer >2 lines, page overflow, output >1 MiB. None fired.

## b. Determinism

`python3 compose.py /tmp/det1.png` and `python3 compose.py /tmp/det2.png`
both produced sha256 `a9f14be975935337…` — byte-identical to each other
and to `entry.png`.

## c. Entrypoint

`python3 main.py` run twice with `MAKEFUN_OUTPUT_DIR` set to two
different temp dirs: exit 0 both times, output `entry.png` byte-identical
(sha256 `a9f14be975935337…`) to the repo's `entry.png` both times.

## d. Grader simulation (unprivileged user, read-only source, 10 s limit)

- Copied the repo to `/tmp/grader-repo`, removed `__pycache__` and
  `candidates/`, made it read-only (`chmod -R a+rX,a-w`).
- Ran as uid 65534 (nobody) with a separate writable output dir:
  `timeout 10 su nobody -s /bin/sh -c 'MAKEFUN_OUTPUT_DIR=/tmp/grader-out
  python3 /tmp/grader-repo/main.py'` — exit 0, well inside 10 s.
- Output byte-identical to the repo's `entry.png`
  (sha256 `a9f14be975935337…`).
- Note: the first attempt failed with "Permission denied" because the
  `cp -r` copy was owned root:root with mode 750, so uid 65534 could not
  traverse it. That was an artefact of the test copy, not of the entry:
  after `chmod -R a+rX` (world-readable, still read-only — the realistic
  read-only-mount simulation) the run passed. `main.py` needs no network
  and no node; it is pure stdlib Python.

## e. Legibility (frames read at full size and at 300 px wide)

Frames extracted and read: full page at 300×300; masthead+lead (full
size, 0–260); tiles row 1 (255–425); tiles row 2 (420–592); bottom band
(585–1024).

- 300 px view: the page reads as a coherent newspaper front page;
  masthead, lead headline, tile grid, map and index are all recognisable.
- Masthead: "THE WORLD TODAY", "MONDAY 23 NOVEMBER 2026",
  "31 STORIES · 6 CONTINENTS · ONE DAY", and the italic rule line are
  all legible and centred, nothing clipped.
- Lead: headline "AI sell-off deepens as Asia slides" on one line; the
  two-line account and "SEOUL · MONDAY" dateline legible; vignette
  (falling candlesticks, red plunge line, green bounce) clear.
- All 10 tile headlines fit on two lines, all 10 subs on two lines, no
  clipping or overlap. Tile #24's headline renders at the 13 px shrink
  floor (the longest headline) and remains legible; the shrink-floor
  warning from the 20261122 code was deliberately removed — a headline
  that fits at 13 px is fine, only a headline that still overflows at
  13 px warns.
- All 11 vignettes read clearly at tile size; all are text-free PIL
  vector art (no words or letters inside any picture).
- Map: all 11 pins visible and separated; leader lines visible on the
  five offset pins (16, 17, 24, 26, 27); no pin touches the frame edge.
  Wellington's pin sits just inside the right edge after its −16 px
  offset (without it the pin centre would be at x≈575 of 584 and the
  10 px radius would cross the frame).
- Index: all 20 lines on one line each, number + headline + region,
  legible, no overflow.
- Counts line, BY THE NUMBERS line and the two-line sources footer are
  legible; nothing overlaps; the page ends with whitespace to spare
  (sources end at y≈990 of 1024).

## f. No secrets in the repo

`grep -rniE "api[_-]?key|secret|password|passwd|token|bearer|
private[_-]?key|aws_|sk-|BEGIN .* PRIVATE"` over `*.py` and `*.md`:
no matches.

## g. Figure cross-check (page vs research-notes.md)

Every figure printed on the page was checked against
`research-notes.md`; all match exactly. Checked:

- Lead: KOSPI −5.41% intraday to 4,606.44; five-minute halt to program
  selling; Taiwan −0.93% in morning trade; about 10 trillion won
  stabilisation funds.
- Tiles: $2 billion Nepal package (sought); Dymer 9 of 12 dead; Opentil
  32nd-minute goal, 1–0; 330 votes, 258 House seats, most since 1992;
  71% / 97%; 429 Brussels flights; $450M, nine years, $50M a year;
  35–10, three first-half TD passes, 9–1; 720/9, 43 overs; aged 83,
  5:30am.
- Index: 37.3%; R3.1m; 27–24; 100–150%; Murray 45, Jokic 202nd; M5.4;
  M4.2; 2.2%; aged 60; 13 years.
- Counts: Asia 7 · Europe 4 · N. America 6 · S. America 2 · Africa 4 ·
  Oceania 8 = 31. Programmatic check: story numbers 1–31 all present
  exactly once (lead + 10 tiles + 20 index lines); pins keyed 1:1 to the
  11 illustrated stories.
- BY THE NUMBERS: KOSPI −5.41% intraday · $450M Skubal deal · 258 House
  seats · 71% of MPs.
- No figure was invented, estimated or rounded beyond the source's
  wording. The KOSPI official close is deliberately NOT printed (see
  research-notes.md "Refresh outcomes": snapshots conflicted).

## Audit-relevant notes

- Pending outcomes framed as scheduled (never claimed): Nepal–Modi joint
  statement / $2B package (ask, not agreed); Burnham Commons statement
  (Monday afternoon GMT); Joburg speaker election (sitting only);
  Brazil fiscal vote (Monday 18:00 Brasília); Anthropic options first
  trades (US open 14:30 UTC — listing confirmed, trades not claimed).
- Cut at composition: Iowa lead-azide detonation and US West Coast king
  tides (scheduled/warnings, not completed events). Verified pool was 33;
  final page has 31.
- Story #30 (Julie Carter) was verified-but-thin at rebuild (Wikipedia +
  NZ aggregator; underlying obituary not directly retrieved) — kept in
  the index only, flagged in research-notes.md. Fix round: a second
  independent NZ source was retrieved (Stuff, 23 Nov, "dies, aged 60");
  the NZ Herald obituary itself remains directly unretrieved after a
  genuine attempt — see research-notes.md #30.
- Index headlines #19, #21, #28 are shortened to fit one line; full
  headlines are in research-notes.md. Tile #20's headline drops "Purdy
  stars as" (Purdy detail is in the tile sub).
- The v1 cricket framing ("India close in on win") was replaced by the
  confirmed DRAW; the vignette's stale "INDIA CLOSE IN" title was
  removed along with all vignette text.
- All 11 vignettes are text-free (the 20261122 proven pattern); the v1
  vignettes carried text tags, which were stripped in this rebuild.

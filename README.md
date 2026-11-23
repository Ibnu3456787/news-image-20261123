# THE WORLD TODAY — Monday 23 November 2026

[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Ibnu3456787/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Ibnu3456787/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

A one-image front page summing up the world's news of Monday 23 November
2026, built for the make.fun `news-image-20261123` bounty.

## The image

`entry.png` (1024×1024, PNG, 238,621 bytes) is a newspaper front page:

- **Masthead** naming the day: Monday 23 November 2026, "31 stories ·
  6 continents · one day".
- **Lead story:** the AI sell-off deepening as Asia slides — Seoul's KOSPI
  down 5.41% intraday to 4,606.44, triggering a five-minute halt to
  program selling; Taiwan down 0.93% in morning trade after a 17% week;
  Seoul readying
  about 10 trillion won in stabilisation funds.
- **Ten illustrated tiles:** Nepal's PM in Delhi; the Kyiv-region toll
  rising to 12; Ghana winning the Amputee World Cup; Democrats clinching
  258 House seats; the Fit to Lead study on Australian MPs' mental
  health; Belgium's nationwide strike; Skubal's record $450M Mets deal;
  the 49ers routing the Vikings 35–10 in Mexico City; New Zealand batting
  out a draw after India's record 720/9; Molly Meldrum's death at 83.
- **A world map** with a numbered pin for each of the 11 illustrated
  stories, and an index ("ALSO ON THIS DAY") with the other 20 stories,
  one line each.
- **Continent counts** (Asia 7 · Europe 4 · N. America 6 · S. America 2 ·
  Africa 4 · Oceania 8), a **BY THE NUMBERS** line and a **sources**
  footer (Reuters, AP, AFP, BBC, IANS, ABC, AAP, ESPN, NBC Sports,
  Cricinfo, USGS, AFAD, Stats NZ, RNZ, Korea JoongAng Daily, Seeking
  Alpha, Sowetan, TimesLIVE, Ghana FA, Cboe, Anadolu, Better Politics
  Foundation).

Every story happened, or was first reported, on Monday 23 November 2026
in some time zone. The research behind each story — sources, figures,
timezone edges and the pending outcomes that were framed as scheduled —
is recorded in `research-notes.md`.

## How it is built

- `vignettes.py` — draws the eleven story illustrations with PIL
  primitives only (own text-free vector-style drawings; no external
  images, no AI-generated images, no copied photos). Each function takes
  no arguments and returns a 480×300 image; `compose.py` centre-crops
  them to the tile aspect ratios.
- `compose.py` — lays out the front page: masthead, lead band, tiles,
  equirectangular world map from `ne_110m_land.geojson` (Natural Earth
  1:110m land data), index, counts, numbers line, sources. Prints a
  warning for any clipped or overflowing text, tile overflow, map pin
  outside the frame, pin collision, or page overflow; a clean build
  prints "no warnings". Layout follows the proven news-image-20261122
  geometry (lead + 10 tiles + map/index bottom band).
- `main.py` — the graded entry point: validates `entry.png` (PNG
  signature, ≤1 MiB, ≤1024×1024) and copies it to `$MAKEFUN_OUTPUT_DIR`
  (default `/output`) as `entry.png`, verifying the copy by sha256.
  Standard library only, no network, deterministic.

Rebuild: `python3 vignettes.py && python3 compose.py` (needs Pillow and
the Liberation fonts). Two builds are byte-identical.

Verification results are in `test-report.md`.

## License

MIT — see `LICENSE`.

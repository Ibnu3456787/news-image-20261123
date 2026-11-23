# Audit pass 3 (cold re-audit) — news-image-20261123
## "THE WORLD TODAY — MONDAY 23 NOVEMBER 2026"

**Auditor:** re-audit agent (pass 3), session `94d18198-a74b-4c36-80e2-59ee172f934e`.
**Audit time:** Mon 23 Nov 2026 ~08:00–08:45 UTC (15:00–15:45 WIB).
**Entry audited:** `entry.png`, sha256
`afe84a5db0224c966875e3a4c0a2209922e968f168ac9846067d60f02f165d1a`,
238,621 bytes — hash verified by the auditor, matches the task brief.
**Method:** every story re-verified from scratch with fresh web searches
(`browser.search`, 31 searches across all 31 stories — no reliance on
pass-2 or fix-round claims without an independent check). The image was
read at full size plus 2× zoomed crops (lead band, both tile rows,
bottom band with map + index). `compose.py`, `research-notes.md`,
`README.md`, `vignettes.py`, `audit-pass2.md` and `fix-round.md` were
read/grepped. Story-number coverage, pin mapping and continent counts
were re-derived programmatically from `compose.py`.

## Tallies

**31 PASS / 0 WEAK / 0 FAIL** (31 stories)

All three pass-2 WEAK items are resolved: #1 (Taiex qualifier on the
page, no close figure anywhere), #24 (tile reframed to the Monday
launch), #30 (second independent NZ source retrieved and cited, story
still index-only). No FAILs: no story has a wrong first date, a wrong
printed figure, a claimed outcome that did not happen, or a
page-vs-notes mismatch.

## Per-story verdicts

| # | Headline (as printed) | Verdict | Reason (one line) | Sources checked (fresh, this pass) |
|---|---|---|---|---|
| 1 | AI sell-off deepens as Asia slides (LEAD) | PASS | KOSPI −5.41% to 4,606.44, 5-min halt, ₩10T fund all confirmed; Taiex −0.93% now qualified "in morning trade"; official Taiex close STILL unconfirmed (Finnhub close blank, LiveWorldMarket moving intraday) — correctly not printed. | Seeking Alpha via TradingView, publ. 2026-11-23T03:45:50Z (−5.41% to 4,606.44, ~21.4% below 2 Nov close, ₩10T fund); Korea JoongAng Daily 23 Nov (sidecar 11:33 a.m., 5 min, 2nd straight session); BigGo Finance 23 Nov (1,213-pt swing, reclaimed 36,000); Finnhub TAIEX ETF pages (23 Nov close field blank as of 05:25 UTC); LiveWorldMarket (+2.69% at 37,001.3, never labelled a close) |
| 2 | Nepal's PM holds talks with Modi in Delhi | PASS | Talks Monday confirmed; $2B is the ASK — page says "seeks"; joint vision document due. | janpathnewsnetwork 23 Nov ($1B loans + $500M grants + $500M reconstruction per Indian Express/Kathmandu Post; India "reportedly considering" ~$1.5B); particle.news (talks 23 Nov, joint press conference); obnews.co 23 Nov (Saryu-Kamala Express) |
| 3 | China–Singapore council meets in Singapore | PASS | 22nd JCBC met Monday, co-chaired Ding/Gan; 29 deals concluded (page prints no number). | PMO Singapore (Gan opening remarks, 22nd JCBC); redhot.sg 23 Nov (29 deals concluded Nov 23); nglobenews 22 Nov (>20 deliverables expected) |
| 4 | Seoul silent on spy chief replacement reports | PASS | Presidential office "cannot confirm" on Monday; Kang Kum-sil front-runner; 1 yr 5 mo. | Seoul Economic Daily, publ. 2026.11.23 (spokesperson Kim Sung-wan, Chunchugwan briefing) |
| 5 | Lee's approval rating rises to 37.3% | PASS | 37.3% (+0.9pp), 59.9% negative, n=2,514, 16–20 Nov, released Monday; ₩1 trillion export figure confirmed (Aju Press). | Korea JoongAng Daily publ. 2026-11-23T02:55:56Z (Yonhap); Aju Press 23 Nov ("1 trillion won in exports") |
| 6 | Saudi hand seen behind failed COP31 deal | PASS | Reuters investigation datelined ANTALYA Nov 23; O'Brien "hijacked" quote; first no-deal COP since 2009. | Reuters via dailyfoxnews.com / wdsm710.com / dukecountry.fm, ANTALYA Nov 23 |
| 7 | Three killed in Gaza as truce frays | PASS | MEMO/Anadolu 23 Nov 02:52: 3 killed, 4 injured (incl. child); 1,675/6,095 since ceasefire. Distinct from the 21 Nov Tel al-Hawa strike. | Middle East Monitor / Anadolu via 7788news.com, publ. 23 Nov 2026 02:52 |
| 8 | Kyiv toll rises to 12 as rescuers dig on | PASS | Monday figures re-confirmed: 12 across region (Dymer 9, Vyshneve 2, Bila Tserkva 1); Sunday toll was 5. News Central TV's 14/Dymer 10 remains a single uncorroborated outlet; no wire has confirmed a higher toll. | AFP via europesays.com / redhot.sg, 23 Nov (12 / Dymer 9); DPA via dailyfoxnews.com, Mon 23 Nov (Dymer 9; late Sunday 5); metapress.net 23 Nov; world-today-journal.com 23 Nov |
| 9 | Belgium grinds to a halt in nationwide strike | PASS | Strike is Monday; 429 flights / ~59,500 pax / 213 out + 216 in; ATC 07:00–21:00; Charleroi all cancelled; SNCB ran normally (Temmerman quote confirmed). | airwaysmag.com; qncnews.com 23 Nov; nomadlawyer.org 23 Nov; europesays.com (SNCB "No strike notice was submitted, so our service will run as normal on Monday"); striketracker.app 23 Nov |
| 10 | M4.2 quake in the Aegean off Bodrum | PASS | AFAD M4.2 (Mw), 66.74 km off Bodrum, 23 Nov 02:42:48 local (23:42 UTC Sun) — Monday in Türkiye; M2.4 aftershock 23:52 UTC confirmed. | AFAD via turkishnewsworld.com 2026-11-23; USGS via quakewatch.beer (M4.2, 33 km WSW Pánormos, 23:42 UTC); volcanoesandearthquakes.com list (updated 23 Nov 04:00 UTC, M2.4 23:52 UTC near Astypalaia) |
| 11 | Burnham asks MPs to back his EU deal | PASS | Commons statement scheduled Monday afternoon GMT; all sources future tense; no outcome claimed on page. £17bn/0.5% claim + Badenoch dispute + 18–31 YES ages + £5.1bn farm-trade figure all confirmed. | madeinshoreditch.co.uk 23/11/2026 (citing BBC); BBC via web-ecs.test.bbcx-internal.com; reformuk.scot (YES "aged 18 to 31", 100,000/yr, up to 3 years); magnabureau.space (£5.1bn farm-trade arrangement) |
| 12 | At least 46 killed in Niger State attacks and reprisals | PASS | AFP security report: 11 (Luman Ba'are, Sat) + 35 (Wawa reprisals) = 46; Gada Oli toll "more than Wawa", so "At least" is correct — 46 is a floor. First published Sun 22 Nov 22:16 UTC = Monday UTC+2 eastward. EDGE, honestly flagged. | AFP via thenews.pk 23 Nov; AFP via beninwebtv.bj 23 Nov; ThisDay 2026-11-22T12:30Z |
| 13 | Ghana win Amputee World Cup | PASS | 1–0 vs Morocco, Opentil 32nd min (GFA official account); first title; Mubarik Golden Boot 7 goals; Sports Ministry statement Monday 23 Nov. Final played Sun evening Mexico, first Ghana reports Monday. | ghanafa.org 23 Nov; ghanasoccernet.com 23 Nov (Ministry statement Mon 23 Nov); Metro TV Online 23 Nov; ghsportsnews.com 23 Nov |
| 14 | Ex-councillors sue ActionSA for R3.1m | PASS | Sowetan 23 Nov: six ex-councillors, claim >R3.1m; all six names + individual amounts match (sum R3,145,284); summons filed 13 Nov, first reported 23 Nov. | Sowetan, sowetan.co.za/news/2026-11-23-... |
| 15 | Hung Joburg council sits for first time | PASS | First sitting Monday 23 Nov (swear in + elect speaker); DA 91 / ANC 63 / ActionSA 43 of 270, majority 136; no outcome claimed. (BusinessDay 23 Nov says Joburg "convenes Thursday" — conflicts with TimesLIVE/politicsweb/FM/africanbulletin24; majority supports Monday; conflict flagged in notes.) | TimesLIVE via community.southafricafacts.co.za 22 Nov; africanbulletin24.com (upd. 22 Nov, "meets on Monday, 23 November"); politicsweb.co.za diary 22 Nov; Financial Mail 22 Nov |
| 16 | Democrats clinch 258 House seats | PASS | AP call Sunday 6:04 p.m. EST (= 23:04 UTC Sun, Monday UTC+1 eastward); Hubbard beat Foxx by 330 votes after recount; 258 seats, most since 1992 (also 258); net gain 44. | AP via dailyfoxnews.com; foxrochester.com (TNND/AP); BBC via web-ecs.live.bbcx-internal.com (258, "at least 173" GOP, 4 races uncalled); thursdayreview.com |
| 17 | Skubal signs record $450M Mets deal | PASS | 9 years, $450M, $50M AAV — richest pitcher deal ever (tops Yamamoto $325M); $45M signing bonus, full no-trade, no opt-outs; lockout 1 Dec confirmed (NBC). Reported Sun evening US = Monday Asia-Pacific. | AP via lapost.com / statmuse.com (AP source, Sunday); ESPN/Jeff Passan 22 Nov; NBC Sports (lockout "begins on Dec. 1"); SI; theScore (upd. 2026-11-23T00:36:45Z) |
| 18 | Jets end five-game skid, 27–24 over Chargers | PASS | 27–24 at SoFi; Geno Smith 17/21, 176 yds, 3 TD, 0 INT; Shepard 2 TD; scored on first five drives; game ended after midnight UTC Monday. | AP via thescore.com; Field Level Media 23 Nov; sportradar (Mon 23 Nov 04:05 WIB); newyorkjets.com |
| 19 | Anthropic options debut; volatility seen at 100–150% | PASS | Cboe preview (20 Nov): options begin trading Mon 23 Nov, earliest date under Rule 4.3; IV 100–150% per Cboe-floor market makers (CNBC 20 Nov). No first trades claimed (US open after build). | Cboe "Anthropic Options Preview", 20 Nov 2026; CNBC 20 Nov via aiagentupdate.com 22 Nov; Reuters 18 Nov via aistockwire.com; tradersunion.com 23 Nov (Tradr ANTT/ANTZ) |
| 20 | 49ers rout Vikings 35–10 in Mexico City | PASS | 35–10, Purdy 21/26, 255 yds, 3 first-half TDs; 49ers 9–1; McCaffrey 6-yard TD confirmed (AP); game ended ~05:00 UTC Monday. | NBC Sports 23 Nov; AP via thescore.com (MEXICO CITY); NBC Sports Bay Area 23 Nov ("McCaffrey's 6-yard fourth-quarter touchdown run"); vikings.com 22 Nov 10:42 PM |
| 21 | Murray's 45, Jokic's 202nd triple-double win OT thriller | PASS | Nuggets 151–145 OT; Murray season-high 45 (8 in OT per AP); Jokic 202nd triple-double (37/18/11), 7 shy of Westbrook's 209; final publ. ~02:52 UTC Monday. | AP via thescore.com / TSN / ESPN ("scored eight of his season-high 45 points in overtime"); denversports.com (combined 82, 2nd-most ever for the pair); legionreport.com |
| 22 | M5.4 quake shakes Peru's Andes as toll rises | PASS | M5.4, 9 km N Carhuamayo, 21:35:31 UTC Sun (Monday Asia-Pacific), 117.4 km deep; Indeci Reporte Complementario N.º 16277 confirmed (1 dead, 15 injured, 152 homes uninhabitable, 853 displaced + 628 affected, 5 regions); 4 aftershocks within 63 km (quakemate/USGS). EDGE, honestly flagged. | USGS via terremoto.developers.do / quakenear.me (21:35:31 UTC); watchers.news 23 Nov (COEN-INDECI Reporte 16277, 22 Nov 08:20 local, Report No. 10); Infobae via allatra.media (publ. Nov 22 8:35 PM EST); quakemate.app |
| 23 | Brazil's lower house votes on Lula's fiscal package | PASS | Extraordinary session Monday 23 Nov 18:00 Brasília; PLP 299/2026, Senate approved 18 Nov (69–2); 257 votes needed; rapporteur kept Senate text. Vote not yet held at build — no outcome claimed. (Cut-size conflict 10% vs 20% persists; page prints neither.) | contrapontobrasil.com.br 23 Nov; LIDE clipping 20 Nov (session Mon 18:00, 257 votes); particle.news; macroherald.com; todayinbrazil.com |
| 24 | Fit to Lead study launches in Canberra | PASS | Launch is the Monday event: Parliament House, Canberra, Mon 15:30–17:30 AEDT, keynote Alastair Campbell (Better Politics Foundation). Tile headline now states the launch; 71% / 97% figures confirmed (BPF data page; ABC). | Better Politics Foundation (report launching 23 Nov 2026; launch Mon 15:30–17:30, Parliament House; "71% of parliamentarians"); ABC News via daily8.com (71% MPs, 61% councillors, 97% cite online abuse); zot.news publ. 2026-11-22T20:40:22Z |
| 25 | COP31 failure a sign of 'difficult times', says Albanese | PASS | Albanese spoke Monday: "difficult geopolitical times", defended Bowen; Tehan "resign immediately" / "catastrophic diplomatic disaster"; Bowen "very disappointing". Collapse itself is Sunday — story is the Monday reaction. | Guardian via dailyfoxnews.com, publ. 2026-11-23T04:54:22Z; AFP (Sydney, Nov 23) via NAMPA; darwindaily.com 23 Nov |
| 26 | New Zealand bat out a draw after India's record 720/9 | PASS | MATCH DRAWN: NZ 368 & 239/5 (120 ov) drew with India 720/9 dec; Mitchell 49* (186 balls) + Phillips 26* (126 balls) batted 43 overs together; draw agreed before final hour. No "close in on win" language survives on the image or in code (grep-verified; only meta-mentions in research-notes.md/test-report.md describing the replaced framing). | ESPNcricinfo match report, Nov 23; AP via devdiscourse.com (Wellington, Nov 23); IANS tea report (Wellington, Nov 23, 206/5 at tea, 146 behind); NDTV live, sent Mon 23 Nov 2026 04:43 UTC |
| 27 | Molly Meldrum dies aged 83 | PASS | Died 5:30am Monday 23 Nov at Epworth Hospital, Richmond, Melbourne, aged 83; state funeral announced (Victorian Government). | AAP 23 Nov; hellocare.com.au (5.30am Mon 23 Nov, Epworth Richmond); ARIA 23 Nov 2026; beat.com.au publ. 2026-11-23T03:06:45Z; Wikipedia (died 23 Nov 2026, aged 83) |
| 28 | NZ retail sales surge 2.2%, best in nearly five years | PASS | Stats NZ: volumes +2.2% qoq (NZ$561m), strongest since Q4 2021, vs 0.5% expected; Q2 −0.5%; ex-autos +1.4%; values +2.4% to NZ$33bn; all 16 regions up. YoY resolved: total +3.5% (Econoday), core +4.7% (Westpac Ranchhod quote re-verified). Released 10:45am NZDT Monday (21:45 UTC Sun). | Stats NZ via ActionForex 23 Nov; Inside Retail NZ 23 Nov 2026; Econoday (YoY volumes 3.5%); europesays.com 23 Nov (Westpac: "Core spending… is 4.7% higher than this time last year"); Xinhua 23 Nov |
| 29 | Northland's first wind farm opens | PASS | Mercury cut the ribbon Monday: NZ$287m Kaiwaikawe, 12 × 206 m Vestas V162, 77 MW, 221 GWh/yr, ~27,000 homes; Pāmu Ōmāmari farm, Te Roroa; 12 km NW of Dargaville. | RNZ, 23 Nov 2026 ("Mercury cuts ribbon on Northland's $287m Kaiwaikawe Wind Farm", cited by Wikipedia); Mercury NZ; Pāmu; Fletcher Construction |
| 30 | Former Silver Ferns captain Julie Carter dies aged 60 | PASS | Death date + age CONFIRMED and now multi-sourced: Wikipedia (27 Nov 1965 – 23 Nov 2026, citing NZ Herald obituary, 23 Nov 2026); Netball WBOP (DOB 27/11/1965, 50 caps, 16th captain, 10 wins from 11); Stuff headline "'Tough and uncompromising': Former Silver Ferns captain Julie Carter dies, aged 60" independently surfaced in this pass via the collector.com.tr aggregator. Stays index-only, NOT a tile. | Wikipedia "Julie Carter" (ref 1: NZ Herald, 23 Nov 2026); Netball Waikato BOP player profile; Stuff via collector.com.tr (headline retrieved this pass); research-notes.md #30 cites Stuff (stuff.co.nz, 23 Nov, crawled 02:29 UTC) |
| 31 | Albanese runs biggest, best-paid PM's office in 13 years | PASS | Centre for Public Integrity report released Monday: 59 staff, 3/4 senior (61% at start, <half under Abbott); senior salaries $156,510–$317,152; max bill $12,155,410; 51 at 2022 election, peaked 65 pre-2025 election; Albanese quoted at Monday press conference. | AAP publ. 2026-11-22T23:14:10Z (= 10:14am AEDT Mon); thebullpost.press (report detail, $12,155,410 max bill); pm.gov.au press conference transcript (Parliament House, Canberra, Monday) |

## Fix-round confirmation

| Fix-round item | Status | Evidence |
|---|---|---|
| **1. #1 lead Taiex qualified** | **FIXED** | Lead account on the page (verified visually in the 2× lead crop and in `compose.py` line 82–84) reads "Taiwan falls 0.93% in morning trade." The qualifier is on the page. No close figure appears anywhere on the page or in `compose.py` (grep: the only "close" hits are "close together" map footnote, pin-collision warning text, and a cricket comment in `vignettes.py`). Fresh check confirms the official Taiex close is STILL unconfirmed: Finnhub TAIEX ETF pages show the 23 Nov close field blank as of 05:25 UTC, and LiveWorldMarket's +2.69% at 37,001.3 is a moving intraday quote, never labelled a close. The decision not to print a close remains correct. |
| **2. #24 Fit to Lead reframed to the launch** | **FIXED** | Tile headline on the page (verified visually in the 2× tiles-row-1 crop and in `compose.py`) is "Fit to Lead study launches in Canberra" — the Monday event (Parliament House, 15:30–17:30 AEDT, confirmed on the Better Politics Foundation page). Sub keeps the verified figures: "71% of parliamentarians affected; 97% of them blame online abuse." Headline wraps to 2 lines and fits with no clipping or overflow; sub fits on 2 lines. |
| **3. #30 Julie Carter second NZ source** | **FIXED** | The Stuff citation exists in `research-notes.md` #30 (lines 1001–1020): "'Tough and uncompromising': Former Silver Ferns captain Julie Carter dies, aged 60" (stuff.co.nz, 23 Nov 2026, crawled 02:29 UTC; aggregator mirror collector.com.tr). This pass independently surfaced the same Stuff headline via the collector.com.tr aggregator in a fresh search, and Wikipedia's reference 1 now shows the full NZ Herald citation ("23 November 2026"). Death date (23 Nov 2026) and age (60) are corroborated by Stuff + Wikipedia (citing NZ Herald) + Netball WBOP (DOB 27/11/1965). The story stays index-only: #30 is in `INDEX` in `compose.py` and NOT in `TILES` (verified programmatically). |
| **4. Notes-only corrections** | **FIXED** (6 of 6 spot-checked) | Spot-checked against fresh sources: #5 "exports ₩1 trillion" — Aju Press, "1 trillion won in exports" ✓; #9 "SNCB ran normally" — SNCB spokesperson Temmerman via The Brussels Times / europesays.com, "No strike notice was submitted, so our service will run as normal on Monday" ✓; #11 ages 18–31 — reformuk.scot, "aged 18 to 31"; £5.1bn farm-trade figure — magnabureau.space ✓; #17 lockout 1 Dec — NBC Sports, "potential lockout begins on Dec. 1" ✓; #28 YoY resolved total +3.5% / core +4.7% — Econoday (3.5%) + Westpac's Ranchhod via europesays.com ("Core spending… is 4.7% higher than this time last year") ✓; #22 Indeci report 16277 — Watchers, "Reporte Complementario N.º 16277, Report No. 10" ✓. All six corrections are present in `research-notes.md` (grep-verified) and match their sources. |
| **5. #12 headline "At least 46 killed…"** | **FIXED** | Index line 12 on the page (verified visually in the 2× bottom crop and in `compose.py`) reads "12. At least 46 killed in Niger State attacks and reprisals · AFRICA" and fits on one line with clear margin to the right edge. "At least" is factually correct: the AFP security report gives 11 + 35 = 46 consolidated, while the Gada Oli toll is unconsolidated but "more than the Wawa killing", so 46 is a floor. |
| **6. #8 Kyiv toll recheck (no change expected)** | **NO CHANGE — CORRECT** | Rechecked ~08:10 UTC: AFP/DPA wire consensus is STILL 12 / Dymer 9 (AFP via europesays.com and redhot.sg; DPA via dailyfoxnews.com; metapress.net; world-today-journal.com — all crawled within the last 1–2 hours). News Central TV alone (publ. 2026-11-23T04:54:33Z) reports 14 / Dymer 10 — still uncorroborated by any wire source. One newly surfaced outlet (ghananews24) reports a LOWER toll (7) from earlier Sunday figures, not a higher one. No FAIL trigger: the page stays at 12/9. |

## Image / technical findings

- **File integrity:** sha256 matches the brief
  (`afe84a5d…65d1a`), 238,621 bytes (≤ 1 MiB), 1024×1024 PNG, RGB.
  No rebuild was performed by this auditor.
- **Legibility (full size + 2× zoomed crops):** masthead, lead
  headline + 2-line account + dateline, all 10 tile headlines/subs,
  all 20 index lines, map footnotes, counts line, BY THE NUMBERS and
  the 2-line sources footer are all legible with no clipping, overlap
  or overflow observed. Tile 24's new headline wraps to 2 lines and
  fits; index #12 fits on one line.
- **Map pins (11):** all present and numbered 1, 2, 8, 9, 13, 16, 17,
  20, 24, 26, 27, matching the 11 illustrated stories
  (programmatically verified: `PINS` keys == lead + tiles). Offsets
  with leader lines visible for 16/17 (Washington/New York) and
  24/26/27 (Canberra/Melbourne/Wellington); the footnote naming
  exactly those five pins is accurate. Pin positions match their
  coordinates (Seoul, New Delhi, Dymer, Brussels, Accra, Washington,
  New York, Mexico City, Canberra, Wellington, Melbourne). Pin 13
  (Accra) sits on the Gulf of Guinea coast at this scale — within
  tolerance, no fix needed.
- **Continent counts — recounted from the story list by the
  auditor:** Asia 7 (1, 2, 3, 4, 5, 6, 7) · Europe 4 (8, 9, 10, 11) ·
  N. America 6 (16, 17, 18, 19, 20, 21) · S. America 2 (22, 23) ·
  Africa 4 (12, 13, 14, 15) · Oceania 8 (24, 25, 26, 27, 28, 29, 30,
  31) = 31. The page line matches exactly (also verified
  programmatically from `compose.py` region tags).
- **Story coverage:** numbers 1–31 each appear exactly once across
  lead + tiles + index (programmatically verified: 31 unique, no
  missing, no duplicates).
- **Page-vs-notes-vs-compose.py consistency:** every headline, sub,
  figure, count and pin on the image matches research-notes.md and
  compose.py. Documented shortenings are as stated in the notes
  (#19, #21, #28 index lines; #20 tile headline). BY THE NUMBERS
  (KOSPI −5.41% intraday · $450M Skubal deal · 258 House seats ·
  71% of MPs) matches. All 22 outlets in the sources footer
  correspond to sources actually cited in the notes.
- **#26 language check:** no "close in on win" / "INDIA CLOSE IN"
  language survives on the image, in README.md, or in vignettes.py /
  compose.py / main.py (grep-verified). The only occurrences are
  meta-mentions in research-notes.md:485 and test-report.md:181–182
  describing the replaced v1 framing — correct and intentional.
- **Scheduled/pending outcomes:** #2 ($2B as ASK — page says
  "seeks"), #11 (statement scheduled Monday afternoon — no outcome
  claimed), #15 (sitting taking place — no speaker result claimed),
  #19 (debut, no first trades claimed), #23 (vote scheduled 18:00
  Brasília — no outcome claimed) are all framed honestly.
  Present-tense headlines for same-day scheduled events are standard
  front-page convention and are not counted as errors.
- **Conflicts noted but correctly handled (no action):** #13
  goal-scorer accounts (GFA Opentil 32' vs ghanasoccernet Mubarik
  free-kick own goal — page follows the GFA, the primary source);
  #16 seat total 258 (AP) vs 259 (CNN/NBC — page follows AP);
  #15 sitting day (TimesLIVE/politicsweb/FM/africanbulletin24 say
  Monday; BusinessDay 23 Nov says Thursday — majority supports
  Monday); #7 source date (MEMO publ. 23 Nov 02:52; a jadidan
  mirror dates the same piece 22 Nov — incidents are
  overnight/Monday); #8 Vyshneve figures (AFP 2/8 Monday vs mayor
  Dikov 3/15 — page follows AFP's Monday figures); #21 Murray OT
  points 8 (AP) vs 6 (FLM — page/notes follow AP); #2 delegation
  figures (IANS 35 + 52 vs single-35 accounts — page prints
  neither); #23 cut size 10% vs 20% (page prints neither);
  #11 YES ages 18–31 (Bury Times/IfG/Reuters/Reform UK) vs
  "under-30s" (magnabureau — notes follow the 18–31 sources).

## Minor notes-only observations (NOT verdict items — no fix required)

These do not affect the image, the tallies, or submission readiness.
Listed only so the notes file stays accurate:

- **#25 location:** the notes say Albanese spoke "in Sydney on
  Monday"; the AFP/NAMPA text says he "told journalists in Canberra"
  (the AFP dateline is Sydney). The page prints no location for #25.
  Optional: drop the city from the notes or follow the AFP text.
- **#30 stale caveat line:** the "Sourcing caveat" paragraph in #30
  still says "Treat as verified-but-thin" — the fix-round paragraph
  directly below it supersedes this with the Stuff corroboration.
  Optional: update the caveat line to match.
- **README.md:14** summarises the lead as "Taiwan down 0.93% after
  a 17% week" without the "in morning trade" qualifier. README is
  not page-facing and prints no close figure, so this is cosmetic
  only. Optional: add the qualifier for consistency.

## Bottom line

The entry is clean: **31 PASS / 0 WEAK / 0 FAIL**. All three pass-2
WEAK items are fixed and verified, the Kyiv toll recheck confirms no
change is needed, and a full from-scratch re-verification of all 31
stories found no wrong date, no wrong printed figure, no claimed
outcome that did not happen, and no page-vs-notes mismatch. The
image is legible throughout with no clipping or overflow. No fixes
are required before submission.

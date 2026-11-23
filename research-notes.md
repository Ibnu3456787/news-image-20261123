# Research notes — news-image-20261123
## "THE WORLD TODAY — Monday 23 November 2026"

**Bounty:** news-image-20261123 — "Sum up 23 November's world news in one image". $100 escrowed.
**Entries close:** Tuesday 25 November 2026, 07:00 WIB.
**Final entry:** 31 stories, 6 continents (lead + 10 illustrated tiles + 20 index lines).

**Research windows:** v1 ~01:40–02:30 UTC; Asia/Europe/Africa/Middle East
~05:10–06:20 UTC; Americas/Oceania ~05:10–06:30 UTC; composition refresh
~06:35–07:00 UTC — all Monday 23 November 2026.

**Rule applied throughout:** every story must have HAPPENED, or been FIRST
REPORTED, on Monday 23 November 2026 in some timezone. Anything first reported
on 21 or 22 November was dropped, however prominently it was republished on
23 November (see "Dropped candidates" — 60+ items investigated and rejected).
Timezone-edge cases are flagged EDGE: first reported late Sunday 22 Nov UTC
but Monday 23 Nov in timezones east of UTC — the competition's "in any time
zone" rule makes these Monday stories for most of the world.

**Continent assignment convention:** by event location. Middle East stories
count as ASIA (20261122 convention). The Anthropic options listing is North
America because Cboe is in Chicago; the markets lead is Asia because the
Monday action is Seoul/Singapore/Taiwan; the Wellington Test is Oceania
because it was played in Wellington.

## Continent distribution (31 stories, 6 continents)

| Continent | Count | Stories |
|---|---|---|
| Asia | 7 | 1 lead markets, 2 Nepal–Modi, 3 JCBC, 4 spy chief, 5 Lee poll, 6 Saudi/COP31, 7 Gaza |
| Europe | 4 | 8 Kyiv toll, 9 Belgium strike, 10 Aegean quake, 11 Burnham |
| Africa | 4 | 12 Niger State, 13 Ghana, 14 ActionSA, 15 Joburg council |
| North America | 6 | 16 House, 17 Skubal, 18 Jets, 19 Anthropic, 20 49ers, 21 Nuggets/Bulls |
| South America | 2 | 22 Peru quake, 23 Brazil fiscal vote |
| Oceania | 8 | 24 Fit to Lead, 25 Albanese, 26 cricket draw, 27 Meldrum, 28 NZ retail, 29 wind farm, 30 Carter, 31 PMO staffing |
| **Total** | **31** | |

## Cut at composition (verified pool was 33)

- **Iowa lead-azide detonation** (Americas file #17): the detonation itself
  was PLANNED for Monday, not happened; the Army said only it would act "by
  November 24". Scheduled, not a completed event — cut.
- **US West Coast king tides** (Americas file #18): warnings in effect
  Monday, no outcomes reported; flooding forecast for Monday morning PST,
  after the research window. Warnings, not outcomes — cut.
- **Julie Carter (#30) KEPT** in the index: death confirmed by Wikipedia,
  Stuff (23 Nov, "dies, aged 60") and a NZ news aggregator, with
  Netball WBOP corroborating the career details; the underlying NZ
  Herald obituary was not directly retrieved — verified, kept in the
  index only, flagged below.

## Refresh outcomes (composition, ~06:35–07:00 UTC)

- **KOSPI official close: NOT confirmed.** Afternoon snapshots still
  conflict: Economic Times via smargrid −2.73% to 4,736.98; CNBC −3.74%;
  investingLive ~−3.2% near 4,710; AirRadar −3.85% (02:29 UTC snapshot).
  No reliable source confirmed the official 15:30 KST close, so the page
  prints ONLY the verified intraday figures (−5.41% to 4,606.44, sidecar
  11:33 a.m. KST) and no close figure.
- **Nepal–Modi joint statement: no outcome published yet.** The $2B
  remains Nepal's ASK; India "reportedly considering" ~$1.5B. The page
  frames the talks as happening and the package as sought, never agreed.
  Note a breakdown conflict: janpathnewsnetwork (per Indian Express /
  Kathmandu Post) gives $1B concessional loans + $500M grants + $500M
  reconstruction; particle.news/briev say $1B in grants. The janpath
  breakdown is used.
- **Burnham Commons statement: scheduled Monday afternoon GMT**, not yet
  delivered at build time. All sources use future tense. Framed as the
  statement being made Monday; no outcome claimed.
- **Joburg speaker election: outcome NOT confirmed.** A single undated
  iono.fm snippet claims ActionSA's Nobuhle Mthembu was elected, but the
  sitting had not yet happened at build time (08:50 SAST) and the item
  carries no date — NOT used. Framed as the sitting taking place.
  Seat-count conflict noted: TimesLIVE gives ANC 63 / ActionSA 43;
  africanbulletin24 gives ANC 64 / ActionSA 42. The page prints neither.
- **Brazil fiscal vote: scheduled Monday 18:00 Brasília (21:00 UTC)**,
  not yet held; one source (Primeira Análise) says analysis Monday with
  the vote Tuesday. Framed as the vote happening Monday; no outcome
  claimed. Cut-size conflict noted: most sources say a 10%
  across-the-board cut in sectoral benefits; a LIDE clipping says the
  linear cut was raised from 10% to 20%. The page prints neither.
- **Anthropic options:** US markets open 14:30 UTC, after build time, so
  first trades are NOT claimed. The Monday listing itself is confirmed by
  Cboe's own preview (earliest date under Cboe Rule 4.3).

## Fix round (audit pass 2, ~07:20–08:10 UTC)

Cold audit pass 2 returned 28 PASS / 3 WEAK / 0 FAIL. The three WEAK
items and all of the audit's notes-only corrections were addressed:

- **#1 (page):** the lead account now reads "Taiwan falls 0.93% in
  morning trade" — the −0.93% figure is a morning snapshot (CNBC TV18);
  the Taiex reversed sharply later in the session. The official close
  was NOT confirmed despite three fresh searches and a direct check of
  LiveWorldMarket (whose "live" figure moved between crawls and is never
  labelled a close), so no close figure is printed.
- **#24 (page):** tile headline reframed to the Monday launch — "Fit to
  Lead study launches in Canberra" — with the 71%/97% findings kept in
  the sub. The findings were previewed by ABC on Sunday 22 Nov; only the
  launch is a Monday event.
- **#30 (sourcing):** a second independent NZ news source was retrieved
  — Stuff, "'Tough and uncompromising': Former Silver Ferns captain
  Julie Carter dies, aged 60" (23 Nov). The NZ Herald obituary itself
  could not be retrieved directly after a genuine attempt (see #30);
  the story stays index-only, now corroborated by Stuff + Wikipedia +
  Netball WBOP.
- **#8 (recheck):** AFP/DPA consensus rechecked ~07:30 UTC — still 12 /
  Dymer 9. News Central TV alone reports 14 / Dymer 10. Page unchanged.
- **#12 (page, optional audit suggestion):** index headline now reads
  "At least 46 killed…" — it fits at size 11 (321.8 px of 392) and 46
  is a floor (the Gada Oli toll is unconsolidated but "more than Wawa").
- **Notes-only corrections applied:** #1 week distinction (worst
  percentage week since 1991 vs worst weekly point drop since 1990);
  #2 delegation figures confirmed as 35 + 52 (IANS) with the
  single-delegation conflict noted; #5 exports ₩1 trillion (Aju Press)
  with the KJD "$1 trillion" conflict noted; #6 O'Brien "hijacked"
  quote also given to AFP on Sunday; #9 SNCB trains ran normally;
  #10 M2.4 aftershock near Astypalaia; #11 Youth Experience Scheme
  ages 18–31, £5.1bn farm-trade figure sourced (Reuters / UK gov SPS
  explainer); #17 lockout 1 December; #20 McCaffrey 6-yard TD and the
  71-yard fair-catch kick both confirmed (AP); #21 Murray 8 OT points
  (AP) vs 6 (FLM), Hield 33 and the 296 combined points confirmed;
  #22 aftershock count clarified, power cut to ~93,000 verified
  (Osinergmin), Indeci report 16277 identified as the later assessment;
  #28 YoY volumes resolved (3.5% total, 4.7% core); #29 commissioning
  reconciled from Mercury's own statements. Nothing was skipped for
  lack of a source.

---

## Lead-story recommendation

**#1 — AI sell-off deepens as Asia slides (GLOBAL / ASIA).** The single
most consequential verified Monday story: a genuine Monday event with
global reach, a trading curb triggered in Seoul, and emergency government
intervention. The strongest challenger, the Kyiv-region death toll rising
to 12, is a casualty update on strikes from the Saturday–Sunday night,
not a new Monday event.

---

## Illustrated stories (lead + 10 tiles)

### 1. [LEAD] AI sell-off deepens as Asia slides — Asia / Global
**Headline:** "AI sell-off deepens as Asia slides"
**Account:** Asian markets slide on Monday after last week's wipeout in AI
and chip stocks. South Korea's chip-heavy KOSPI falls as much as 5.41%
intraday to 4,606.44 — about 21.4% below its 2 November close — prompting
the Korea Exchange to halt program selling for five minutes from 11:33
a.m. (a sell-side sidecar, triggered for a second consecutive session);
the index recovers to trade down around 3–4% in the afternoon session.
Taiwan's Taiex falls 0.93% in morning trade after a 17.5% weekly drop —
its worst percentage week since 1991 and its worst weekly point drop
(7,641.83 points) since 1990 — then reverses sharply, swinging 1,213
points intraday, reclaiming 36,000 and trading in positive territory in
the afternoon; Shanghai falls about 1% and Hong Kong's Hang Seng about
0.7%. Japan's
markets are closed for Labour Thanksgiving Day. South Korea is preparing
a market stabilisation fund of about 10 trillion won after a weekend
emergency meeting; Taiwan tightened short-selling rules on Saturday and
China exchanges eased margin-financing requirements. US futures stage a
tentative bounce: S&P 500 futures up about 2.2% and Nasdaq 100 futures up
close to 3% through the Asian session.
**Key figures:** KOSPI intraday −5.41% to 4,606.44; ~21.4% below 2 Nov
close; Friday close 4,869.96 (−5.21% on Friday); sidecar 11:33 a.m. KST,
5 minutes, 2nd straight session; Taiex −0.93% in morning trade (week
−17.5%; worst percentage week since 1991, worst weekly point drop since
1990); Taiex intraday swing 1,213.07 pts (low 35,442.41; high 36,655.48
in the morning, 37,108.2 later per LiveWorldMarket); Shanghai ~−1%;
Hang Seng ~−0.7%; stabilisation fund ~₩10 trillion; S&P 500 futures
~+2.2%, Nasdaq 100 futures ~+3%.
**Sources:** Seeking Alpha via TradingView (published 2026-11-23T03:45:50Z);
Korea JoongAng Daily (23 Nov, sidecar 11:33 a.m.); CNBC TV18 via
TradingView (23 Nov, KOSPI −3.74%, Taiex −0.93% morning snapshot);
investingLive Asia-Pacific market news (23 Nov); Seoul Economic Daily
(23 Nov); Reuters (Singapore, Nov 23) via kwsn.com, wncy.com,
wdsm710.com and others; BigGo Finance (23 Nov, 1,213-pt swing, reclaim
36,000); LiveWorldMarket (23 Nov, intraday snapshots); Taiwan News
(23 Nov, worst week since 1991); FXNews.ai (23 Nov, week −17.50%,
7,641.83 pts, Friday close 36,033.29); TradingView Asia market open
(23 Nov, Taiex +0.35% at 36,160.19 as of 01:39 UTC).
**Figure notes:** the official KOSPI close was NOT confirmed at build time
(see Refresh outcomes) — the page prints only intraday figures. The
official TAIEX close was also NOT confirmed: three fresh searches and a
direct LiveWorldMarket check (fix round, ~07:30 UTC) found only moving
intraday snapshots — LiveWorldMarket showed +2.69% at 37,001.3 in one
crawl and +2.46% at 36,917.88 in a later crawl, never labelled a close,
and Finnhub ETF data stopped at 05:17 UTC (before the 05:30 UTC close)
with no close recorded — so the page prints ONLY the qualified morning
figure ("falls 0.93% in morning trade") and no close figure. Week
distinction: Reuters/Informist call it the worst week since 1990;
Taiwan News, cryptobriefing and aiagentupdate say worst *percentage*
week since 1991 — 1990 applies to the worst weekly *point* drop
(7,641.83 points, per BigGo Finance / FXNews.ai). Korea JoongAng
Daily's "4,211.00" level is a typo (4,869.96 − 248.96 = 4,621.00)
— not used. Two Reuters updates differ on the futures bounce; the later
figures (~2% / ~1% in v1, ~2.2% / ~3% in later updates) are not printed
on the page.
**Pin:** Seoul, South Korea — 37.5665, 126.9780

### 2. Nepal's PM holds talks with Modi in Delhi — Asia
**Headline:** "Nepal's PM holds talks with Modi in Delhi"
**Account:** Nepal Prime Minister Balendra Shah holds delegation-level
talks with Prime Minister Narendra Modi at Hyderabad House, New Delhi, on
Monday, on his first bilateral visit abroad since taking office in March
2026. Shah receives a ceremonial welcome at Rashtrapati Bhavan on Monday
morning and calls on President Droupadi Murmu. Nepal is seeking a $2
billion economic package from India — $1 billion in concessional loans,
$500 million in grants and $500 million for reconstruction after the
August floods — while India is reportedly considering about $1.5 billion.
The two leaders are to unveil a Joint Vision Document, "Samriddha Nepal,
Samunnat Bharat" (Prosperous Nepal, Developed India), exchange MoUs
covering education, health, agriculture, sports, disaster management and
human resource development, and virtually flag off the Saryu-Kamala
Express, a new weekly train service between Ayodhya and Janakpur Dham.
Shah leads a 35-member government delegation plus a 52-member business
delegation; Modi hosts an official luncheon and the two address a joint
press conference.
**Key figures:** $2 billion package sought ($1B loans + $500M grants +
$500M reconstruction); India reportedly considering ~$1.5B; 35-member
government delegation + 52-member business delegation; August 26 floods
killed ~1,500.
**Sources:** IANS via newkerala.com (New Delhi, Nov 23); ANI via
desitalkchicago.com (Nov 23, ceremonial welcome); janpathnewsnetwork.com
(23 Nov, $2B breakdown per Indian Express / Kathmandu Post);
tezzbuzz.com (23 Nov, Saryu-Kamala Express); News On AIR via
industrialfront.com (23 Nov); MEA statement via thefreedompress.in,
fact.net.in, sportssun.com (ANI), obnews.co.
**Note:** the $2B is Nepal's ASK, not an agreed package, at build time
(see Refresh outcomes). Shah arrived Sunday for the two-day State visit
(22–23 Nov); the talks are the Monday event. Delegation figures
confirmed by IANS (22–23 Nov): a 35-member government delegation plus a
separate 52-member business delegation travelling at its own expense
(also newkerala, dailykiran, industrialfront, virginiatimesnow). Some
outlets (bankingnews.com.np, obnews.co, tezzbuzz) describe a single
35-member delegation including business representatives — the IANS
35 + 52 account is followed.
**Pin:** New Delhi, India — 28.6139, 77.2090

### 8. Death toll from Russian strikes on Kyiv region rises to 12 — Europe
**Headline:** "Kyiv toll rises to 12 as rescuers dig on"
**Account:** Rescuers in Ukraine race on Monday to find residents trapped
under the rubble of a five-storey block of flats in Dymer, about 45 km
north of Kyiv, after overnight Russian strikes on the Kyiv region killed
at least 12 people. The death toll in Dymer rises to nine on Monday, Kyiv
regional official Tymur Tkachenko says on Telegram, including a teenager
and a woman in her forties; rescuers pulled a child alive from the debris
on Sunday evening and are still searching for 11 people, including two
children. Two more people are killed and eight wounded when a strike hits
a supermarket in Vyshneve, and one person is killed when a strike sets a
private home ablaze in Bila Tserkva. Russia also strikes a power
substation in the Dnipropetrovsk region, Prime Minister Sergiy Koretsky
says, as Moscow ramps up attacks on Ukraine's energy network with
temperatures dropping toward freezing.
**Key figures:** at least 12 dead across Kyiv region (Dymer 9, Vyshneve 2,
Bila Tserkva 1); 8 wounded in Vyshneve; 11 people still missing in Dymer
incl. 2 children; Dymer toll was 5 late Sunday, 9 by Monday.
**Sources:** DPA via dailyfoxnews.com (Mon 23 Nov 02:03 UTC, Dymer toll
rises to nine); AFP via europesays.com (published 2026-11-23T03:29:19Z,
at least 12 dead); metapress.net (23 Nov); France 24 (23 Nov); AFP via
redhot.sg (23 Nov, 12 / Dymer 9); world-today-journal.com (23 Nov).
**Recheck (fix round, ~07:30 UTC):** AFP/DPA consensus still 12 / Dymer
9 — europesays (AFP), redhot.sg (AFP), metapress and world-today-journal
all still report 12 with Dymer at nine. News Central TV alone
(published 2026-11-23T04:54:33Z) reports 14 / Dymer 10; no wire source
has confirmed a higher toll. Page unchanged at 12/9.
**Note (date care):** the Dymer block was hit in the overnight attack
between Saturday and Sunday; late Sunday the toll stood at 5. The MONDAY
news is the toll rising to 9 in Dymer / 12 across the region and the
ongoing rescue — framed as the toll rising on Monday, not the strikes as
Monday events. The Vyshneve supermarket strike was reported Sunday
evening with early figures (3 killed, 15 wounded — dropped in v1); the
Monday figures are 2 killed, 8 wounded. Use the Monday figures.
**Pin:** Dymer, Kyiv Oblast, Ukraine — 50.78398, 30.31239

### 9. Belgium grinds to a halt in nationwide strike — Europe
**Headline:** "Belgium grinds to a halt in nationwide strike"
**Account:** Belgium faces a near-total shutdown on Monday as a nationwide
general strike called by the three main trade unions — ACV-CSC, ABVV-FGTB
and ACLVB — protests the federal government's austerity measures, pension
overhaul and declining purchasing power under Prime Minister Bart De
Wever. Air traffic controllers at Skeyes walk out from 07:00 to 21:00
local time, so Brussels Airport cancels the majority of its 429 scheduled
flights (213 departures, 216 arrivals, about 59,500 passengers) and
Brussels South Charleroi Airport cancels all flights for the day.
Brussels public transport (STIB-MIVB) is heavily disrupted and about
4 in 10 De Lijn buses and trams in Flanders do not run, while national
rail (SNCB/NMBS) runs normally — "No strike notice was submitted, so our
service will run as normal on Monday," SNCB spokesperson Dimitri
Temmerman told The Brussels Times. Ports and customs face
interruptions. The action coincides with a royal deadline
for De Wever to break a political deadlock over a contentious €10 billion
budget adjustment.
**Key figures:** 429 Brussels Airport flights scheduled (213 out, 216 in);
~59,500 passengers affected; ATC walkout 07:00–21:00 (14 hours);
Charleroi: all flights cancelled; €10 billion budget plan at issue.
**Sources:** IBTimes SG (23 Nov); ftnnews.com (23 Nov, 59,500 passengers /
429 flights); eurotoday.org (23 Nov, citing Brussels Morning Newspaper 22
Nov); nomadlawyer.org (23 Nov); cargonice.com (23 Nov, ports/customs);
europesays.com (23 Nov, SNCB quote via The Brussels Times);
striketracker.app (23 Nov, STIB heavily disrupted, ~4 in 10 De Lijn
services cancelled, SNCB no disruption).
**Note:** the strike was ANNOUNCED on Saturday 21 Nov (Skeyes statement),
but the strike itself is the Monday event — this is a Monday story, not a
republication. Rail correction (fix round): an earlier draft said SNCB
was "heavily disrupted", following nomadlawyer.org; SNCB itself says no
strike notice was submitted and trains ran normally — the SNCB account
is followed.
**Pin:** Brussels, Belgium — 50.8503, 4.3517

### 13. [EDGE] Ghana win Amputee Football World Cup — Africa
**Headline:** "Ghana win Amputee World Cup"
**Account:** Ghana's Black Challenge beat Morocco 1–0 in the final of the
2026 WAFF Amputee Football World Cup in San Juan de los Lagos, Mexico, to
win the country's first-ever world title in amputee football. Captain
Richard Opentil scores the decisive goal in the 32nd minute. Ghana become
only the second African nation to lift the trophy after Angola in 2018,
having beaten defending champions Turkey in a penalty shootout in the
semi-final. Forward Mohammed Mubarik wins the Golden Boot as the
tournament's top scorer with seven goals. Ghana's Ministry of Sports and
Recreation issues a statement on Monday congratulating the team, calling
it "a moment of immense national pride".
**Key figures:** 1–0 final; Opentil goal 32nd minute; Mubarik Golden Boot,
7 goals; first Ghanaian world title; second African winners after Angola
(2018).
**Sources:** Ghana Football Association / ghanafa.org (23 Nov); Graphic
Online (23 Nov 03:50 GMT); Metro TV Online (23 Nov); ghanasoccernet.com
(23 Nov, Sports Ministry statement issued Monday 23 Nov);
ghanasportsonline.com (23 Nov, Golden Boot).
**Timezone note (EDGE):** the final was played on Sunday evening in Mexico
(UTC−6) and ended after midnight UTC — Monday 23 Nov in UTC and in Ghana
(UTC+0). First Ghanaian reports are Monday morning (Graphic Online 03:50
GMT). Same pattern as the Jets story (game ended after midnight UTC). One
source (ghanasportsonline) calls it "Monday's final"; most say "Sunday's
final" (Mexico local time). The Ministry's congratulatory statement is
unambiguously Monday. Goal-scorer detail conflicts across Ghanaian outlets
(Opentil 32nd-minute strike vs a Mubarik free-kick turned in as an own
goal); the GFA/Graphic account (Opentil, 32nd minute) is used.
**Pin:** Accra, Ghana — 5.6037, -0.1870 (team's home; the final was played
in San Juan de los Lagos, Mexico, approx. 21.25, -102.33)

### 16. [EDGE] Democrats clinch 258 House seats — North America
**Headline:** "Democrats clinch 258 House seats"
**Account:** Democrat Chuck Hubbard defeats 11-term Republican Rep.
Virginia Foxx in North Carolina's 5th district by 330 votes out of
287,000 cast after a recount Foxx requested; Foxx concedes. The win takes
Democrats to at least 258 House seats — their largest House majority since
1992 (when they also won 258), a net gain of 44 seats, four more than the
40 they picked up in 2018. Republicans hold at least 173 seats. Four
races remain uncalled: Minnesota's 1st, Tennessee's 4th (where Republican
Scott DesJarlais conceded last Monday to Democrat Victoria Broderick,
though AP has not called it), and Louisiana's 5th and 6th, headed to
December runoffs. The Democratic total could top out at 260. Democrats
will also hold 56 of 100 Senate seats; the new Congress meets 3 January
2027.
**Sources:** AP (AP News in Brief 6:04 p.m. EST Sunday; "The 258-seat tally
was reached Sunday after Democrat Chuck Hubbard defeated Republican Rep.
Virginia Foxx"); Reuters (WASHINGTON, Nov 22); WVLT/AP; TMJ4;
political.org; The Why Daily (updated Nov 22, 5:05 p.m. CT); Thursday
Review; Trinidad Tribune; NJ Radar Online; Daily Fox News.
**Timezone note (EDGE):** the AP call/concession came on Sunday evening in
the US (6:04 p.m. EST = 23:04 UTC Sunday), which is Monday 23 November in
every timezone from UTC+1 eastward. Monday story under the "any time
zone" rule.
**Pin:** US Capitol, Washington DC — 38.8899, -77.0091 (pin offset on the
map: Washington and New York sit close together)

### 17. [EDGE] Skubal signs record $450M Mets deal — North America
**Headline:** "Skubal signs record $450M Mets deal"
**Account:** Two-time Cy Young Award winner Tarik Skubal agrees a
nine-year, $450 million contract with the New York Mets — the richest
contract ever for a pitcher, at $50 million a year, topping Yoshinobu
Yamamoto's $325M deal and nearly doubling Yamamoto's $27.1M average
annual value. $45M signing bonus (protected from a potential 2027
lockout), full no-trade clause, $30M deferred, no opt-outs. Skubal, 30
(turned 30 on 20 Nov), split 2026 between Detroit and the Los Angeles
Dodgers (2.72 ERA, 26 starts). Mets owner Steve Cohen: "I don't have to
worry about him pitching in New York. He's an outstanding individual."
The deal comes about a week before the collective bargaining agreement
expires at 11:59 p.m. ET on 1 December, when MLB owners are expected to
lock players out. The agreement is subject to a successful
physical; the Mets have not formally announced the signing.
**Sources:** AP via arizonasports.com / dailyfoxnews.com ("a person
familiar with the negotiations told The Associated Press on Sunday");
ESPN/Jeff Passan (Nov 22); Bleacher Report (Nov 23 — Cohen quote, via The
Athletic's Will Sammon / NY Post's Jon Heyman); NY Post's Joel Sherman
(deferrals, no options); focalnews.org (Nov 23); Flashscore; SI;
dailyfoxnews.com / bvmsports.com (CBA expires 11:59 p.m. ET Dec. 1).
**Note:** an earlier draft said the lockout was expected on 2 December;
the CBA expires at 11:59 p.m. ET on 1 December and the lockout is
expected then (NBC Sports / FanGraphs / BVM Sports). Some outlets
phrase the lockout itself as starting "the next day" (2 Dec).
**Timezone note (EDGE):** agreed/reported Sunday evening US time
(yardbarker "Last updated Nov 22, 2026 5:42 PM ET" = 22:42 UTC Sunday),
which is Monday 23 November in Asia-Pacific timezones (05:42 WIB). Monday
story under the "any time zone" rule. The Cohen quote and meeting colour
are new Monday reporting.
**Pin:** Citi Field, Queens, New York — 40.7571, -73.8458 (pin offset on
the map: Washington and New York sit close together)

### 20. Purdy stars as 49ers rout Vikings 35–10 in Mexico City — North America
**Headline:** "Purdy stars as 49ers rout Vikings 35–10 in Mexico City"
(Page tile headline shortened to "49ers rout Vikings 35–10 in Mexico
City"; Purdy detail in the tile sub.)
**Account:** Brock Purdy throws three first-half touchdown passes as the
San Francisco 49ers rout the Minnesota Vikings 35–10 in Sunday Night
Football at Estadio Banorte in Mexico City, moving to an NFC-best 9–1 —
their third win in a third country this season. Purdy finishes 21-for-26
for 255 yards and three touchdowns, drawing "MVP" chants from the crowd;
Christian McCaffrey caps a 13-play, 98-yard drive with a 6-yard touchdown
run for the 35th point early in the fourth quarter. Kirk Cousins throws a
pick-six in the second quarter as the Vikings fall to 7–3; Will Reichard's
71-yard fair-catch kick just before half-time — which would have beaten
the NFL record of 68 yards set by Cam Little last season — falls just
short. The game kicked off at 8:20 PM ET
Sunday and ended after midnight ET — Monday 23 November in UTC.
**Sources:** NBC Sports (Nov 23); NBC Sports Bay Area live updates
(Nov 23); ESPN (AP, MEXICO CITY); Bleacher Report (Nov 23);
yardbarker.com; Daily Norseman; sportradar (Mon 23 Nov 2026 8:20 AM WIB,
L 10–35).
**Timezone note:** kickoff 8:20 PM ET Sunday = 01:20 UTC Monday; the game
ended ~05:00 UTC Monday. The result was first reported on Monday 23 Nov
in UTC and in the Americas. Same pattern as the Jets story.
**Figure notes (fix round):** McCaffrey's TD run is 6 yards per AP
(theScore), NBC Sports and the theScore scoring summary ("rushed up the
middle for 6 yards") — the Daily Norseman's 5 yards is wrong. The
71-yard attempt is confirmed by AP: a fair-catch kick by Will Reichard
after a fair catch at the Vikings' own 40 with 3 seconds left in the
first half, which "came up just short" of the 68-yard NFL record.
**Pin:** Estadio Banorte, Mexico City — 19.3029, -99.1505

### 24. Fit to Lead study launches in Canberra — Oceania
**Headline:** "Fit to Lead study launches in Canberra"
**Account:** The Fit to Lead study launches at Parliament House, Canberra,
on Monday (15:30–17:30 AEDT, keynote by Alastair Campbell). The Better
Politics Foundation surveyed 288 current and former elected
representatives (Feb 2025 – Feb 2026): 71% of state and federal
parliamentarians and 61% of councillors say the job adversely affected
their mental health or wellbeing; 97% of those affected cite online
abuse; about 1 in 5 affected reported thoughts of self-harm or suicide;
44% of affected parliamentarians say fears for their safety or their
family's significantly damaged their wellbeing (women 51%, men 35%); 85%
would still encourage others to stand for office. The study was
conducted before the October attack on independent MP Helen Haines, who
lost both legs in an alleged targeted attack outside her Wangaratta
electorate office. Campbell: democracies are "failing those who serve,
and deterring others from wanting to serve in the first place."
**Sources:** Better Politics Foundation (report launching November 23,
2026; launch 15:30–17:30, Parliament House, Canberra); ABC News (Annabel
Crabb, Sun 22 Nov 6:00pm AEDT); zot.news; newsy-today.com; briev.ai;
en.killbait.com.
**Note:** findings were previewed by ABC on Sunday evening AEDT; the
launch event itself is Monday 23 Nov, and the story is framed as the
launch. At research time (~06:30 UTC) the launch was just concluding; no
outcome coverage of the launch event itself had yet appeared.
**Framing (fix round):** the tile headline was reframed from the finding
("Most Australian MPs say politics harmed their mental health") to the
Monday launch ("Fit to Lead study launches in Canberra"), keeping the
71% figure in the sub — the findings were first reported Sunday, only
the launch is a Monday event.
**Pin:** Parliament House, Canberra — -35.3081, 149.1244 (pin offset on
the map: Canberra, Melbourne and Wellington sit close together)

### 26. New Zealand bat out a draw after India's record 720/9 — Oceania
**Headline:** "New Zealand bat out a draw after India's record 720/9"
**Account:** The 1st Test at Basin Reserve, Wellington, ends in a draw on
Monday: New Zealand 368 and 239/5 (120 overs) drew with India 720/9 dec.
India are denied their first Test win in New Zealand since 2009. On the
final day India dismiss both overnight batters before lunch — Devon
Conway caught behind off Washington Sundar for 65, Rachin Ravindra out
for 37 to Prasidh Krishna — and Tom Blundell for 15 after lunch, leaving
New Zealand 157/4 at lunch and 206/5 at tea, still 146 behind. But Daryl
Mitchell (49 not out off 186 balls) and Glenn Phillips (unbeaten, 126
balls) bat 43 overs together to force the stalemate; the teams agree the
draw before the final hour. India declared at 720/9 on Sunday — the
highest Test total in New Zealand — for a first-innings lead of 352. The
draw pushes India further from World Test Championship final contention;
New Zealand slip to No. 3 on the WTC table. The second Test starts in
Christchurch on Friday.
**Sources:** ESPNcricinfo match report (Nov 23); AP via crictoday.com
(Wellington, Nov 23); IANS (Wellington, Nov 23, tea report);
inshorts.com (Nov 23); NDTV live (sent Mon 23 Nov 2026 04:43 UTC);
Cricbuzz live; sportradar live.
**Note:** the match FINISHED during the research window. The v1 notes'
"close in on win" framing is replaced by the confirmed draw — the old
framing must NOT be used. The 720/9 declaration is Sunday news and is
used only as context.
**Pin:** Basin Reserve, Wellington — -41.3005, 174.7803 (pin offset on
the map: Canberra, Melbourne and Wellington sit close together)

### 27. Molly Meldrum dies aged 83 — Oceania
**Headline:** "Molly Meldrum dies aged 83"
**Account:** Ian "Molly" Meldrum, the Countdown host, music journalist
and record producer who championed Australian music for six decades, dies
peacefully at 5:30am on Monday 23 November at Epworth Hospital in
Richmond, Melbourne, aged 83, after a long period of ill health. His
management announces his death; a state funeral will be held. Tributes
pour in from across the music industry and sport — including his beloved
St Kilda Saints and the Melbourne Storm — and from ARIA and APRA AMCOS.
**Sources:** AAP (Nov 23); Sydney Morning Herald via if.com.au; Herald
Sun via themusicnetwork.com; Mumbrella (Nov 23); Mediaweek (Nov 23);
ARIA (23 November 2026); APRA AMCOS; Flashscore (Nov 23); Wikipedia
(died 23 November 2026, Richmond, Victoria).
**Pin:** Epworth Hospital, Richmond, Melbourne — -37.8230, 144.9983 (pin
offset on the map: Canberra, Melbourne and Wellington sit close together)

---

## Index stories ("ALSO ON THIS DAY")

### 3. China–Singapore council meets as Ding visits — Asia
**Headline:** "China–Singapore council meets in Singapore"
**Account:** Chinese Vice Premier Ding Xuexiang co-chairs the 22nd
China-Singapore Joint Council for Bilateral Cooperation (JCBC) in
Singapore on Monday with Deputy Prime Minister Gan Kim Yong, alongside
the joint steering councils for the Suzhou Industrial Park, the Tianjin
Eco-City and the Chongqing connectivity initiative. Prime Minister
Lawrence Wong said earlier that more than 20 deliverables are expected,
spanning trade, digitalisation, financial integration, research and
innovation, healthcare and education. Ding arrived in Singapore on
Sunday for the two-day visit. The meeting follows Wong's talks with Xi
Jinping in Shenzhen on Friday, at which the two sides launched
negotiations to upgrade their bilateral free trade agreement to CSFTA 4.0.
**Key figures:** 22nd JCBC; more than 20 deliverables expected; 3
flagship project steering councils; visit 22–23 Nov.
**Sources:** nglobenews.com (22 Nov, citing MFA Singapore / MFA China /
Xinhua); littlebigreddot.com (23 Nov, "Ding Xuexiang Singapore visit:
JCBC talks on 23 November"); Asia Daily (22 Nov, CSFTA 4.0 launch 20 Nov).
**Note:** the JCBC meeting itself is the Monday event; the CSFTA 4.0
launch (20 Nov) is context only.

### 4. Seoul won't confirm spy chief replacement reports — Asia
**Headline:** "Seoul silent on spy chief replacement reports"
**Account:** South Korea's presidential office declines on Monday to
confirm reports that National Intelligence Service Director Lee
Jong-seok is to be replaced, saying "we cannot confirm matters related
to personnel" — without explicitly denying the reported replacement. One
outlet reported the same day that President Lee Jae-myung is considering
replacing the intelligence chief he appointed early in his term, after
one year and five months, with former Justice Minister Kang Kum-sil the
leading candidate to succeed him. Prolonged friction between South
Korean and US intelligence authorities and the lack of a breakthrough in
inter-Korean relations were cited as factors. Kang was the first woman
to serve as justice minister in the country's constitutional history.
**Key figures:** Lee Jong-seok in post 1 year 5 months; Kang Kum-sil
named as front-runner.
**Sources:** Seoul Economic Daily (published 2026.11.23 10:25 KST =
01:25 UTC), presidential spokesperson Kim Sung-wan at Chunchugwan
briefing.

### 5. Lee Jae Myung's approval rating rises to 37.3% — Asia
**Headline:** "Lee's approval rating rises to 37.3%"
**Account:** South Korean President Lee Jae Myung's approval rating rises
for a second consecutive week to 37.3%, a Realmeter poll released on
Monday finds. Positive assessments rose 0.9 percentage points from the
previous week, while negative assessments fell 1 point to 59.9%.
Realmeter attributed the rise to diplomatic and economic gains — Lee's
attendance at the ASEAN and APEC summits and his meeting with Xi Jinping,
and exports topping ₩1 trillion — while the KOSPI falling below 5,000
and the college-entrance-exam AI-cheating controversy held back further
gains. In party support, the opposition People Power Party leads on
42.5% (down 0.5 points) against the ruling Democratic Party's 35.6% (up
1 point).
**Key figures:** approval 37.3% (+0.9pp); disapproval 59.9% (−1pp); poll
of 2,514 adults, 16–20 Nov; PPP 42.5%, DP 35.6% (1,010 adults, 19–20
Nov); margin of error ±2.0pp / ±3.1pp at 95% confidence.
**Sources:** Korea JoongAng Daily (published 2026-11-23T02:55:56Z,
Yonhap); Aju Press (23 Nov, survey released November 23). Commissioned
by Asia Business Daily / Asia Economy.
**Note:** Aju Press says the export milestone is "1 trillion won in
exports" (twice); Korea JoongAng Daily (Yonhap) says "exports topping
the $1 trillion mark". The two sources conflict on the currency; the
Aju Press wording (₩1 trillion) is used, as Aju Press is the cited
source for the survey detail.

### 6. Saudi influence 'loomed large' over failed COP31 deal — Asia (Middle East)
**Headline:** "Saudi hand seen behind failed COP31 deal"
**Account:** Saudi Arabia's influence loomed large over the failed COP31
climate deal, Reuters reports from Antalya on Monday, citing negotiators
from Europe, small island states, Latin America, Asia and Africa. Saudi
officials had regular access to the talks' Turkish and Australian
presidents while other delegations struggled to get meetings, and Riyadh
was at the forefront of resisting language on reducing reliance on
fossil fuels — chiefly why no political agreement could be reached, for
the first time since 2009. "This COP, I believe, was hijacked by some
oil states," Ireland's climate minister Darragh O'Brien told Reuters on
behalf of the European Union. The Turkish COP presidency said no group
or country was given "preferential treatment". Negotiators said Riyadh's
hand was strengthened by the absence of active US engagement and the
lack of close US-China coordination.
**Key figures:** first COP without a political agreement since 2009; EU,
small island states and others rejected a draft with no mention of
fossil fuels.
**Sources:** Reuters (ANTALYA, Nov 23) via dailyfoxnews.com, wdsm710.com,
dukecountry.fm, kwsn.com (23 Nov); sumi.news Middle East feed (23 Nov).
**Note:** the COP31 collapse itself is Sunday 22 Nov news (dropped in
v1); this Monday Reuters investigation — with the O'Brien "hijacked"
quote — is the Monday story, on the same basis as the Albanese reaction
story (#25). Note the quote was ALSO given to AFP on Sunday: phys.org
(22 Nov) reports O'Brien told AFP outside the assembly hall that the
summit had been "hijacked by some oil states", and NAMPA/AFP (22 Nov)
carried it the same day. The Monday story is the Reuters investigation
itself, not the quote alone.

### 7. Israeli attacks kill 3 in Gaza in latest ceasefire violation — Asia (Middle East)
**Headline:** "Three killed in Gaza as truce frays"
**Account:** Three Palestinians are killed and four others, including a
child, injured in Israeli attacks across the Gaza Strip, medical sources
tell Anadolu Agency on Monday, in the latest violation of the ceasefire
that took effect on 10 October 2025. A 50-year-old man is killed when an
Israeli drone drops a bomb near Al-Matahin junction east of Deir
al-Balah; a Palestinian dies of wounds from an overnight strike on a camp
for displaced people in Al-Mawasi, west of Khan Younis, in which five
were wounded; and another dies of wounds from a drone strike in
Al-Maslakh, south-west of Khan Younis, on Saturday evening. A 12-year-old
boy is shot in the back in Al-Sikka, central Khan Younis, and a drone
strike on civilians in Bir al-Naaja, west of Jabalia, injures three, one
seriously. Israeli violations of the ceasefire have killed 1,675
Palestinians and injured 6,095 since 10 October 2025, Gaza's Health
Ministry says; Israel's war on Gaza has killed more than 74,000
Palestinians since October 2023.
**Key figures:** 3 killed, 4 injured (incl. a child) on Monday; 5 wounded
in the Al-Mawasi strike; 1,675 killed / 6,095 injured since the ceasefire
began; more than 74,000 killed since October 2023.
**Sources:** Middle East Monitor / Anadolu Agency (published 23 Nov 2026,
02:52); 7788news.com (23 Nov, MEMO/Anadolu text).
**Note (date care):** do NOT confuse with the Tel al-Hawa food-vehicle
strike (3 killed, 21 Nov — dropped) or the AP Sunday roundup (8 killed,
22 Nov — dropped). This MEMO/Anadolu report covers different, overnight /
Monday incidents first reported Monday.

### 10. M4.2 quake in the Aegean off Bodrum — Europe
**Headline:** "M4.2 quake in the Aegean off Bodrum"
**Account:** A magnitude 4.2 earthquake is recorded in the Aegean Sea,
66.74 km off Bodrum (Muğla, Türkiye), at 02:42 local time on Monday
(23:42 UTC Sunday), depth 9.43 km. No damage reported. The largest
aftershock near the epicentre was an M2.4 ten minutes after the
mainshock (23:52 UTC Sunday / 02:52 Monday local), 31 km NNE of
Astypalaia Island (NOA via volcanoesandearthquakes.com); AFAD's
23 November list of Turkish events shows only minor tremors, the
largest a magnitude 1.7 in Izmir Bay at 00:06. (An undated "6.1-magnitude western
Turkey" item circulating online could not be verified as a 23 Nov event
and is dropped.)
**Key figures:** M4.2 (Mw); 66.74 km off Bodrum; 02:42:48 local, 23 Nov;
36.78767 N, 26.56167 E; depth 9.43 km.
**Sources:** AFAD via turkishnewsworld.com (2026-11-23); USGS via
terremoto.developers.do (M4.2, 33 km WSW of Pánormos, Greece); AFAD daily
list via turkishnewsworld.com (23 Nov, no significant aftershocks);
volcanoesandearthquakes.com quake list (updated 23 Nov 04:00 UTC, M2.4
23:52 UTC near Astypalaia, NOA).
**Timezone note:** Monday 23 Nov in Türkiye (UTC+3) / Greece (UTC+2);
Sunday 22 Nov 23:42 UTC. Monday story under the "any time zone" rule.

### 11. Burnham asks MPs to back his 'landmark' EU deal — Europe
**Headline:** "Burnham asks MPs to back his EU deal"
**Account:** Prime Minister Andy Burnham tells MPs on Monday that the deal
struck with the EU in Brussels on Friday 20 November is a "landmark"
agreement and "the single biggest growth measure to be delivered in this
parliament", pitching it as a choice between easing pressure on the cost
of living or allowing food prices to rise further. The package eases food
and farm trade, links emissions trading systems and creates a Youth
Experience Scheme letting 100,000 18–31-year-olds from each side live,
work or study in the other's territory for up to three years, with the
first young people travelling no later than January 2030; Britain
will also rejoin Erasmus+. Burnham says the Treasury estimates the deal
adds up to 0.5% to UK GDP, a £17 billion boost; Conservative leader Kemi
Badenoch disputes the figure, saying Burnham "plucked that figure out of
the air", and calls the deal "terrible" at the CBI conference on Monday.
Former prime minister Theresa May said on Sunday she was "aghast" at
talk of further EU negotiations.
**Key figures:** £17 billion / 0.5% GDP claim (Treasury estimate,
disputed); 100,000 18–31-year-olds each side, up to 3 years, first
travellers no later than January 2030; farm-trade (SPS) arrangement
worth up to £5.1 billion a year vs projected 2040 levels (+0.14% GDP).
**Sources:** madeinshoreditch.co.uk (23/11/2026, citing BBC News);
magnabureau.space (22 Nov 20:14 GMT, deal details); BBC via both; The
Standard (23 Nov, supermarket visit + Commons statement later Monday);
Bury Times / Oldham Times (20 Nov, 18–31 scheme, 100,000 visas a year);
Institute for Government (20 Nov, YES aged 18–31); Reuters via
live.euronext.com (20 Nov, £5.1bn/yr food-trade estimate); UK
government SPS explainer (assets.publishing.service.gov.uk, "worth up
to £5.1 billion a year when compared to projected levels in 2040,
increasing UK GDP by up to 0.14%").
**PENDING at build time:** the Commons statement is scheduled for Monday
afternoon GMT. Frame as the statement being made on Monday; no outcome
claimed (see Refresh outcomes). The deal itself (20 Nov) is context; the
Monday story is Burnham selling it to Parliament.

### 12. [EDGE] At least 46 killed in Niger State attacks and reprisals — Africa
**Headline:** "At least 46 killed in Niger State attacks and reprisals"
(Page index line now carries "At least" too — restored in the fix round;
it fits at size 11, and 46 is a floor: the Gada Oli toll is
unconsolidated but "more than the Wawa killing".)
**Account:** At least 46 people are killed in a spate of attacks in Borgu
district, Niger State, central-western Nigeria. Armed gangs attack Luman
Ba'are, a Kambari village, at dawn on Saturday during prayers, killing
11 residents including the village chief, burning homes, stealing cattle
and abducting residents. Local vigilantes then stage reprisal attacks on
Fulani settlements in neighbouring Wawa and Gada Oli; a security report
seen by AFP puts the Wawa toll at 35 Fulani killed, with burials still
under way and bodies still being found, while a community leader who took
part in a mass burial gives 38. The report says the toll in Gada Oli is
"more than the Wawa killing". Niger State authorities deploy joint
security teams and urge residents not to take justice into their own
hands.
**Key figures:** at least 46 dead in total (11 in Luman Ba'are raid + 35
in Wawa reprisals); Wawa community leader's count 38 (37 men, 1 woman);
Gada Oli toll unconsolidated but "more than Wawa" per the security
report; state government counts 5 dead in the initial raid (security
sources: 11).
**Sources:** AFP via thenews.pk (23 Nov); AFP via RFI Afrique (22 Nov
22:16 GMT); beninwebtv.bj (23 Nov, AFP security report); ThisDay (22 Nov
12:30 UTC, initial attacks); veritynewsonline.com (23 Nov, police/state
figures).
**Timezone note (EDGE):** the attacks happened Saturday 21 Nov and the AFP
report was first published Sunday 22 Nov at 22:16 UTC — which is Monday
23 Nov in every timezone from UTC+2 eastward (00:16 in Johannesburg/
Cairo, 06:16 in Beijing). Included under the "any time zone" rule on the
same basis as the House-seats story. The killings are a weekend event
first reported as a consolidated toll late Sunday UTC / Monday in the
eastern hemisphere.

### 14. Six ex-councillors sue ActionSA for R3.1m — Africa
**Headline:** "Ex-councillors sue ActionSA for R3.1m"
**Account:** Six former ActionSA Johannesburg councillors claim more than
R3.1 million for loss of income, accusing the party of selectively
enforcing membership recruitment targets, disregarding their explanations
for failing to meet them and removing them from their positions last
year, while allegedly allowing other councillors in comparable
circumstances to remain. In a summons filed at the Johannesburg high
court on 13 November, Paul Nefdt, Elmari Atterbury, Esmie Liebenberg,
Edwin Ntshidi, Zahid Jainoodeen and Delano Coverdale accuse the party of
breaching their contractual agreements. Their councillor terms were due
to end on election day, 4 November, with an option to renew. Approached
for comment, ActionSA president Herman Mashaba said only that the
councillors should "exercise their rights".
**Key figures:** total claim over R3.1m; Nefdt R540,489; Atterbury
R505,089; Liebenberg R540,488; Ntshidi R540,488; Jainoodeen R505,089;
Coverdale R513,641; interest sought from 30 September 2025 plus legal
costs.
**Sources:** Sowetan (2026-11-23, sowetan.co.za/news/2026-11-23-...);
TimesLIVE (23 Nov 02:30 GMT, per AfricaFrontPage).
**Note:** the summons was filed 13 Nov but the claim is FIRST REPORTED on
23 Nov (Sowetan/TimesLIVE) — a Monday story under the first-reported rule.

### 15. Hung Joburg council sits to swear in councillors — Africa
**Headline:** "Hung Joburg council sits for first time"
**Account:** Johannesburg's new hung council holds its first sitting on
Monday to swear in councillors and elect a speaker, after the 4 November
local elections left no party with a majority in the 270-seat chamber (a
majority is 136). The DA finished first with 91 seats; ActionSA, with
43, holds the balance of power, with the ANC on 63. Coalition talks
continue: the ANC has proposed Herman Mashaba as mayor with ANC regional
chair Loyiso Masuku as deputy, while the DA has published a
confidence-and-supply offer with Helen Zille as mayor. The mayoral vote
itself may wait until Wednesday. No mayor has been elected in any of the
hung Gauteng metros.
**Key figures:** 270 seats, majority 136; DA 91, ANC 63, ActionSA 43
(ANC + ActionSA = 106, 30 short of a majority).
**Sources:** TimesLIVE via community.southafricafacts.co.za ("Who will
govern the hung metros? 22 Nov" — first sitting Monday 23 Nov confirmed
by TimesLIVE report); Financial Mail (22 Nov, ActionSA kingmaker);
africanbulletin24.com (23 Nov); politicsweb.co.za (23 Nov diary);
Business Day (23 Nov).
**PENDING at build time:** the sitting is a scheduled Monday event; the
speaker election outcome was not confirmed at build time (see Refresh
outcomes). Framed as the sitting taking place, not as a result. Seat
counts conflict across sources (ANC 63 vs 64, ActionSA 43 vs 42); the
TimesLIVE figures are used and the page prints neither.

### 18. [EDGE] Jets end five-game skid, 27–24 over Chargers — North America
**Headline:** "Jets end five-game skid, 27–24 over Chargers"
**Account:** The New York Jets beat the Los Angeles Chargers 27–24 at
SoFi Stadium, Inglewood, ending a five-game losing streak; the Jets
scored on their first five drives. Geno Smith completes 17 of 21 passes
for 176 yards and three touchdowns with no interceptions; Sterling
Shepard scores twice for New York, Ladd McConkey twice for Los Angeles.
The Jets' first win since facing the Chiefs and Bills in consecutive
weeks.
**Sources:** AP via dailyfoxnews.com; athlonsports.com (Nov 22, 2026
8:04 PM EST); dyma-data.com; StatMuse (AP recap dated Nov 23, 2026).
**Timezone note (EDGE):** the late Sunday game in California ended after
midnight UTC — Monday 23 November in UTC and in Asia-Pacific timezones.
The game report timestamp (8:04 PM EST = 01:04 UTC Monday) confirms
Monday reporting.

### 19. Anthropic options debut as traders brace for 100–150% volatility — North America
**Headline:** "Anthropic options debut as traders brace for 100–150% volatility"
(Page index line shortened to "Anthropic options debut; volatility seen
at 100–150%" to fit one line.)
**Account:** Listed options on Anthropic (ANT) begin trading on Monday,
23 November — the earliest possible date under Cboe Rule 4.3, two
business days after the Nasdaq debut on 19 November — with all 20 US
options exchanges expected to list the contracts. Market makers on the
Cboe floor estimate implied volatility of 100% to 150% (CNBC, Nov 20).
Monthly contracts and longer-dated LEAPS are available at launch, with
strikes roughly 50% above and below the spot price in $5 increments near
ANT's ~$87 level; weekly Friday expirations are added later in the week,
the first expiring Friday 27 November. ANT closed Friday at $88.91, down
8.5% on its second day, after opening at $111.50 on Thursday and closing
day one at $97.17 (IPO price $83; 980 million shares, $81.34 billion —
the largest IPO on record). Tradr is also launching 2x leveraged (ANTT)
and 2x inverse (ANTZ) Anthropic ETFs on Cboe on Monday.
**Sources:** Cboe "Anthropic Options Preview" (Henry Schwartz, Nov 20);
Reuters (Nov 18) via aistockwire.com; CNBC (Nov 20) via aiagentupdate.com
(Nov 22); tradersunion.com (Tradr ETFs, Nov 23); livetube.tv (Reuters
World News video, Monday November 23, 2026).
**Note:** framed as a Monday debut — US markets open 09:30 ET (14:30
UTC), after build time, so first-day trading itself is not claimed. The
listing date is confirmed by Cboe's own preview. The Riemann
certification (21 Nov) is NOT claimed as a Monday story.

### 21. Murray's 45 and Jokic's 202nd triple-double win OT thriller — North America
**Headline:** "Murray's 45 and Jokic's 202nd triple-double win OT thriller"
(Page index line shortened to "Murray's 45, Jokic's 202nd triple-double
win OT thriller" to fit one line.)
**Account:** Jamal Murray scores a season-high 45 points and Nikola Jokic
records the 202nd triple-double of his career (37 points, 18 rebounds,
11 assists) as the Denver Nuggets beat the Chicago Bulls 151–145 in
overtime at the United Center — the NBA's highest-scoring game of the
season. Murray scores eight of his 45 in overtime and the pair combine
for 82 points, the second-most they have ever combined for. Jokic moves
seven shy of Russell Westbrook's NBA record of 209 career triple-doubles.
For Chicago, Buddy Hield scores 33 and Josh Giddey posts 23 points, 14
rebounds and a career-high 22 assists — the most assists in any NBA game
this season. The Nuggets improve to 10–5, their third straight win; the
Bulls fall to 4–12.
**Sources:** AP via theScore / TSN (CHICAGO); Field Level Media
(published 2026-11-23T03:03:01Z); legionreport.com (published
2026-11-23T02:52:26Z); Sports Illustrated; denversports.com; NBA on X
(November 23, 2026).
**Timezone note:** Sunday-night game in Chicago that went to overtime;
the final result was published ~02:52 UTC Monday 23 Nov. Monday story in
UTC.
**Figure notes (fix round):** Murray's overtime points are 8 per AP
(theScore / TSN / StatMuse: "scored eight of his season-high 45 points
in overtime"); Field Level Media says 6 — the AP figure is followed.
Hield's 33 is confirmed by AP, NBC Sports and the Sportradar box score
(13/19 FG, 7/13 3PT). The "highest-scoring game of the season" claim is
confirmed by pitchlabstats: the 296 combined points are the most in a
game of the 2026–27 season.

### 22. [EDGE] M5.4 quake shakes Peru's Andes as toll rises — South America
**Headline:** "M5.4 quake shakes Peru's Andes as toll rises"
**Account:** A magnitude 5.4 earthquake strikes near Carhuamayo, Peru, at
117.4 km depth on Sunday evening UTC (Monday in Asia-Pacific timezones),
in the same area as Friday's magnitude 6.7 quake — the strongest of four
aftershocks recorded so far within 63 km of the mainshock epicentre
(quakemate.app, USGS data). No
damage reported from the M5.4. Meanwhile Peru's civil defence institute
Indeci raises the toll from Friday's M6.7 quake: 1 dead, 15–16 injured
and more than 1,400 people displaced or otherwise affected across five
regions (Junín, Pasco, Huánuco, Lima and Callao); 152 homes
uninhabitable, 157 affected; power cut to nearly 93,000 people across
four regions (energy regulator Osinergmin). The M6.7 struck at 7:09 p.m. local time Friday (00:09 UTC
Saturday), 9 km NE of Carhuamayo at 108 km depth, and was felt in Lima
and Bogotá.
**Sources:** USGS via zenitmap.com (M5.4, Nov 22, 21:35 UTC) and
quakemate.app (4 aftershocks, strongest M5.4); Infobae via allatra.media
(published Nov 22, 8:35 PM EST = Nov 23, 01:35 UTC); El Comercio (Peru);
thetruepost.ca; travelandtourworld.com (Indeci Complementary Report No.
16257, 21 Nov 18:00); USGS via terremoto.developers.do (M5.4, 9 km N of
Carhuamayo, 117.4 km deep); watchers.news (23 Nov, COEN-INDECI Reporte
Complementario N.º 16277, 22 Nov 08:20 local, Report No. 10);
BusinessMirror/Bloomberg (22 Nov, Osinergmin: power cut to nearly
93,000); nomadlawyer.org (92,906 users disconnected).
**Timezone note (EDGE):** the M5.4 struck 21:35 UTC Sunday 22 Nov, which
is Monday 23 Nov in Asia-Pacific timezones (04:35 WIB); the Indeci toll
update was published Monday 23 Nov in UTC. Monday story under the "any
time zone" rule. The "aftershock" relationship is stated only as "in the
same area" for the M5.4 itself; USGS/quakemate do list it among the
sequence's aftershocks. Injured figure conflicts across sources (15 vs
16); the range is given.
**Figure notes (fix round):** aftershock counts vary by threshold and
radius — quakemate (USGS data) lists 4 aftershocks within 63 km of the
epicentre, strongest M5.4; zenitmap/USGS list 3 quakes M4.5+ within
150 km; IGP lists two milder aftershocks in Junín. The "four
aftershocks" figure is the quakemate/USGS 63 km count. The power cut
("nearly 93,000") is verified: Osinergmin via Bloomberg/BusinessMirror
and thetruepost.ca; 92,906 users per nomadlawyer/travelandtourworld.
Indeci reports: No. 16257 (21 Nov 18:00) was the earlier assessment
(1 dead, 16 injured); the toll figures used here (1 dead, 15 injured,
152 homes uninhabitable, 853 displaced + 628 affected = 1,481 people)
come from the later COEN-INDECI Reporte Complementario N.º 16277
(22 Nov 08:20 local, Report No. 10) per Watchers.

### 23. Brazil's lower house votes on Lula's fiscal package — South America
**Headline:** "Brazil's lower house votes on Lula's fiscal package"
**Account:** Brazil's Chamber of Deputies holds an extraordinary session
on Monday to debate and vote on President Lula's fiscal adjustment bill
(PLP 299/2026), after the Senate approved it last week. The package caps
real growth in public spending at 2% in years when the government must
impose a spending freeze and imposes a 10% across-the-board cut in
benefits granted to economic sectors, with an estimated R$45.1–50.1
billion positive impact on the 2027 primary result. Approval needs 257
votes. Rapporteur Mauro Benevides Filho says he will not change the
Senate text, so approval would send the bill straight to Lula for
sanction. The vote comes as the real slides — the commercial dollar
closed at R$5.9344 on 19 November, its highest since January 2025 — and
the central bank has sold $1 billion in a spot auction, its first since
December 2024.
**Sources:** macroherald.com; particle.news; todayinbrazil.com;
v3.news (Institutional Relations Minister José Guimarães, 18 Nov);
flamerzinho (257 votes); Primeira Análise (R$45.1–50.1bn);
investoffshore.com (real, central bank); contrapontobrasil.com.br
(23 Nov); lideswitzerland.ch (20 Nov clipping).
**Note — scheduled event:** the session is Monday (18:00 Brasília =
21:00 UTC), but some sources say the vote itself may run from Monday
night into Tuesday. At build time the session had not yet begun.
Framed as the vote/debate happening Monday; do NOT claim an outcome.
Cut-size conflict noted: a LIDE clipping says the linear cut in tax
benefits was raised from 10% to 20%; most sources say 10%. The page
prints neither figure.

### 25. COP31 failure a sign of 'difficult times', says Albanese — Oceania
**Headline:** "COP31 failure a sign of 'difficult times', says Albanese"
**Account:** Australian Prime Minister Anthony Albanese, on Monday,
attributes the failure of the COP31 climate talks in Antalya,
Turkey, to "difficult geopolitical times" and defends Climate Minister
Chris Bowen, who served as president of negotiations, from Coalition
calls for his resignation. "That is the reality. The important work of
Cop is the work that we've done with the Pacific," Albanese said. The
talks collapsed on Sunday after the EU and other nations rejected a draft
pact that made no explicit reference to fossil fuels; Bowen called the
outcome "very disappointing" and said "Australia left nothing on the
field". Coalition energy spokesperson Dan Tehan said Bowen should
"resign immediately" and called the outcome a "catastrophic diplomatic
disaster"; the Greens' deputy leader Steph Hodgins-May called it a
"disastrous embarrassment".
**Sources:** AFP (Sydney, Nov 23, 2026) via NAMPA; Guardian via
dailyfoxnews.com (published 2026-11-23T04:54:22Z); Helsinki Times;
zot.news.
**Note:** the collapse itself is Sunday news; Albanese's Monday reaction
is the Monday story, and the story attributes the quote to him.

### 28. New Zealand retail sales surge 2.2%, strongest in nearly five years — Oceania
**Headline:** "New Zealand retail sales surge 2.2%, strongest in nearly five years"
(Page index line shortened to "NZ retail sales surge 2.2%, best in
nearly five years" to fit one line.)
**Account:** New Zealand retail sales volumes jump 2.2%
quarter-on-quarter in Q3 2026, Stats NZ reports on Monday — far above
the 0.5% expected, reversing Q2's 0.5% contraction, and the strongest
quarterly increase since Q4 2021 (NZ$561m). Excluding motor vehicles,
sales rise 1.4% (vs 0.8% expected); retail sales values climb 2.4% to
NZ$33bn, with all 16 regions reporting higher values, led by Gisborne,
Nelson and Otago. Year-on-year, total volumes rise 3.5% (Econoday);
core spending (excluding fuel and motor vehicles) is 4.7% higher than a
year earlier (Westpac/Stats NZ). The New Zealand
dollar edges up to near US$0.5475 in early Asian trade after the data,
still near its lowest since March 2020.
**Sources:** Stats NZ via ActionForex (Nov 23); FXStreet (Nov 23);
Inside Retail NZ (23 Nov 2026); Newsquawk; JAFX (NZD/USD 0.5474, lowest
since March 2020); Econoday (23 Nov, YoY volumes 3.5%); b2bnews.co.nz /
europesays.com (23 Nov, Westpac: core spending +4.7% YoY).
**Note (fix round):** an earlier draft said "year-on-year, volumes rise
4.7%" — that 4.7% is the CORE (ex-fuel, ex-autos) year-on-year figure
(Westpac's Satish Ranchhod, quoting Stats NZ); total volumes are +3.5%
year-on-year per Econoday. Inside Retail NZ's "volumes rose 4.7 per
cent" year-on-year refers to the same core figure.
**Timezone note:** Stats NZ released the data at 10:45am Monday NZDT
(21:45 UTC Sunday). Monday 23 Nov in New Zealand, Australia and Asia.

### 29. Northland's first wind farm opens — Oceania
**Headline:** "Northland's first wind farm opens"
**Account:** Mercury cuts the ribbon on Northland's first wind farm, the
NZ$287 million Kaiwaikawe Wind Farm near Dargaville, on Monday. Its 12
turbines — 206-metre Vestas V162 machines, taller than any structure in
New Zealand bar Auckland's Sky Tower — will produce 77 megawatts (221
GWh a year), enough electricity to power about 27,000 homes. All 12
turbines are installed and electricity was first generated in July 2026;
Mercury plans full generation by the end of the 2026 calendar year, with
final commissioning, testing, site rehabilitation and removal of
construction facilities continuing into early 2027. The farm sits on Pāmu's
Ōmāmari farm, 12 km north-west of Dargaville, in partnership with mana
whenua Te Roroa.
**Sources:** RNZ (23 Nov 2026, 03:11 UTC) via monolith.news and
downundervoices.com; Mercury NZ; Wikipedia; Global Energy Monitor;
Mercury NZX announcement (full operation expected by end of 2026);
Mercury new-builds page ("We plan to reach full generation by the end
of the 2026 calendar year"); Mercury Kaiwaikawe project page (final
commissioning/testing/site rehabilitation into early 2027); Mercury Q3
2026 operational update (all 12 turbines online and generating since
July).
**Note (fix round):** Mercury's own statements cover two different
milestones — full generation by end of 2026 (NZX announcement,
new-builds page) and final commissioning/testing/site rehabilitation
into early 2027 (project page). Both are recorded here; neither
contradicts the other.

### 30. Former Silver Ferns captain Julie Carter dies aged 60 — Oceania
**Headline:** "Former Silver Ferns captain Julie Carter dies aged 60"
**Account:** Julie Carter, the former Silver Ferns captain, dies on
Monday 23 November, aged 60. A Waikato goal attack, Carter represented
New Zealand 50 times between 1988 and 1993, became the Silver Ferns'
16th captain in 1992, and led the team to 10 wins from 11 outings,
losing only once as captain. She played at the 1991 Netball World Cup.
Tributes describe her as "one of the great thinkers" of the game.
**Sources:** Wikipedia (27 November 1965 – 23 November 2026, citing
"Netball: Former Silver Ferns captain Julie Carter dies");
monolith.news NZ headlines (23 Nov 2026); Netball Waikato Bay of Plenty
player profile (50 caps, 16th captain, 10 wins from 11); Stuff,
"'Tough and uncompromising': Former Silver Ferns captain Julie Carter
dies, aged 60" (stuff.co.nz, 23 Nov 2026, crawled 02:29 UTC; aggregator
mirror collector.com.tr published 2026-11-23T04:36:06+03:00).
**Sourcing caveat:** the death date is confirmed by Wikipedia (citing
the NZ Herald obituary) and by Stuff's own obituary (see fix-round note
below), plus Netball WBOP for the career details; the NZ Herald obituary
text itself was not directly retrieved. Corroborated by three sources;
kept in the index only, not illustrated.
**Fix round (retrieval attempt, ~07:30 UTC):** a genuine attempt was
made to retrieve the NZ Herald obituary directly — three fresh searches
("Julie Carter Silver Ferns dies NZ Herald obituary",
"nzherald.co.nz 'Julie Carter' netball 'Silver Ferns' dies") plus
opening the Wikipedia page (reference 1 carries no URL) and the
collector.com.tr aggregator pages (which list the Herald headline but
link only to the Stuff article). No nzherald.co.nz URL surfaced and the
obituary text could not be retrieved. The attempt DID retrieve a second
independent NZ news source: Stuff's obituary, headlined "…dies, aged
60", published 23 Nov (title + publication timestamp + tribute summary
retrieved; the article body did not extract). Decision: KEEP index-only
— death date (23 Nov 2026) and age (60) are now corroborated by Stuff +
Wikipedia (citing the NZ Herald obituary) + Netball WBOP (DOB
27/11/1965, 50 caps, 16th captain). No evidence the date or age is
wrong was found anywhere.

### 31. Albanese runs biggest, best-paid PM's office in 13 years — Oceania
**Headline:** "Albanese runs biggest, best-paid PM's office in 13 years"
**Account:** A Centre for Public Integrity report released on Monday
finds Anthony Albanese has built the largest and best-paid prime
minister's office in 13 years: 59 political staff, three-quarters of
them senior (up from 61% when he took office, and under half under Tony
Abbott), with senior salaries of $156,510–$317,152 a year and a maximum
taxpayer bill of $12,155,410 before entitlements. The office had 51
staff at the 2022 election, peaked at 65 before the 2025 election, and
now stands at 59 — more than the entire federal crossbench's combined
allocation of extra staff, after Albanese cut crossbench support from an
average 2.6 extra staff per crossbencher to 1.4 (now 1.5). Albanese,
asked about the report at a Parliament House press conference on Monday,
said: "It's not the system that I created. It's one I inherited, and we
increased the staffing for every member of the House of Representatives
and the Senate."
**Sources:** AAP (published 2026-11-22T23:14:10Z = 10:14am AEDT Monday);
pm.gov.au press conference transcript (Parliament House, Canberra,
Monday); europesays.com / thebullpost.press (report detail);
startsat60.com.
**Timezone note:** AAP published 23:14 UTC Sunday = 10:14 AEDT Monday
23 Nov. Monday story in Australia.

---

## Dropped candidates (merged from all three research passes — investigated, rejected)

Each item's true first date is given. Republication on 23 Nov does not
make a story a Monday story.

**Sunday 22 Nov (or earlier) events, republished Monday:**
- COP31 collapse itself — Sunday 22 Nov (Antalya). Only Monday reactions
  used (#6 Reuters investigation, #25 Albanese).
- Russian drone strike on Kyiv supermarket, early figures (3 killed, 15
  wounded) — evening 22 Nov. Monday figures (2 killed, 8 wounded) used
  in #8. Zelensky's "165 missiles in a week" / Patriot appeal — Sunday.
- Verstappen wins Las Vegas GP — Saturday night 21 Nov Las Vegas (race
  ended ~06:00 UTC Sunday 22 Nov).
- India 720/9 declared — Sunday 22 Nov (Day 4). Used only as context
  for #26.
- El Chapo Isidro captured — Friday night 20 Nov, confirmed Sat 21 Nov.
- Indonesia candy-factory fire (Serang, Banten) — broke out Sat 21 Nov
  17:00 local; body-bag/missing toll updates Sunday 22 Nov. Monday
  "search resumes" is a follow-up, not a new event.
- South Korea Education Minister Choi Kyo-jin resigns — Sunday 22 Nov
  (Korea JoongAng Daily published 22 Nov 06:18 UTC; Reuters wire 23 Nov
  00:19 UTC is a republication).
- Sparta II Russian cargo ship on fire off Finland — struck Sat 21 Nov;
  still burning / towing began Sunday 22 Nov.
- Lisbon cost-of-living march — Saturday 21 Nov (Reuters).
- Wembanyama 50 points vs Pelicans — Saturday 21 Nov.
- Riemann hypothesis proof — claim Fri 20 Nov; Lean/Mathlib certification
  Sat 21 Nov 13:55 UTC; verification update Sun 22 Nov 16:10 UTC.
- St. Johns River record flood, Florida — record broken 19–21 Nov; Sunday
  22 Nov "still spreading". A crest near 13.1 ft was forecast for early
  Monday but no confirmed Monday reading was found.
- Tom Jackson dies — died Fri 20 Nov, announced Sun 22 Nov.
- ICE arrests at Seattle airport — Saturday 21 Nov.
- UK–Ukraine drone production deal — signed Sat 21 Nov in Kyiv.
- Wadkute (BJP MP) dies — late Sat 21 Nov, reported Sun 22 Nov.
- Rajasthan pilgrim crash (9 killed) — ~01:00 Sunday 22 Nov.
- UN lethal-autonomous-weapons talks — agreement Saturday 21 Nov (Geneva);
  MENAFN republication 23 Nov 00:52 GMT is not first reporting.
- Lewis Pugh Strait of Hormuz swim — swum 16–18 Nov, reported 21–22 Nov.
- Everest helicopter collision — 3 Nov 2026.
- Qingdao cargo-ship fire (25 dead) — 10 Sep 2026.
- Washington paper-mill disaster — 26 May 2026; $10.1M penalties Fri 20 Nov.
- Tinubu donates N250m to Bayelsa boat victims — announced SUNDAY 22 Nov
  by VP Shettima (thetrumpet.ng 2026-11-22T19:32Z). Punch's 23 Nov 01:04
  GMT item is a republication. The boat accident itself was Friday 20
  Nov; death toll 29 confirmed Sunday.
- AKA's father challenges 'one-sided' inquest — Tony Forbes challenged
  the investigating officer in the Cape Town Regional Court on Thursday
  19 Nov; the docket dispute dates to 20–21 Oct. TimesLIVE's 23 Nov
  02:30 GMT item recycles those proceedings.
- Egypt El Ayyat train collision (7 dead, 125 injured) — Sunday 8 Nov
  2026 (Wikipedia; Health Ministry toll 9 Nov 03:50 UTC).
- Netanyahu–Eisenkot coalition talks end without deal — Sunday 22 Nov
  (Al Jazeera published 22 Nov; 4-hour Herzliya meeting, joint
  statement, no date for follow-up).
- Basra Hartha power station fire (4 dead, 35 injured) — Saturday 21 Nov
  ~06:00 (Reuters 21 Nov; Al-Sabah safety-warning follow-up 22 Nov).
- Russell Brand sentenced to 10½ years — Monday 9 Nov 2026, Southwark
  Crown Court. Reports saying "sentenced on Monday" refer to 9 Nov.
- Beijing to bar young 'red-chip' firms from offshore listings — Reuters
  exclusive 20 Nov. TradingView's 22 Nov 23:10 UTC timestamp is a
  republication.
- Philippines deploys anti-ship missiles in Bolinao — first reported
  Sunday 22 Nov (Manila Times Sunday report; mirrors from 13:46 Sun UTC).
- Angola to pay $180m for 10% of De Beers — Endiama CEO disclosed Friday
  20 Nov (Reuters). Hold On Angola 23 Nov 01:04 GMT is a republication.
- Mozambique Rovuma River settling ponds (Lupilichi) — Jornal Notícias
  reported 22 Nov. Club of Mozambique 23 Nov 04:01 GMT is a
  republication/translation.
- EU–Indonesia IEU-CEPA trade pact signed — Saturday 21 Nov, Brussels.
- Vietnam high-speed rail consultancy contract (Systra-led, $397–416m) —
  announced Sunday 22 Nov. aseancoverage 23 Nov 07:24 is a
  republication. Figures also conflict ($397m VND-based vs $416m
  won-based).
- Indonesia–China $1.8B coal-to-ethanol partnership — Wednesday 18 Nov,
  Shenzhen.
- Ukraine's 1,336-drone night / ~600 drones at Moscow — overnight 15–16
  Nov (ABC News 16 Nov). The Nexus Europa 23 Nov digest is a roundup.
- Fela Kuti Rock & Roll Hall of Fame induction — ceremony Saturday 14 Nov,
  Peacock Theater, Los Angeles.
- France torpedoes EU budget draft ("very disappointing") — Saturday
  21 Nov (MENAFN republication 23 Nov 00:55 GMT).
- Kenya and DRC restore full diplomatic relations — agreement at the Oyo
  (Congo-Brazzaville) summit, Sunday 22 Nov (ADIAC 22 Nov 18:26 GMT).
- DRC South Kivu honey production halved (10t → 4–6t) — Monde des
  Abeilles report published Sunday 22 Nov. Only the provincial assembly's
  bee-edict examination is Monday (thin, not used).
- Russian ship explosion at Libya port (Benghazi) — 22 Nov (BBC;
  Benghazi government called for an investigation 22 Nov 20:15 GMT).
- South Sudan cattle camp attack, Tonj East (21 killed) — Eye Radio
  22 Nov 13:32 GMT.
- Sudan drone attacks kill five children (Khartoum/Omdurman) — Radio
  Dabanga 22 Nov 17:20 GMT.
- Zimbabwe preacher Urbert Angel arrested — 22 Nov (Nyasa Times 21:46 GMT).
- Kabila rebels shoot down fighter jet, capture pilot (DRC) — Taarifa
  22 Nov 16:48 GMT.
- Thailand plans chemical export halt over Myanmar mining pollution —
  22 Nov 16:11 (aseancoverage).
- Mount Ibu and Mount Semeru eruptions (Indonesia) — late Saturday /
  early Sunday (ANTARA).
- China rejects US telecom ban (FCC phone-number access) — commerce
  ministry statement Sunday 22 Nov.
- Gaza Tel al-Hawa food-vehicle strike (3 killed) — 21 Nov (tbsnews
  22 Nov 08:50: "struck a truck in Gaza yesterday (21 November)"). The
  axadletimes piece timestamped 23 Nov 00:30 CET is a late republication.
- AP Gaza roundup: "strikes kill eight, including a boy" — Sunday 22 Nov
  ("latest news from the Middle East on Sunday").
- Ukraine strikes on Kerch Bridge — 17 Nov (Nexus Europa 23 Nov digest
  is a roundup of the week's strikes).
- Berlin Coalition of the Willing summit — 19 Nov. Merz floats gradual
  Russia sanctions relief — 21 Nov. Zelenskyy names eight European
  peace-talk seats — 21 Nov.
- DAX −2.6% / STOXX worst week since March — Friday 20 Nov.
- Singapore–China CSFTA 4.0 launch — 20 Nov, Shenzhen (context for #3
  only).
- India: Amit Shah's ₹4,000 crore Arunachal push — Sunday 22 Nov.
- Modi IIT Patna AI centre inauguration — reported 22–23 Nov in
  school-assembly digests but no dated primary source found; not used
  (unverified date).
- Newspoll: Albanese net approval −31, Taylor leads as preferred PM
  42–41 — published Sunday night 22 Nov (Daily Mail 13:27 GMT 22 Nov).
- Brazil supercell storm, Tupanciretã (5 dead, 265 injured) — storm hit
  Saturday 21 Nov; death toll rose to 5 on Sunday 22 Nov. The "02:41 AM
  Mon Nov 23" item is a republication.
- Bolsonaro in ICU — hospitalised Friday 20 Nov; wife's "without pain"
  update Sunday 22 Nov.
- Flamengo win Brazilian title — Saturday 21 Nov (1–1 draw at Palmeiras).
- Boca Juniors win Copa Sudamericana; Paredes collapses in interview —
  Saturday 21 Nov, Barranquilla.
- Colombia FARC-dissident bombing (5 dead, Meta) — Saturday 21 Nov.
- Colombia bus crash, Huila (8 dead, 20 injured) — early Saturday 22 Nov.
- Colombia MinTIC asks X to suspend Gustavo Petro's account — request
  sent Sunday 22 Nov.
- Chile Chiloé crash (6 dead, incl. 4 children) — Sunday morning 22 Nov.
- 5th Circuit strikes down Pregnant Workers Fairness Act (9–8) — decision
  issued Friday 20 Nov; AP story updated 22 Nov 14:44 EST.
- Trump: "very hard" to work with Schumer as Senate majority leader —
  Truth Social post Sunday 22 Nov (Reuters Nov 22).
- Trump will work with Democrats on 10% credit-card cap — Fox News
  interview Saturday 21 Nov (CBS/AP Nov 21, 1:27 PM EST).
- FBI NCIC database breach — first reported Friday 20 Nov (CNN/Reuters
  Nov 20); Trump downplayed it Saturday 21 Nov.
- JPMorgan software-bug bank outage — Monday 16 Nov 2026. The "Nov 23"
  items are stale reposts.
- Delta weight-and-balance delays (2,000+ flights, ~58% delayed) —
  Sunday 22 Nov event (ground stop 07:46 ET Sunday; system restored
  Sunday evening ET). Dropped as a Sunday story (borderline).
- Kīlauea episode 57 — precursory overflows began 01:21 HST Sunday
  22 Nov; alert raised to WATCH/ORANGE Sunday. Fountaining forecast for
  22–26 Nov, most likely 23–25 Nov, but not started.
- CDC flu hospitalisations (11,734/week, highest since 2010–11) —
  FluView published Friday 20 Nov.
- Alabama natural gas pipeline fire, Ward (flames 100+ ft) — Saturday
  21 Nov ~11:30 PM CST; force majeure declared Sunday 22 Nov.
- Stockton birthday-party mass shooting (4 dead, 10 injured) —
  REPUBLICATION TRAP. Credible reports date the shooting to Saturday
  night 29 November 2025; the usdailypost.com item dated "November 23,
  2026" is a re-run of the old story. No credible source reports a NEW
  Stockton shooting on 22–23 Nov 2026.
- Alleged Russian agent stalking Palantir staff (Igor D'iu) — DOJ
  indictment announced Wednesday 18 Nov; Stanford Daily Nov 20. The ABC
  item dated Nov 23 is a repost.
- Cowboys fan Mario Narro dies after stadium fight — game Sunday 15 Nov
  (Week 10), died Wednesday 18 Nov, Jerry Jones spoke Friday 20 Nov.
- Farmlands chair Rob Hewett resigns — announced Sunday 22 Nov.
- Brazil Rockbridge Network probe — STF order 27 Oct; inquiry opening
  reported 10 Nov; Rio Times item 22 Nov.
- NZ election "too close to call", Joshua Wong sentencing, Indonesia VP
  resignation — 19–21 Nov.
- "Swimmer crosses Hormuz", "India–Pakistan cricket in Qatar", Centrica
  energy bills, Anupama snooker title — checked; either 21–22 Nov or
  unverifiable as Monday news; not used.

**Checked, not used (no Monday-verified development / too thin):**
- "6.1-magnitude earthquake, western Turkey, late Monday night"
  (newsinsights.org) — undated, no verifiable 23 Nov event; AFAD's
  23 Nov list shows only minor tremors (largest M1.7, Izmir Bay 00:06).
- Chile/Colombia/Peru unified stock market — no Monday-verified
  development found.
- NHL Sunday results — only game ending Monday UTC was Blackhawks 6–3 at
  Canucks plus Blues' 5–4 SO win over Oilers; neither had standout news
  value. Not used.
- Warriors 88–87 Celtics — Sunday-night game ending Monday UTC (~04:00
  UTC), but no standout narrative found; one NBA story (#21) is enough.
- Chile/Argentina storm warnings (SMN/INMET) — Monday weather warnings
  with no reported impacts; weaker than the cut king-tides item.
- Singapore social support thresholds raised / 2027 property tax rebates
  (BusinessToday, 23 Nov) — details not verified.
- Malaysia/Singapore HI Mobility Johor bus contract (RM665.68m, reported
  23 Nov 10:23) — not independently verified.
- South Korea stalker restraining orders / life without parole (Yonhap,
  23 Nov) — presidential office "considering"; thin, not used.
- Thailand Rukchanok lèse-majesté appeal decision due Monday — outcome
  unknown at research time; not used.
- DRC South Kivu bee-protection edict examination (Radio Okapi, 23 Nov)
  — thin; the honey-production figures come from a Sunday report.
- Nepal PM's arrival in Delhi — Sunday 22 Nov; only Monday's talks used
  (#2). Fit to Lead findings preview — Sunday 22 Nov (ABC); only
  Monday's launch used (#24).

## Figure cross-check (page vs these notes)

Every figure printed on the page was checked against this file at build
time; see test-report.md for the full check. Figures printed on the page:
KOSPI −5.41% intraday to 4,606.44; five-minute halt; Taiex −0.93%; ~10
trillion won stabilisation fund; $2 billion Nepal package (sought);
Dymer 9 of 12 dead; Opentil 32nd-minute goal, 1–0; 330 votes, 258 House
seats, most since 1992; $450M / $50M a year / nine years; 429 Brussels
flights; Purdy three first-half TD passes, 49ers 9–1; 71% / 97%; 43
overs; Meldrum 5:30am, aged 83; 37.3%; R3.1m; 27–24; 100–150%;
Murray 45 / Jokic 202nd; M5.4 / M4.2; 2.2%; 60; 13 years. No figure on
the page was invented, estimated or rounded beyond the source's wording.

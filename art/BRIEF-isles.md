# Brief: 35 island emblems

You are drawing original emblem illustrations for a junior-high social-studies learning page
(Traditional Chinese, Taiwan). Each "island" is a unit of study. The emblem appears on the
island's card (about 64 px), in its pop-up sheet (about 72 px) and in the island page header
(about 100 px). Draw everything yourself — do not trace or imitate any textbook, brand, logo,
flag or existing artwork.

## Output

Write exactly one file per island into the `isles/` folder: `isles/<subject>-<id>.svg`
(for example `isles/geo-map.svg`). Write nothing outside `isles/`. 35 files in total.

## Format (checked by `python check_svg.py isles`)

- `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120">` with no width/height.
- Allowed elements only: g path circle ellipse rect line polyline polygon defs marker title.
  No text, no gradients, no filters, no style, no script, no image, no href, no comments.
- Colours: every fill/stroke must be `none` or one of these CSS variables, so the art works in
  light and dark themes:
  - `var(--ic)` the island's own accent colour (main object — use it generously)
  - `var(--fig-ink)` outlines and dark details
  - `var(--fig-paper)` light highlights / white parts
  - `var(--fig-land)` grass and land, `var(--fig-sand)` beach and sand
  - `var(--fig-sea)` water, `var(--fig-deep)` deeper water / wave lines
  - `var(--fig-warm)` sun, fire, light, `var(--fig-cool)` sky, ice, snow
  - `var(--fig-soft)` secondary grey details, `var(--fig-line)` faint lines
- If you use an id, it must start with the file name (e.g. `geo-map-…`).
- Under 3.5 KB per file. Round the numbers in path data to at most 1 decimal.

## Style (keep all 35 consistent)

- Composition: a small island sitting on a sea of 2–3 gentle wave lines near the bottom
  (island base around y = 78–100), with ONE clear themed object standing on it, centred,
  roughly 50–64 units tall. Leave a 6-unit margin on every side.
- Flat, friendly, slightly chunky. Outlines in `var(--fig-ink)`, stroke-width 2.5,
  `stroke-linecap="round" stroke-linejoin="round"`. Few shapes; it must read at 48 px.
- The themed object is mainly `var(--ic)` with `var(--fig-paper)` highlights. Sea in
  `var(--fig-sea)`, island top in `var(--fig-land)` with a `var(--fig-sand)` rim.
- No words, letters, numbers, national flags, religious symbols, weapons aimed at people,
  or real people's faces. Simple stick/round figures are fine.
- Vary the island silhouette a little between files so they don't look copy-pasted.

## The islands and suggested motifs

| file | island (name — topic) | motif idea |
|---|---|---|
| geo-map | 位置・臺灣島 — latitude/longitude, maps | folded map with a grid + compass rose |
| geo-land | 地形・海岸島 — landforms, coasts | layered mountain peaks above a cliff coast |
| geo-climate | 氣候・水文島 — weather, climate, rivers | rain cloud over a winding river |
| geo-people | 人口・族群・農業島 — population, ethnic groups, farming | three round figures beside rice sprouts |
| geo-city | 工商・都市・區域島 — industry, trade, cities | small skyline + factory chimney with smoke |
| geo-china | 中國大地島 — China's land, climate, economy | terraced hillside with a long river |
| geo-neasia | 東北亞島 — Japan, Korean peninsula | snow-capped volcano cone + blossom branch |
| geo-seasia | 東南亞・南亞島 — monsoon, cultures | palm tree + monsoon cloud over paddies |
| geo-mideast | 西亞・北非島 — dry lands, oil | sand dunes + oil pump jack + strong sun |
| geo-africa | 漠南非洲島 — savanna, development | flat-topped acacia tree + sun on savanna |
| geo-europe | 歐洲・俄羅斯島 — Europe and Russia | windmill in front of alpine peaks |
| geo-america | 美洲島 — North and Latin America | desert mesa + corn stalk |
| geo-oceania | 大洋洲・兩極島 — Pacific islands, poles, climate change | iceberg with a penguin + small coral |
| geo-taiwan | 地名・農業食品島 — Taiwan place names, food | wooden signpost + rice bowl |
| his-prehist | 史前・大航海島 — archaeology, Age of Sail | three-masted sailing ship + clay pot |
| his-qing | 清帝國臺灣島 — Qing rule, ports, settlers | curved temple roof + tea leaves |
| his-japan | 日治臺灣島 — colonial rule, modern building | steam locomotive + sugar-mill chimney |
| his-postwar | 戰後臺灣島 — democratisation, economy | ballot box + container ship |
| his-ancient | 商周到宋元島 — ancient China | bronze tripod cauldron (ding) + scroll |
| his-modern | 明清與近代東亞島 — tribute trade, Western impact | sailing junk + steamship smoke |
| his-republic | 民國初年島 — early Republic, new culture | open book + paper lantern |
| his-eastasia | 戰爭與當代東亞島 — war and Cold War East Asia | dove flying over a cracked wall |
| his-classic | 古文明與宗教島 — ancient civilisations | pyramid + Greek column |
| his-earlymod | 近代歐洲島 — Renaissance, revolutions | printing press or telescope + caravel |
| his-worldwar | 革命與大戰島 — revolutions, world wars | old helmet resting under an olive branch |
| civ-rights | 公民・人權島 — civic virtue, human dignity | raised open hand holding a heart |
| civ-family | 家庭・校園・部落島 — family, school, tribe | house with three round figures |
| civ-culture | 文化・規範・團體島 — culture, norms, groups | linked hands of different colours (use --ic, --fig-warm, --fig-cool) |
| civ-justice | 輿論・正義・社福島 — public opinion, fairness | balance scale + speech bubble |
| civ-demo | 憲政・政府・參政島 — constitution, government | columned hall + ballot box |
| civ-law | 契約・民事・刑法島 — contracts, civil and criminal law | signed paper with pen + gavel |
| civ-rescue | 訴訟・行政・兒少島 — lawsuits, child protection | shield protecting a small figure |
| civ-market | 消費・生產・市場島 — consumption, markets | market stall with awning + coins |
| civ-trade | 貿易・貨幣・勞動島 — trade, currency, work | cargo crate + stacked coins |
| civ-global | 科技・全球・國際島 — technology, globalisation | globe with an orbiting satellite |

## Finish

Run `python check_svg.py isles` and fix every FAIL until all 35 pass. In your final message,
list the files and any motif you changed and why.

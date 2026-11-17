# Brief: 27 teaching diagrams (grade 7, first semester)

You are drawing original explanatory diagrams for a junior-high social-studies learning page
(Traditional Chinese, Taiwan). Each diagram sits inside a lesson card, above the key points,
and is read on phones (about 340 px wide) and desktops (up to about 640 px wide). Draw
everything yourself as clean schematic diagrams — do not trace or imitate any textbook figure.
Accuracy matters more than decoration: these are for 12-year-olds studying for exams.

## Output

Write exactly one file per diagram into `figs/`: `figs/<id>.svg` (e.g. `figs/geo-latlon.svg`).
Write nothing outside `figs/`. 27 files in total, ids listed below.

## Format (checked by `python check_svg.py figs`)

- `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 H" role="img">` where H is
  between 140 and 280 (pick what the content needs). No width/height on the root.
- First child: `<title>` with one plain sentence describing the diagram in Traditional Chinese.
- Allowed elements only: g path circle ellipse rect line polyline polygon text tspan title
  defs marker. No gradients, filters, style, script, image, href or comments.
- Colours: every fill/stroke is `none` or one of these CSS variables (they switch for dark mode):
  - `var(--fig-ink)` all text, outlines and arrows
  - `var(--fig-soft)` secondary text, axis ticks, dashed guide lines
  - `var(--fig-line)` faint grid lines and panel borders
  - `var(--fig-paper)` panel/background fills that must contrast with ink
  - `var(--ic)` the highlight colour for the one thing the diagram is about
  - `var(--fig-sea)` water, `var(--fig-deep)` deep water / groundwater
  - `var(--fig-land)` land and plains, `var(--fig-sand)` sand, dry ground, mountain shading
  - `var(--fig-warm)` sun, heat, warm air, tropics; `var(--fig-cool)` cold air, ice, sky, cold zones
- Text: use `<text>` with `font-size` 11 to 14 (labels 12–13, panel titles 13–14), and
  `fill="var(--fig-ink)"` or `var(--fig-soft)`. Do not set font-family. Use `text-anchor` for
  alignment. Text must stay inside the viewBox and must not overlap other text. Budget about
  1 em per Chinese character (13 px wide at size 13). Prefer putting labels in clear space
  with a short leader line rather than on top of shapes. No transform on `<text>`; groups may
  use `translate()` only.
- Arrows: a `<marker>` inside `<defs>` is fine; its id must start with the file name
  (e.g. `geo-rain-arr`). Every id in a file must start with the file name.
- Under 9 KB per file; round path numbers to at most 1 decimal.
- Use the exact label wording given below (Traditional Chinese). You may shorten only where
  marked "(may shorten)". Never add facts, numbers or place names that are not listed.
- Where a diagram is schematic (not to scale), include the small soft-grey note `示意圖` in a
  corner as listed.

## Visual style

Calm and readable: thin ink outlines (1.5), soft fills, generous white space, at most one
`var(--ic)` highlight per panel. Multi-panel diagrams: equal-width panels separated by
`var(--fig-line)`, each with a short title at the top. Keep everything left-to-right readable.

## The 27 diagrams

### Geography 地理

1. **geo-pos** — two panels. Left title `相對位置`: a station icon labelled `車站` in the
   middle, a small compass (`北` up), and a school icon up-right labelled `學校`, joined by a
   dashed arrow labelled `東北方 500 公尺`. Right title `絕對位置`: a 4×4 seat grid; rows
   labelled `第1排`…`第4排` down the left side, columns `1`…`4` along the top; the cell at
   row 3, column 2 filled with `var(--ic)`; caption under the grid `第 3 排第 2 個`.

2. **geo-latlon** — a globe (circle) seen from the front with the prime meridian in the centre.
   Draw a vertical axis line sticking out at top and bottom labelled `地軸`, with `北極` at the
   top and `南極` at the bottom. Latitude lines are straight horizontal chords (equator
   highlighted in `var(--ic)`, labelled `赤道 0°` outside the globe on the right). Meridians are
   half-ellipses from pole to pole; the centre one highlighted and labelled `本初經線 0°` near the
   bottom. Short labels: `北緯 N` above the equator, `南緯 S` below it, `西經 W` left of the
   prime meridian, `東經 E` right of it. A curved arrow across the front pointing right
   (west → east) labelled `自轉`.

3. **geo-zones** — Earth circle (radius about 80) with sunlight arrows coming from the left
   (`var(--fig-warm)`), labelled `陽光`. Horizontal lines at the correct heights
   (y = centre − R·sin(latitude)): 66.5°N, 23.5°N, 0°, 23.5°S, 66.5°S. Fill the bands:
   between the tropics `var(--fig-warm)`, between tropic and polar circle `var(--fig-land)`,
   beyond the polar circles `var(--fig-cool)`. Right-side labels with leader lines:
   `北極圈 66.5°N`, `北回歸線 23.5°N`, `赤道 0°`, `南回歸線 23.5°S`, `南極圈 66.5°S`; and zone
   names placed inside or just left of the bands: `寒帶`, `溫帶`, `熱帶`, `溫帶`, `寒帶`.

4. **geo-mapparts** — a small fictional town map in a rounded rectangle: a river, a road,
   a school symbol (flag on a square), a park symbol (tree). On the map: a title strip at the top
   reading `河濱小鎮地圖`; a legend box in a corner with three rows: square-flag `學校`,
   tree `公園`, double line `道路`; a north arrow with `N`; a scale bar marked `0` and `500 公尺`.
   Outside the map, four callout labels with leader lines pointing to each part:
   `圖名`, `圖例`, `方向標`, `比例尺`.

5. **geo-landsea** — left: a donut chart split 71% (`var(--fig-sea)`) / 29% (`var(--fig-land)`)
   with labels `海洋 71%` and `陸地 29%`. Right title `七大洲（面積由大到小）`: seven
   horizontal bars, longest first, relative lengths 100, 68, 54, 46, 32, 23, 19, labelled in this
   order: `亞洲`, `非洲`, `北美洲`, `中南美洲`, `南極洲`, `歐洲`, `大洋洲`. No numbers on the bars.

6. **geo-twpos** — schematic, note `示意圖`. A large land mass on the left labelled `亞洲大陸`;
   open water on the right labelled `太平洋`. A curved chain of islands running from the top
   (labelled `東北亞`) down past a highlighted island in the middle labelled `臺灣` to the bottom
   (labelled `東南亞`). A dashed horizontal line through Taiwan labelled `北回歸線`. Two curved
   arrows alongside the chain (one going down, one going up) labelled `候鳥南北遷徙`.

7. **geo-sea** — schematic, note `示意圖（未依比例）`. A horizontal strip: land on the left
   (`陸地`), a vertical line at the coast labelled `領海基線`, then a band labelled
   `領海` with sub-label `視同領土`, then a wider band labelled `經濟海域` with sub-label
   `漁業、礦產權利`, then open water labelled `公海`. Below, a distance ruler with ticks `0`,
   `12 浬`, `200 浬` lined up with the band edges.

8. **geo-landforms** — one landscape cross-section from left to right ending in the sea:
   a high flat-topped block `高原`, steep jagged peaks `山地` (sub-label `多高於 1,000 公尺`),
   low rounded hills `丘陵`, a flat-topped step with steep edges `台地`, a dip between two rises
   `盆地`, flat low ground `平原`, then sea. One label above each landform, no overlaps.

9. **geo-contour** — two panels. Left title `等高線圖`: a hill made of 4 closed contour lines
   labelled `100`, `200`, `300`, `400` (top at the centre, small triangle summit). The lines are
   crowded on the right side (label `線密：坡陡`) and spread out on the left (label
   `線疏：坡緩`). On the lower side, the contours bend into a V whose tip points UP toward the
   summit, with a small river line running down through it: label `河谷`. On the upper-left,
   the contours bend into a V whose tip points DOWN away from the summit: label `山脊`.
   Right title `地形剖面`: the matching side profile — gentle slope on the left, steep on the
   right — with height ticks 100–400.

10. **geo-coasts** — 2×2 panels with titles `沙岸`, `岩岸`, `珊瑚礁海岸`, `斷層海岸`.
    沙岸: straight shoreline, a long sand bar offshore enclosing a lagoon — labels `沙洲`, `潟湖`.
    岩岸: jagged coast of headlands and bays — labels `岬角`, `海灣`.
    珊瑚礁海岸: shallow clear water with coral shapes along a shore — label `溫暖清澈的淺海`.
    斷層海岸: side view of a tall straight cliff dropping into deep water — labels `懸崖`, `近岸水深`.

11. **geo-islands** — three panels titled `大陸島`, `火山島`, `珊瑚礁島`.
    大陸島: side view of hills and valleys; a dashed line labelled `海平面上升` higher than the
    old sea level; valleys under water, hilltops sticking out. Example label `金門、馬祖`.
    火山島: a volcano cone rising from the sea floor above the water. Example `澎湖、綠島、蘭嶼`.
    珊瑚礁島: a low flat island sitting on a coral reef. Example `小琉球、東沙島`.

12. **geo-rain** — three panels titled `地形雨`, `對流雨`, `鋒面雨`.
    地形雨: wind arrow from the sea on the left pushing moist air up the left slope of a
    mountain; cloud and rain on the left slope labelled `迎風坡多雨`; dry right slope labelled
    `背風坡少雨`.
    對流雨: sun heating the ground, warm air rising straight up (vertical arrows), a tall cloud
    with heavy rain; label `夏季午後雷陣雨`.
    鋒面雨: a wedge of cold air (`冷氣團`, `var(--fig-cool)`) under warm air (`暖氣團`,
    `var(--fig-warm)`) which slides up along the sloping boundary labelled `鋒面`; a long cloud and
    rain band; label `例：梅雨`.

13. **geo-monsoon** — schematic, note `示意圖`. Two panels titled `冬季：東北季風` and
    `夏季：西南季風`. Each shows the same simple elongated island (long axis tilted slightly from
    lower-left to upper-right, like a leaf) with a ridge line down the middle, north arrow `N`.
    Winter: several arrows coming from the upper-right (north-east); rain marks on the
    north-east coast with label `迎風多雨`; label on the south-west side `背風較乾`.
    Summer: arrows coming from the lower-left (south-west); rain marks on the south-west side
    with label `迎風多雨`.

14. **geo-watercycle** — sun at top-left, sea at bottom-left, land with a mountain and a tree
    on the right, a cloud in the middle. Arrows with labels: `蒸發` (sea → up), `蒸散`
    (tree → up), `凝結` (at the cloud), `降水` (cloud → mountain), `地表逕流` (along the ground
    surface down to the sea), `地下逕流` (dashed, below the ground surface, toward the sea).

15. **geo-basin** — map view, note `示意圖`. Two neighbouring river systems flowing down to a
    coastline at the bottom, each with a main stream and 2–3 tributaries. A dashed line along the
    high ground between them labelled `分水嶺`. One whole river system's area lightly shaded with
    `var(--ic)` and labelled `流域`. A dot on one river with the area upstream of the dot outlined
    and labelled `集水區`. Labels `主流`, `支流`, `河口`.

16. **geo-groundwater** — side view: sea on the left, land on the right with a groundwater layer
    (`var(--fig-deep)`). A well with a pump on the land drawing water up, label `超抽地下水`.
    Around the well the ground surface dips with small down arrows, label `地層下陷`.
    Salt water pushing in from the sea under the land with an arrow, label `海水倒灌`.
    On the far right a small wetland with rain arrows soaking into the ground, label
    `保留溼地：雨水滲入，涵養地下水` (may shorten to `溼地涵養地下水`).

### History 歷史

17. **his-periods** — a horizontal timeline of Taiwan's history, left to right, as coloured
    segments: `史前時代`, `大航海時代`, `清帝國時期`, `日治時期`, `中華民國在臺灣時期`
    (may shorten to `中華民國時期`). Ticks below the boundaries: `1624`, `1684`, `1895`, `1945`.
    Inside 清帝國時期 a thin divider at `1860` with tiny labels `開港前` / `開港後`. Above the
    line, two brackets: `史前時代（沒有文字紀錄）` over the first segment and `歷史時代` over
    all the rest. The prehistoric segment is compressed — mark it with a small `≈` break.

18. **his-prehist** — a time axis "years ago" running left (older) to right (recent), with an
    axis break between 50,000 and 10,000. Tick labels: `距今 50,000 年`, `7,000`, `5,000`,
    `2,000`, `400`. Three bars: `舊石器時代` from 50,000 to 5,000; `新石器時代` from 7,000 to 2,000
    (overlapping the end of the first bar); `金屬器時代` from 2,000 to 400. Under each bar its
    cultures: `長濱文化` / `大坌坑・圓山・卑南文化` / `十三行文化`, and its tool: `打製石器` /
    `磨製石器・陶器` / `鐵器`.

19. **his-1624** — timeline from 1620 to 1690 with three coloured spans and event ticks.
    Spans: `荷蘭 1624–1662`, `西班牙 1626–1642` (northern Taiwan, a separate lane), `鄭氏 1662–1683`.
    Events (short labels, alternate above/below to avoid overlap): `1624 荷蘭占南部`,
    `1626 西班牙占北部`, `1642 荷蘭逐出西班牙`, `1662 荷蘭退出`, `1683 施琅攻臺`,
    `1684 清帝國統治`.

20. **his-admin** — five steps left to right (or a 2-row zigzag if needed), each a small card
    with year, name and reason, connected by arrows:
    `1684` `一府三縣` `納入版圖`; `1727` `一府四縣二廳` `朱一貴事件後`;
    `1812` `一府四縣三廳` `增設噶瑪蘭廳`; `1875` `二府八縣四廳` `沈葆楨・增臺北府`;
    `1885` `臺灣建省` `劉銘傳・後為三府一直隸州` (may shorten to `劉銘傳任巡撫`).

21. **his-exports** — a three-row flow table titled `開港後的三大出口品`. Each row: product
    chip → origin → export port → destination, joined by arrows.
    `茶` → `北部` → `大稻埕加工・淡水出口` → `美國、東南亞`;
    `糖` → `南部` → `安平、打狗` → `日本`;
    `樟腦` → `中北部` → `淡水` → `歐美`.

22. **his-gods** — three columns, each a small temple-roof icon over two lines:
    `泉州人` / `清水祖師`; `漳州人` / `開漳聖王`; `潮州（客家）人` / `三山國王`.
    Below, one wide band spanning all three: `共同信仰：媽祖、王爺、土地公`.

### Civics 公民

23. **civ-nationality** — a central box `取得國籍的方式` with three branches, each a card with
    title, rule and example:
    `血統主義（屬人）` / `父或母是本國人` / `我國、多數歐洲國家`;
    `出生地主義（屬地）` / `在該國領土出生` / `美國`;
    `歸化` / `婚姻、收養、投資移民` / `例：新住民`.

24. **civ-gender-laws** — top row: a three-step chain with arrows
    `刻板印象` (sub `固定的看法`) → `偏見` (sub `負面的態度`) → `歧視` (sub `不公平的對待`).
    Bottom row title `性平三法`: three cards
    `性別平等教育法` / `校園事件・性平會調查`;
    `性別平等工作法` / `職場事件・禁止同工不同酬`;
    `性騷擾防治法` / `其他場合的性騷擾`.

25. **civ-family-types** — three panels titled `小家庭（核心）`, `折衷家庭（主幹）`,
    `大家庭（擴展）`. Use round head + body figures connected by lines like a small family tree.
    小家庭: two parents and two children (2 generations).
    折衷家庭: two grandparents above, two parents, two children (3 generations, one line).
    大家庭: two grandparents above two married couples (siblings and their spouses), each couple
    with one or two children. Captions: `夫妻＋未婚子女`, `三代同堂`, `幾個小家庭同住`.

26. **civ-aging** — a horizontal bar from 0% to 25% labelled `65 歲以上人口比例`. Threshold
    markers at 7%, 14%, 20% with labels `高齡化社會 7%`, `高齡社會 14%`, `超高齡社會 20%`
    (stagger them so they don't overlap). The segment beyond 20% filled with `var(--ic)` and a
    pointer label `我國 2025 年進入超高齡社會`.

27. **his-eras** — calendar systems, four small cards in a row or 2×2:
    `西元紀年` / `10 年＝一個年代` / `100 年＝一世紀`;
    `帝王紀年` / `用年號` / `光緒 10 年＝1884 年`;
    `民國紀年` / `1912 年＝民國元年` / `民國年＋1911＝西元年`;
    `干支紀年` / `10 天干配 12 地支` / `60 年一循環`.

## Finish

Run `python check_svg.py figs` and fix every FAIL until all 27 pass. Then re-read each brief
item and check every label and fact against it once more. In your final message list the files
and anything you could not draw exactly as described.

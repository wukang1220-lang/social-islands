# Brief: 23 more teaching diagrams (grade 8, first semester)

Same project, same rules as `BRIEF-figs.md` — read its **Format** and **Visual style** sections
and follow them exactly (viewBox 360 wide, height 140–280, `<title>` first, only the listed
elements, only `var(--fig-*)` / `var(--ic)` colours, ids prefixed with the file name, text
11–14 px with no overlap, under 9 KB, `示意圖` note where marked). The 50 existing files in
`figs/` are finished and approved: do not modify or delete any of them.

Important lessons from the last review — please follow:
- Never put dark text on a `var(--ic)` fill (it can be a dark colour). Use `var(--ic)` for
  outlines, small markers or bars without text; put text on `var(--fig-paper)` or light fills.
- Timelines: give every label its own clear space; no leader line may cross any text. Prefer a
  vertical list layout when there are more than 6 events.
- Keep charts geometrically consistent (bar lengths proportional to the numbers given).

Write exactly these 23 new files into `figs/`. Use the exact label wording given; never add facts,
numbers or names that are not listed.

### Geography 地理（中國、東北亞）

1. **geo-cnsteps** — note `示意圖`. A west→east terrain profile of China descending in three steps,
   left `西` right `東`. Step labels above each part: `高階梯`, `中階梯`, `低階梯`. Sub-labels:
   高 — `山地、高原` and `4,000 公尺以上`, example `青藏高原`; 中 — `高原、盆地` and
   `2,000 公尺以下`, examples `內蒙古高原・黃土高原・四川盆地`; 低 — `平原、丘陵`, example
   `長江三角洲`. A wavy arrow along the top labelled `河川由西向東流`.
2. **geo-cnmonsoon** — note `示意圖`. Two panels `冬季` and `夏季`. Each: a simple rounded block
   for the land with sea on the east and south sides (labelled `海洋` once), and a dashed
   horizontal line across the middle of the land labelled `秦嶺—淮河`. Winter: north half arrow
   from upper-left labelled `西北風`, south half arrow from upper-right labelled `東北風`, label
   `陸地 → 海洋`. Summer: north half arrow from lower-right labelled `東南風`, south half arrow from
   lower-left labelled `西南風`, label `海洋 → 陸地`.
3. **geo-cnclimate** — a decision flowchart titled `中國氣候怎麼判斷`. Start box `高地（如青藏高原）？`
   → yes: `高地氣候`. No → `年降水量` splits three ways: `＜250 毫米` → `溫帶沙漠`; `250～500 毫米`
   → `溫帶草原`; `＞500 毫米` → `最冷月均溫` splits: `＜0°C` → `溫帶季風`; `0～18°C` → `副熱帶季風`;
   `＞18°C` → `熱帶季風`. Group the two dry results under a small tag `乾燥氣候（距海遠近）` and the
   three monsoon results under `季風氣候（緯度）`.
4. **geo-cnfarm** — note `示意圖`. A rectangle for China divided by a vertical dashed line labelled
   `年降水量 500 毫米` into a west part `畜牧為主` (two items: `新疆：游牧`, `青藏高原：山牧季移`)
   and an east part `農業為主`. The east part is split by a horizontal dashed line labelled
   `秦嶺—淮河` into north `旱田：小麥、高粱` and south `水田：水稻`. A small tag in the west part:
   `綠洲、河谷可種植`.
5. **geo-huline** — note `示意圖`. A rectangle for China with a diagonal line from top-right
   (label `黑河`) to bottom-left (label `騰衝`). West side shaded light with `人口稀少`,
   `高山、乾燥少雨`; east side shaded `var(--ic)` lightly (low opacity, text stays readable on
   `var(--fig-paper)` boxes) with `約 94% 人口`, `地形平坦、雨量較多`.
6. **geo-cnregions** — four cards in a 2×2 grid: `東部率先發展` / `最早開放、交通便利、工商業最發達`;
   `中部崛起` / `煤、糧食與低廉工資，連結東西的樞紐`; `東北振興` / `傳統重工業區，礦產枯竭、設備老舊`;
   `西部開發` / `資源豐富但交通不便，能源輸往東部`. Title `中國四大經濟區`.
7. **geo-beltroad** — note `示意圖`. Simple nodes, no map outlines: `中國` on the right, `歐洲` on the
   left. Upper route labelled `一帶：陸上絲路` passing `中國西部` → `中亞` → `歐洲`. Lower route labelled
   `一路：海上絲路` passing `東南亞` → `南亞` → `非洲` → `歐洲`. Below, two small boxes:
   `目的：能源、消化產能、擴大市場` and `挑戰：債務、主權糾紛`.
8. **geo-koreas** — a two-column comparison `北韓` vs `南韓` with rows: `政治` — `獨裁` / `民主`;
   `產業` — `重工業、國防工業` / `高科技、娛樂影視`; `困境` — `經濟制裁、民生物資缺乏` /
   `依賴大型財閥，風險集中`. Bottom band across both: `長期對峙是半島發展的威脅`.
9. **geo-japanshift** — a flow: left box `問題` with `薪資高漲・成本增加` and `人口老化・勞力不足`;
   two arrows to the right: upper box `國外` with `勞力密集產業移往中國、東南亞` and `企業國際化`;
   lower box `國內` with `技術研發、專利獲利` and `高齡照護科技`.

### History 歷史（中國與東亞）

10. **his-zhou** — a five-level pyramid (top to bottom): `天子`, `諸侯`, `卿大夫`, `士`, `庶人`.
    A bracket on the right covering the top four labelled `貴族（宗法世襲）`. A note under:
    `禮樂：規範各階級的器物與儀式`.
11. **his-selection** — three cards left→right with arrows: `漢` / `察舉・太學` / `推舉孝子廉吏`;
    `魏晉南北朝` / `九品官人之法` / `上品無寒門，下品無世族`; `隋唐以後` / `科舉` /
    `考試取士，沿用到清末`. Small tag under the middle card: `世族勢力壯大`.
12. **his-songyuan** — a vertical timeline (dot + year + text): `947 契丹建遼`, `960 北宋建立`,
    `1005 澶淵之盟`, `1115 女真建金`, `1127 靖康之禍，南宋建立`, `1206 鐵木真建蒙古國`,
    `1271 忽必烈定國號為元`, `1279 元滅南宋`.
13. **his-yuanclass** — four stacked horizontal steps from top: `蒙古人`, `色目人`, `漢人`, `南人`, with a
    downward arrow on the side labelled `地位由高到低`. Notes: top two bracket `享有較多特權`,
    bottom two bracket `受到不平等待遇`.
14. **his-silver** — note `示意圖`. A loop: `美洲白銀` → `歐洲商人` → `中國` (with `購買絲綢、瓷器`)
    → `轉賣世界各地` → back. A separate arrow from `美洲` to `中國` labelled
    `玉米、番薯、馬鈴薯傳入`. A tag at `中國`: `白銀與銅錢並用`.
15. **his-reforms** — comparison table, columns `自強運動` / `明治維新`; rows: `推動者` —
    `奕訢、曾國藩、李鴻章` / `明治天皇與官員`; `政治` — `設總理各國事務衙門` / `君主立憲、頒布憲法`;
    `性質` — `著重器物層面` / `制度、器物、文化全面改革`; `成效` — `成效不彰` / `亞洲第一個現代化國家`.
16. **his-qingwars** — a vertical list of five rows, each `戰爭 → 結果 → 清廷回應`:
    `鴉片戰爭` → `南京條約` → `無意改革`; `英法聯軍` → `增開通商口岸` → `自強運動`;
    `甲午戰爭` → `馬關條約` → `戊戌變法`; `八國聯軍` → `辛丑和約` → `庚子後新政`;
    `日俄戰爭` → `輿論要求改革` → `立憲運動`.

### Civics 公民（八上）

17. **civ-state4** — centre circle `國家`, four cards around: `人民` / `具有國籍的國民`; `領土` /
    `領陸・領海・領空`; `政府` / `行使公權力`; `主權` / `對內最高・對外獨立`.
18. **civ-lawpyramid** — a three-tier pyramid: top `憲法` (side note `制憲國民大會制定・最高性`),
    middle `法律` (side note `立法院三讀、總統公布・法、律、條例、通則`), bottom `命令`
    (side note `行政機關依授權訂定・規程、規則、細則、辦法等`). An arrow down the left labelled
    `位階由高到低`. Footnote: `下位階不得牴觸上位階`.
19. **civ-rights4** — four cards: `平等權` / `法律上一律平等`; `自由權` / `防止國家不當干涉`;
    `受益權` / `要求國家有所作為`（`請願・訴願・訴訟`）; `參政權` / `選舉・罷免・創制・複決`.
20. **civ-fiveyuan** — an org chart: top `總統（人民直選）`. Below in a row the five branches:
    `行政院`, `立法院`, `司法院`, `考試院`, `監察院`, each with one short duty: `執行政策`,
    `制定法律・監督行政`, `審判・憲法法庭`, `考選・銓敘`, `彈劾・糾舉・審計`.
    Arrows/labels: `總統任命院長` to 行政院; `立法委員民選` at 立法院; one bracket over 司法院,
    考試院, 監察院 labelled `總統提名、立法院同意`; a curved arrow 行政院 → 立法院 labelled `對立法院負責`.
21. **civ-local** — a table with columns `層級`, `行政機關`, `立法機關`; rows:
    `直轄市` / `直轄市政府` / `直轄市議會`; `縣（市）` / `縣（市）政府` / `縣（市）議會`;
    `鄉（鎮、市）` / `鄉（鎮、市）公所` / `鄉（鎮、市）民代表會`; `直轄市山地原住民區` / `區公所` /
    `區民代表會`. Title `地方自治團體（行政權＋立法權）`.
22. **civ-ballot** — four cards with simple icons: `普通` / `符合資格人人可投`; `平等` /
    `一人一票，票票等值`; `直接` / `親自投票，不能代投`; `無記名` / `秘密投票，不受威脅`.
23. **civ-referendum** — a flow left→right: `提案` → `連署` → `公告` → `投票`, then two branches:
    `通過` → `政府依決議執行`; `不通過` → `2 年內不得再提`. Under 投票 a note box:
    `門檻：同意票＞不同意票，且同意票 ≥ 投票權人總數 1/4`.

## Finish

Run `python check_svg.py figs` until all 73 files pass (50 old + 23 new). Re-check every label
against this brief. In your final message list the 23 new files and anything you could not draw
exactly as described.

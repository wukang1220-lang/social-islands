# Brief: 30 more teaching diagrams (grade 9, first semester)

Same project, same rules as `BRIEF-figs.md` — read its **Format** and **Visual style** sections
and follow them exactly (viewBox 360 wide, height 140–280, `<title>` first, only the listed
elements, only `var(--fig-*)` / `var(--ic)` colours, ids prefixed with the file name, text
11–14 px with no overlap, under 9 KB, `示意圖` note where marked). The 103 existing files in
`figs/` are finished and approved: do not modify or delete any of them.

Lessons from earlier reviews — please follow:
- Never put dark text on a `var(--ic)` fill (it can be a dark colour). Use `var(--ic)` for
  outlines, small markers or bars without text; put text on `var(--fig-paper)` or light fills
  (`--fig-sea`, `--fig-land`, `--fig-sand`, `--fig-warm`, `--fig-cool`).
- Two neighbouring fills that mean different things must be clearly different colours
  (for example `--fig-cool` next to `--fig-deep`, not `--fig-cool` next to `--fig-sea`).
- Timelines: give every label its own clear space; no leader line may cross any text. Use a
  vertical list layout (dot + date + text) when there are more than 6 events.
- Keep charts geometrically consistent (bar lengths proportional to the numbers given).
- Pictures must read as what they are. When unsure, use a simple labelled box instead of a
  doubtful icon. No real-world map outlines: use simple rounded blobs or boxes for places.
- Phones show these at about 340 px wide, so prefer two columns over four, and short lines.

Use the exact label wording given; never add facts, numbers, years or names that are not listed.
`・` separates short items on one line. Where a line is long, break it into two `<text>` lines.

### Geography 地理（歐洲、俄羅斯、美洲、大洋洲、兩極）

1. **geo-glacier** — note `示意圖`. Top row, two valley cross-sections side by side:
   a V-shaped valley labelled `河流侵蝕：V 型谷` and a wide round-bottomed valley labelled
   `冰河侵蝕：U 型谷`. Bottom row, two small scenes: a U-shaped valley whose bottom is filled
   with sea water (`var(--fig-sea)`), labelled `海水灌入 U 型谷：峽灣`; and a hollow in rock
   holding water, labelled `低窪處積水：冰蝕湖`. Heading `冰河地形`.
2. **geo-euclimate** — note `示意圖`. No map. A large rounded block for Europe. From the left
   edge: a thick arrow labelled `西風` and a curved arrow along the left coast labelled
   `北大西洋暖流`. Inside the block, left to right: `溫帶海洋性` (sub `西歐・北歐西部`) and
   `溫帶大陸性` (sub `東歐`), with an arrow pointing right labelled
   `愈往東：雨量減少、年溫差變大`. A strip along the top `寒帶（近北極）`; a strip along the
   bottom `溫帶地中海型（南歐）：夏乾冬雨`; a small triangle mountain near the bottom strip
   labelled `高地氣候（阿爾卑斯山）`. Footnote: `山脈多東西走向，海洋水氣能深入內陸`.
3. **geo-eu3** — a three-circle Venn diagram, circles labelled `歐盟`, `歐元區`, `申根區`.
   Place these names (small text, one region each): centre (all three) `德國・法國・義大利`;
   歐盟 ∩ 申根區 only `瑞典・丹麥・波蘭`; 歐盟 ∩ 歐元區 only `愛爾蘭・賽普勒斯`;
   申根區 only `挪威・瑞士・冰島`; 歐元區 only `蒙特內哥羅・科索沃`. Leave the other regions
   empty. Footnotes: `歐元區：共同使用歐元` and `申根區：取消邊境管制`.
4. **geo-russia** — note `示意圖`. A west→east profile (left `西`, right `東`). Left: a flat
   low part `歐俄平原` (sub `人口集中・可發展農業`, tag `莫斯科・聖彼得堡`); then a low ridge
   `烏拉爾山` (sub `煤、鐵`); then `西伯利亞` rising in three steps `平原` → `高原` → `山地`,
   with sub `石油、天然氣`, and at the far right `火山、地震`. Under the Siberia part a small
   note with an arrow: `地勢南高北低，河川向北流`.
5. **geo-naprofile** — note `示意圖`. A west→east cross-section of North America (left `太平洋`,
   right `大西洋`): tall jagged `洛磯山脈` (sub `環太平洋火山地震帶`), a long flat low
   `北美大平原` (sub `密西西比河`), low rounded `阿帕拉契山脈` (sub `古老陸塊・礦產豐富`).
   Below the profile, a row of four small hazard chips: `地震（西側）`, `暴風雪（北部）`,
   `龍捲風（大平原）`, `颶風（東南部）`. A tag: `山脈南北走向：冬季冷空氣長驅直入`.
6. **geo-andes** — note `示意圖`. A tall mountain side view with four horizontal bands from the
   foot upward: `熱帶作物`, `溫帶作物`, `高山草原：放牧駱馬、羊駝`, `冰雪`. An upward arrow on
   the side labelled `海拔升高，氣溫降低`. Heading `安地斯山區的垂直變化`.
7. **geo-pacific3** — top: a rectangle of ocean (`var(--fig-sea)`) crossed by a horizontal
   dashed line `赤道 0°` and a vertical dashed line `180° 經線`. Labels: upper-left
   `密克羅尼西亞`, lower-left `美拉尼西亞`, the whole right side `玻里尼西亞`. A few tiny dots
   for islands. Bottom: two small side views: a low flat island with one palm, labelled
   `珊瑚礁島（低島）` and `地勢低平・淡水不足・漁業`; a tall cone island labelled
   `火山島（高島）` and `地勢高・土壤肥沃・可農耕`.
8. **geo-ausprofile** — note `示意圖`. A west→east profile of Australia (left `西`, right `東`):
   a long low plateau `西部高原`, a lower flat `中部平原`, a ridge `大分水嶺`, a narrow
   `東南沿海平原`, then sea. A wind arrow from the right (east) labelled `東南信風` meeting the
   ridge: label `迎風坡：多雨` on the east side, `背風坡：乾燥` on the west side. Tags:
   over the west `沙漠廣布・礦產豐富`, over the east coast `人口集中（雪梨・布里斯班）`.
9. **geo-poles** — two columns `北極地區` vs `南極地區`, rows:
   `範圍` — `北極圈（66.5°N）以內` / `南極圈（66.5°S）以內`;
   `主體` — `北極海（以海洋為主）` / `南極洲（以陸地為主的高原）`;
   `居民` — `少數原住民族` / `無人定居・以科學研究為主`;
   `重點` — `北極航道・飛越北極是最短航線` / `地表最冷・主權不屬任何國家`.
   Top band across both: `共同點：寒漠景觀・地軸傾斜造成永晝、永夜`.
10. **geo-warming** — left column heading `人類活動`, three boxes: `排放溫室氣體`, `大量砍伐森林`,
    `人造建物覆蓋地表`; arrows into a centre box `全球暖化`; arrows out to a right column
    heading `影響`, three boxes: `海水面上升` (sub `冰層融化・海水膨脹`), `生態衝擊`
    (sub `珊瑚白化・北極熊上岸`), `水旱災頻繁` (sub `極端天氣`). Bottom band:
    `1997 京都議定書 → 2015 巴黎協議：升溫控制在 2°C 內`.

### History 歷史（上古到近代的世界）

11. **his-worldera** — vertical list (dot + period + years + text):
    `上古` `約前 3500～前 500 年` `兩河、尼羅河流域發明文字`;
    `古典` `約前 500～後 500 年` `希臘羅馬文化・基督教誕生`;
    `中世紀` `約 500～1500 年` `拜占庭、伊斯蘭世界、西歐基督教世界`;
    `近代` `約 1500～1800 年` `科學革命・啟蒙運動・美法革命`;
    `19 世紀` (no year range on this row) `帝國主義國家海外擴張`;
    `現代` `20 世紀` `兩次世界大戰・冷戰`.
    Heading `世界歷史的分期`, footnote `依「時代特性」畫分`.
12. **his-mesoegypt** — comparison table, columns `兩河流域` / `埃及`, rows:
    `地形` — `平坦、缺少天然屏障` / `沙漠和高山屏障`;
    `政治` — `政權交替頻繁` / `較穩定・法老統治`;
    `文字` — `楔形文字` / `象形文字`;
    `曆法` — `陰曆` / `太陽曆`;
    `其他` — `六十進位・漢摩拉比法典` / `木乃伊・金字塔・幾何`.
13. **his-athsparta** — two columns `雅典` vs `斯巴達`, rows:
    `政治` — `民主政治` / `軍事統治`;
    `特色` — `男性公民參政・抽籤選官員・陶片放逐法` / `男性公民從小接受軍事訓練`;
    `重視` — `公民參與` / `紀律與服從`;
    `影響` — `民主政治的起源` / `武力強大`.
14. **his-rome** — vertical timeline (dot + date + text):
    `前 8 世紀` `建立羅馬城（王政）`; `前 6 世紀末` `推翻王政，改行共和`;
    `前 27 年` `屋大維獲奧古斯都尊號，進入帝國`; `前 27～後 180 年` `羅馬和平`;
    `4 世紀末` `帝國分為東、西兩部`; `476 年` `西羅馬帝國被日耳曼民族所滅`;
    `1453 年` `東羅馬帝國被鄂圖曼帝國攻滅`.
    Mark 共和 and 帝國 spans with two brackets labelled `共和時期` and `帝國時期`.
15. **his-religions3** — table, columns `佛教` / `基督教` / `伊斯蘭教`, rows:
    `創立` — `前 6 世紀・釋迦牟尼` / `1 世紀・耶穌` / `7 世紀・穆罕默德`;
    `起源` — `印度半島` / `巴勒斯坦` / `阿拉伯半島`;
    `主張` — `眾生平等・脫離輪迴` / `平等博愛・《聖經》` / `唯一真神阿拉・《古蘭經》`;
    `傳播` — `東亞、東南亞` / `歐洲` / `歐、亞、非各地`.
    Title `三大普世宗教`.
16. **his-church** — a tree, top to bottom: `基督教（1 世紀）` → at `11 世紀第一次分裂` two
    branches: `羅馬公教（天主教）` with sub `羅馬・政教分離・教宗` and `希臘正教（東正教）`
    with sub `君士坦丁堡・政教合一・拜占庭皇帝`. From 羅馬公教 at `16 世紀宗教改革`:
    a branch `新教` splitting into `路德教派`, `喀爾文教派`, `英國國教派`; and a separate
    small box `舊教改革：耶穌會`.
17. **his-voyages** — note `示意圖`. No real map: four rounded blobs labelled `歐洲`, `非洲`,
    `美洲`, `亞洲（印度）`, placed roughly where they are (美洲 left, 歐洲 top-middle, 非洲 below
    歐洲, 亞洲 right). Routes as curved arrows with labels: from 歐洲 down the west of 非洲 to its
    southern tip `狄亞士：好望角`; continuing round to 亞洲 `達伽馬：抵達印度`; from 歐洲 west to
    美洲 `哥倫布 1492：抵達美洲`; a long dashed loop round the south of 美洲 and off the left edge
    `麥哲倫船隊：環繞地球一周`. Legend: `葡萄牙：向東` and `西班牙：向西`.
18. **his-exchange** — note `示意圖`. Three rounded boxes in a triangle: `美洲` (left), `歐洲、亞洲`
    (top right), `非洲` (bottom right). Arrows with labels: 美洲 → 歐洲、亞洲 `白銀` and
    `玉米・番薯・馬鈴薯`; 歐洲、亞洲 → 美洲 `甘蔗、咖啡種植園` and `傳染病`; 非洲 → 美洲
    `黑奴（補充勞力）`. Heading `大航海後的交流`.
19. **his-enlight** — two panels left→right with an arrow between labelled `重視理性`.
    Left panel `科學革命（16、17 世紀）`: `哥白尼：太陽為宇宙中心`, `伽利略：望遠鏡證實`,
    `培根：歸納法`, `笛卡兒：演繹法`, `牛頓：萬有引力定律`. Right panel `啟蒙運動（18 世紀）`:
    `洛克：天賦人權`, `孟德斯鳩：三權分立`, `伏爾泰：宗教寬容・言論自由`, `盧梭：主權在民`,
    `狄德羅：百科全書`. A bottom arrow from the right panel to a box `美國獨立・法國大革命`.
20. **his-estates** — title `三級會議：一個階級一票`. Three columns: `教士` (a small group of
    3 simple person icons, label `人數少・有特權`, a ballot chip `1 票`), `貴族` (3 icons,
    `人數少・有特權`, `1 票`), `平民` (a large group of about 12 icons, `人數最多・負擔重稅`,
    `1 票`). A bracket over 教士 and 貴族 labelled `常聯手：2 比 1`. Bottom arrow to a box
    `平民不滿 → 另組國民會議`.
21. **his-revtimeline** — vertical timeline (dot + year + text), with a small tag `美國` or
    `法國` on each row: `1773` `波士頓茶葉事件` (美國); `1776` `發表《獨立宣言》` (美國);
    `1787` `制定第一部成文憲法` (美國); `1789` `攻陷巴士底監獄・《人權宣言》` (法國);
    `1804` `拿破崙稱帝` (法國); `1814～1815` `維也納會議` (法國 tag replaced by `歐洲`);
    `1815` `滑鐵盧戰役，拿破崙戰敗` (法國).

### Civics 公民（九上：經濟）

22. **civ-oppcost** — title `機會成本怎麼算？`. Three horizontal bars, lengths proportional:
    `發傳單 230 元`, `超商 220 元`, `餐廳 210 元` (use a common zero at the left; make the
    differences visible by starting the axis at 0 and using about 1.2 px per 元). The 發傳單 bar is
    marked `選擇`; the 超商 bar is outlined thick and labelled `機會成本＝220 元（放棄的最高者）`;
    the 餐廳 bar is faded. Bottom box: `機會成本＝放棄的選項中價值最高者＋實際多花的成本`.
23. **civ-incentive** — a 2×2 grid. Column headings `正向誘因（提高利益）` and
    `負向誘因（提高損害）`; row headings `金錢` and `非金錢`. Cells:
    金錢/正向 `做家事給零用錢`; 金錢/負向 `功課沒寫好扣零用錢`;
    非金錢/正向 `主動回答，平時成績加分`; 非金錢/負向 `上課吵鬧，記點`.
24. **civ-demandsupply** — two small line charts side by side, each with a vertical axis `價格`
    and a horizontal axis `數量`. Left heading `消費者`: a line going down to the right, labels
    `價格高 → 少買` near the top and `價格低 → 多買` near the bottom. Right heading `生產者`:
    a line going up to the right, labels `價格高 → 多生產` and `價格低 → 少生產`. Footnote:
    `其他條件不變時`.
25. **civ-profit** — title `利潤怎麼算？`. A long bar labelled `銷貨收入＝價格 × 銷售量`
    with the example `50 元 × 200 個＝10,000 元`. Under it, the same length split into two
    parts in proportion 6:4: `生產成本 6,000 元` (sub `地租・薪資・利息`) and `利潤 4,000 元`.
    Footnote: `利潤＝銷貨收入－生產成本`.
26. **civ-consumer** — two columns `消費者保護法` vs `公平交易法`, rows:
    `規範` — `消費者和廠商的消費關係` / `廠商之間的競爭關係`;
    `主管` — `行政院消費者保護處` / `行政院公平交易委員會`;
    `例子` — `網購 7 天猶豫期・向消保官申訴` / `處理壟斷・聯合漲價`.
    Bottom band: `前提：遵守誠實信用原則`.
27. **civ-labor** — a tree: `勞動` → `有酬勞動（市場勞動）` with two leaves `雇主：獲取利潤` and
    `受僱者：賺取薪資`; and `無酬勞動（非市場勞動）` with leaves `家務勞動` and `志工服務`.
    A separate box at the bottom: heading `勞動力`, text `年滿 15 歲・有能力・有意願工作`,
    splitting into `就業者：有工作` and `失業者：正在找工作`.
28. **civ-money** — a left→right (or top→bottom) flow of four steps: `以物易物`
    (sub `雙方都要剛好需要`) → `商品貨幣` (sub `貝殼・白銀・黃金`) → `法定貨幣`
    (sub `紙幣・硬幣，中央銀行發行`) → `塑膠貨幣・電子支付` (sub `儲值卡・信用卡`).
    Below, four chips headed `貨幣的功能`: `交易媒介`, `價值衡量`, `儲藏價值`, `清償債務`.
29. **civ-fx** — title `匯率變動（美元：新臺幣）`. Centre box `1：30`. Left arrow to a box
    `1：28` with `新臺幣升值`, `1,000 美元商品＝28,000 元`, `有利進口・出國旅遊`. Right arrow to a box
    `1：32` with `新臺幣貶值`, `1,000 美元商品＝32,000 元`, `有利出口`.
30. **civ-intltrade** — top: a flow of three boxes `原料` (sub `資源多的國家`) → `研發`
    (sub `人才多的國家`) → `製造` (sub `勞工多的國家`), headed `國際分工：選擇機會成本最低的組合`.
    Bottom: two boxes side by side with arrows: `出口` (sub `外國資金 → 本國`) and `進口`
    (sub `本國資金 → 外國`). Footnote: `出口成本：生產・運輸・關稅`.

## Finish

Run `python check_svg.py figs` until every file passes. Re-check every label against this brief.
In your final message list the new files you wrote and anything you could not draw exactly as
described.

# Brief: 18 more teaching diagrams (grade 9, second semester)

Same project, same rules as `BRIEF-figs.md` — read its **Format** and **Visual style** sections
and follow them exactly (viewBox 360 wide, height 140–280, `<title>` first, only the listed
elements, only `var(--fig-*)` / `var(--ic)` colours, ids prefixed with the file name, text
11–14 px with no overlap, under 9 KB, `示意圖` note where marked). The 133 existing files in
`figs/` are finished and approved: do not modify or delete any of them.

Lessons from earlier reviews — please follow:
- Never put dark text on a `var(--ic)` fill (it can be a dark colour). Use `var(--ic)` for
  outlines, small markers or bars without text; put text on `var(--fig-paper)` or light fills
  (`--fig-sea`, `--fig-land`, `--fig-sand`, `--fig-warm`, `--fig-cool`).
- Two neighbouring fills that mean different things must be clearly different colours.
- Timelines: give every label its own clear space; no leader line may cross any text. Use a
  vertical list layout (dot + date + text) when there are more than 6 events.
- Places and routes must be placed correctly relative to each other (for example Berlin lies
  inside East Germany). No real-world map outlines: use simple boxes or rounded blobs.
- Phones show these at about 340 px wide, so prefer two columns over four, and short lines.

Use the exact label wording given; never add facts, numbers, years or names that are not listed.
`・` separates short items on one line. Where a line is long, break it into two `<text>` lines.

### Geography 地理（臺灣的地名、農業與食品）

1. **geo-placename** — title `行政區名怎麼來？`. A 2×2 grid of cards, each with a heading and
   one or two example lines:
   `依方位` / `臺北・臺中・臺南・臺東`;
   `與自然環境有關` / `桃仔園 → 桃園` and `洄瀾 → 花蓮・平湖 → 澎湖`;
   `取自原住民族名稱` / `雞籠社 → 基隆・打狗社 → 高雄` and `噶瑪蘭族 → 宜蘭`;
   `與歷史事件有關` / `半線 → 彰化（彰顯教化）` and `諸羅 → 嘉義（嘉許忠義）`.
   Bottom band: `隨政權更迭而改：打狗 → 高雄（日治）・吉野 → 吉安（戰後）`.
2. **geo-tayovan** — title `「臺灣」這個名字`. A vertical flow of five boxes with down arrows:
   `平埔族：Tavoan（交會之地）` → `荷蘭人：地圖標為 Tayovan` → `漢人：大員・台員・臺灣` →
   `鄭氏：改稱安平，民間以「臺灣」稱全島` → `清帝國：臺灣府・臺灣縣・臺灣省`.
   A side tag beside the top: `西方水手：福爾摩沙（美麗之島）`.
3. **geo-landname** — note `示意圖`. A left→right landscape profile with labels pointing to
   each spot: a mountain with a village at its foot `山仔腳`; a steep slope `崎`; a small
   pond `潭`; a flat-topped tableland whose edge is a cliff, with `崁頂` on top and `崁腳` at
   the foot; then a low sand dune on the plain labelled `崙` with `崙頂` on top and `崙後`
   behind it, and a small wind arrow from the right labelled `風`. Footnote:
   `崙頂不易淹水，崙後可以避風`.
4. **geo-ethname** — title `地名裡的族群`. Top: three columns `閩南語` / `客家語` /
   `原住民族語`. Rows: `房屋` — `厝：陳厝・張厝` / `屋：黃屋・宋屋` / (empty);
   `山與谷` — (empty) / `崠：山頂・窩：山凹小河谷` / (empty);
   `例` — (empty) / `多在桃竹苗` / `鵝鑾鼻（排灣族語「船帆」）`.
   Bottom band headed `移民原鄉`: `泉州：泉州・同安・東石`, `漳州：南靖`, `惠州：陸豐`,
   `潮州：潮州`.
5. **geo-foodchain** — title `農產品怎麼到餐桌？`. Top row, a chain of small boxes with arrows:
   `產地農民` → `集貨市場` → `批發市場` → `零售商` → `消費者` (two rows of boxes are fine
   if needed). Under it a long thin arrow labelled `食物里程變長`. Bottom: a short direct arrow
   `產地` → `餐桌` labelled `地產地消：縮短食物里程`.
6. **geo-foodsafe** — title `降低食安風險`. Three cards side by side or stacked:
   `有機農產品` / `不用農藥、化肥` / `生產成本較高`;
   `產銷履歷` / `知道生產來源` / `和生產過程`;
   `地產地消` / `在地：縮短食物里程` / `當季：減少保鮮能源`.
   Top band: `食安問題：農藥化肥大量使用・食物里程增加`.

### History 歷史（現代國家到冷戰）

7. **his-germanyitaly** — comparison table, columns `德國統一` / `義大利統一`, rows:
   `阻礙` — `小國林立・奧國` / `奧國與法國`;
   `基礎` — `普魯士推動關稅同盟` / `馬志尼：恢復古羅馬光榮`;
   `人物` — `威廉一世・俾斯麥` / `伊曼紐二世・加富爾・加里波底`;
   `過程` — `戰勝奧國 → 德法戰爭` / `排除奧國 → 1861 義大利王國`;
   `完成` — `1871 德意志帝國成立` / `1870 收復羅馬定都`.
8. **his-alliances** — title `第一次世界大戰前的兩大陣營`. Two boxes side by side:
   `三國同盟` / `德・奧・義` and `三國協約` / `英・法・俄`. Between and below them a box
   `巴爾幹半島：歐洲火藥庫` with a small spark mark and the line `1914 塞拉耶佛事件`.
   Bottom, a short left→right timeline with three ticks: `1914 大戰爆發`,
   `1917 美國參戰・俄國革命`, `1918 停戰`.
9. **his-versailles** — centre box `巴黎和會（1919）`. Left branch: `《凡爾賽條約》` /
   `割地・賠款・裁軍` → `埋下二戰禍因`. Right branch: `十四點原則（威爾遜）` /
   `民族自決` → `東歐出現新興國家`. Bottom box: `國際聯盟（1920）` /
   `缺乏武力・美國未加入 → 名存實亡`.
10. **his-interwar** — title `戰間期（1918～1939）`. Top box `1929 經濟大恐慌`, arrows down to
    three boxes: `美國：羅斯福新政`, `義大利：墨索里尼・法西斯黨`, `德國：希特勒・納粹黨`.
    A separate box at the side or bottom: `俄國：1917 革命 → 1922 成立蘇聯`.
    Footnote: `極權政治興起，埋下二戰的種子`.
11. **his-ww2** — vertical timeline (dot + date + text):
    `1937` `盧溝橋事變（亞洲戰場）`; `1938` `慕尼黑協定（姑息政策）`;
    `1939` `德國入侵波蘭（歐洲戰場）`; `1941` `德國攻擊蘇聯`;
    `1941` `珍珠港事件，美國參戰`; `1944` `盟軍登陸諾曼第`;
    `1945.5` `德國投降`; `1945.8` `原子彈，日本無條件投降`.
12. **his-leagueun** — comparison table, columns `國際聯盟` / `聯合國`, rows:
    `成立` — `1920 年` / `1945 年`; `倡議者` — `威爾遜` / `羅斯福`;
    `美國` — `拒絕加入` / `主導運作`; `制裁侵略` — `缺乏武力` / `可要求會員國提供武力`.
13. **his-berlin** — note `示意圖`. Top: a rectangle for Germany split by a vertical line:
    left part `西德（美、英、法占領區）`, right part `東德（蘇聯占領區）`. Inside the right
    part, a circle `柏林` split by a line into `西柏林` and `東柏林`; the dividing line is drawn
    thick and labelled `柏林圍牆`. Bottom: a horizontal timeline with four ticks:
    `1948 封鎖西柏林`, `1961 興建圍牆`, `1989 推倒圍牆`, `1990 東西德統一`.
14. **his-coldwar2** — top: two boxes `北大西洋公約組織` / `美國領導・1949～` and
    `華沙公約組織` / `蘇聯領導・1955～1991`. Middle box: `第三世界：不加入兩大集團的亞非拉國家`.
    A row of four chips headed `冷戰衝突`: `柏林危機`, `古巴危機`, `韓戰・越戰`, `以阿戰爭`.
    Bottom flow: `1985 戈巴契夫改革` → `1989 柏林圍牆倒` → `1991 蘇聯解體`.

### Civics 公民（九下）

15. **civ-ipr** — table, columns `著作權法` / `專利法` / `商標法`, rows:
    `保護` — `語文・音樂・美術・攝影等` / `發明與創作` / `品牌標誌`;
    `取得` — `完成時就取得` / `申請審查通過` / `申請審查通過`.
    Bottom band (two lines): `著作財產權：保護到著作人死後 50 年` and
    `合理使用看：原創性・商業目的・使用比例・市場影響`.
16. **civ-globalization** — centre box `全球化` with sub `人才・資金・商品・資訊快速流動`.
    Three boxes around it: `經濟全球化` / `國際貿易・國際分工`; `政治全球化` /
    `國際組織・公約約束`; `文化全球化` / `音樂・飲食・漫畫流通`. Bottom band headed
    `例：臺灣加入 WTO` with three short items `市場開放（經濟）`, `修法、產地標章（政治）`,
    `進口肉品增加（文化）`.
17. **civ-refugee** — top: comparison, columns `難民` / `移民`, rows:
    `原因` — `迫害、戰爭、暴力，被迫離開` / `工作、教育，改善生活`;
    `依據` — `國際公約保護` / `移入國法令批准`.
    Bottom: heading `全球化的挑戰` and four chips: `貧富不均（血汗工廠）`,
    `文化單一化・文化衝突`, `疾病傳染`, `跨國犯罪`.
18. **civ-igo** — two columns: `政府間國際組織` (sub `主權國家簽約・官方`) listing
    `聯合國`, `世界貿易組織`, `亞太經濟合作會議`; and `國際非政府組織`
    (sub `民間・非營利・志願`) listing `國際特赦組織`, `國際反地雷組織`, `無國界醫生`.
    Bottom band headed `我國的參與`: `1991 以「中華臺北」參與 APEC` and
    `2002 以「臺澎金馬個別關稅領域」加入 WTO`.

## Finish

Run `python check_svg.py figs` until every file passes. Re-check every label against this brief.
In your final message list the new files you wrote and anything you could not draw exactly as
described.

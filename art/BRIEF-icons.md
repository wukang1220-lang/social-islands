# Brief: 36 small icons (museum items and player avatars)

Original icons for a junior-high social-studies learning page (Traditional Chinese, Taiwan).
They are shown in a "museum" grid (about 44 px on a 340 px wide phone), on item detail cards
(about 96 px) and as player avatars inside a hexagon (about 30–40 px). Draw everything yourself;
do not trace or imitate any brand, logo, app icon, game, flag or existing artwork.

## Must follow (checked by `python check_svg.py icons`)

- One file per icon: `icons/<key>.svg`. Write only the files named in your prompt.
- Root: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">`, no width/height.
- Allowed elements: g path circle ellipse rect line polyline polygon. No text, title, gradients,
  filters, style, script, image, href or comments.
- Colours: every fill/stroke is `none` or one of these CSS variables (they change with the theme):
  - `var(--ic)` accent colour of the item (use it for the main body of the object)
  - `var(--fig-ink)` outlines and dark details
  - `var(--fig-paper)` light parts and highlights
  - `var(--fig-warm)` fire, sun, gold, light; `var(--fig-cool)` ice, glass, sky
  - `var(--fig-sea)` water; `var(--fig-land)` plants and grass; `var(--fig-sand)` wood, paper, clay
  - `var(--fig-soft)` grey secondary details
- If you use an id, it must start with the file name.
- At most 1.6 KB per file. Round path numbers to at most 1 decimal.

## Style (keep all 36 consistent)

- Flat, friendly, chunky. One object per icon, centred, filling about 36–40 of the 48 units,
  with a 4-unit margin on every side.
- Outlines `var(--fig-ink)`, stroke-width 2.2, `stroke-linecap="round" stroke-linejoin="round"`
  (set these once on a wrapping `<g>`).
- Few shapes; each icon must still be recognisable at 28 px. No tiny details under 2 units.
- No words, letters, numbers, national flags, religious symbols, weapons, or faces.

## Icons

| key | object |
|---|---|
| compass | round compass with a two-colour needle |
| map | folded paper map, three panels, a dotted route |
| globe | globe on a curved stand, a meridian line |
| mountain | two mountain peaks, snowy tip on the taller one |
| coast | rocky cliff with one big curling wave |
| cloud | rain cloud with three short rain lines |
| drop | single water drop with a highlight |
| people | three round-headed simple figures side by side |
| wheat | bundle of three rice/wheat ears |
| factory | factory with a saw-tooth roof and one chimney with smoke |
| city | three tall buildings of different heights with windows |
| ship | small wooden sailing ship with one sail |
| train | front view of a train with two windows and a headlight |
| vase | ancient clay pot with a simple band pattern |
| scroll | rolled paper scroll, partly open, with lines (not letters) |
| coin | old round coin with a square hole in the middle |
| seal | square official stamp seal with a handle on top |
| book | closed thick book, bookmark ribbon |
| scale | balance scale with two pans, level |
| ballot | ballot box with a folded paper going into the slot |
| house | simple house with a pitched roof, door and window |
| flag | triangular pennant on a pole (plain, no symbols) |
| bubble | two overlapping speech bubbles |
| bulb | light bulb with short rays |
| crown | simple crown with three points and round jewels |
| column | classical stone column with a capital and base |
| oil | oil barrel with two ridges and a drip |
| tree | round leafy tree with a trunk |
| ice | iceberg floating on a water line |
| news | folded newspaper with a picture block and lines |
| phone | smartphone with a screen and a speech dot |
| shield | rounded shield with a check-mark stripe |
| gear | gear wheel with eight teeth and a hole |
| lighthouse | striped lighthouse with a light on top |
| telescope | small telescope on a tripod |
| anchor | ship anchor with a ring |

## Layout suggestions (may adjust)

- Use `var(--ic)` for the largest area (map panels, ship hull, barrel, book cover, shield…),
  `var(--fig-paper)` for highlights, windows and paper, and keep outlines dark.
- Approved style references for line weight and friendliness: `isles/geo-map.svg`,
  `isles/civ-law.svg`, `isles/his-qing.svg` (those are 120-unit emblems with an island; these
  icons have no island or sea base).

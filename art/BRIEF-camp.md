# Brief: camp buildings, decorations and three islanders

Original artwork for a junior-high social-studies learning page (Traditional Chinese, Taiwan).
Students earn building materials and coins by studying; they upgrade a camp on each island
(tent → hut → two-storey house → lighthouse) and decorate their own island with collected
items. Three friendly islanders give hints. Draw everything yourself; do not trace or imitate
any game, brand, logo, app icon, mascot or existing character. In particular the islanders
must NOT look like characters from any video game (no animal villagers, no raccoons, dogs,
foxes, owls or birds); draw them as simple round-headed cartoon people.

## Part A — icons (checked by `python check_svg.py icons`)

Same rules and style as `BRIEF-icons.md` (read it; the approved examples are the existing
files in `icons/`, e.g. `icons/lighthouse.svg`, `icons/house.svg`, `icons/tree.svg`):
48 × 48 viewBox, no text/title, colours only `none` or `var(--ic)` / `var(--fig-*)`,
outlines `var(--fig-ink)` stroke-width 2.2 on a wrapping `<g>`, at most 1.6 KB, one object
centred filling about 36–40 units, recognisable at 28 px.

These icons sit on a grass tile in an island editor and on the island map, so keep a little
ground shadow or base where it helps, but no sea and no island underneath.

| key | object |
|---|---|
| tent | small camping tent, triangular, door flap open |
| hut | small wooden hut with a sloped roof and one door |
| house2 | two-storey house, gabled roof, two rows of windows |
| palm | palm tree with three or four fronds |
| flower | small flower bed: three flowers on stems |
| lamp | old-style street lamp on a post, light glowing (`var(--fig-warm)`) |
| bench | park bench seen from the front-side |
| fence | short wooden fence section, three posts |
| rock | a pile of grey stones (also used as the "stone" building material) |
| windmill | small windmill with four sails |
| tower101 | very tall skyscraper made of stacked, slightly flared segments with a spire (a model of a famous Taipei landmark; simplified, no logo) |
| chikan | two-storey traditional Taiwanese tower pavilion on a stone base, curved upturned roof eaves, red walls |
| pyramid | ancient stone pyramid with a few block lines, small sun behind |
| lantern | round festival lantern hanging from a short cord, with tassel (no writing) |
| fireworks | a firework burst: lines radiating from a centre with dots at the tips, two colours |
| wood | pile of three cut logs showing tree rings (building material) |
| brick | small stack of red bricks in a bond pattern (building material) |

Colour suggestions (may adjust): main body `var(--ic)`; wood and logs `var(--fig-sand)`;
leaves `var(--fig-land)`; light `var(--fig-warm)`; stone `var(--fig-soft)` with
`var(--fig-paper)` highlights; glass and sky `var(--fig-cool)`.

## Part B — three islanders (checked by `python check_svg.py folk`)

- One file each: `folk/surveyor.svg`, `folk/storyteller.svg`, `folk/chief.svg`.
- Root `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96">`, no width/height,
  no text/title, same allowed elements and colour rules as the icons, at most 4 KB each.
- Shown at about 64–80 px inside a speech-bubble card, and at 40 px. Bust or three-quarter
  figure (head and shoulders plus their prop), centred, 4-unit margin.
- Friendly, chunky, flat; outlines `var(--fig-ink)` stroke-width 2.4, round caps/joins.
  Face: round head in `var(--fig-sand)`, two dot eyes, a small smile, rosy cheeks
  (`var(--fig-warm)` with fill-opacity .5). No realistic faces, no real people.
- Use `var(--ic)` for the clothing so each islander takes its subject colour on the page.

| file | who | look and prop |
|---|---|---|
| surveyor | 測量員「阿嶺」 (geography) | wide-brim field hat, explorer vest with pockets, holding a rolled map in one hand and a small compass in the other |
| storyteller | 說書人「卷卷」 (history) | round glasses, long scarf, holding an open scroll; a small paper fan tucked behind |
| chief | 里長「阿民」 (civics) | friendly older neighbourhood chief with short grey hair (`var(--fig-soft)`), a vest with a round badge (plain circle, no symbol), holding a small megaphone |

Make the three clearly different in silhouette (hat / glasses+scarf / grey hair+megaphone).

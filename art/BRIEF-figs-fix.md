# Brief: fixes to 7 diagrams in figs/

A reviewer looked at every diagram in `figs/` in light and dark themes. Most are approved and
must not be touched. Change ONLY the files listed below, keep all the rules in `BRIEF-figs.md`
(colours, ids, text sizes, no overlap, size limit), and leave every other file in `figs/` exactly
as it is. Do not touch `figs/geo-contour.svg` (it was redrawn separately).

1. **figs/geo-coasts.svg**
   - 沙岸 panel: the lagoon must be visible. Draw the shore (land) along the top, and a long sand
     bar offshore whose two ends curve back toward the shore, leaving one narrow inlet. Fill the
     enclosed water between bar and shore with `var(--fig-cool)` and the open sea with
     `var(--fig-sea)`. Put the label `潟湖` inside the enclosed water and point `沙洲` at the bar.
   - 珊瑚礁海岸 panel: the coral currently looks like dead black twigs. Replace with rounded,
     friendly coral clumps (branching coral with round tips and brain-coral domes) filled with
     `var(--ic)` and `var(--fig-warm)`, outlined in `var(--fig-ink)`.
2. **figs/geo-islands.svg**
   - 大陸島 panel: the valleys must look flooded. Draw the land (two hills and the valley between)
     first, then draw the water ON TOP of the land, from the raised sea level (the dashed line
     `海平面上升`) down to the panel bottom, with `fill="var(--fig-sea)" fill-opacity="0.85"`, so
     only the two hilltops stick out above the water. Keep a thin solid line lower down for the old
     sea level labelled `原海平面`.
   - 珊瑚礁島 panel: same coral style as above instead of twigs.
3. **figs/geo-rain.svg** — 對流雨 panel only: sun in the upper-right corner of the panel with a few
   short rays; a ground strip along the bottom; three upward arrows rising from the ground on the
   left half of the panel into ONE tall cloud near the top; heavy rain falling from the cloud on
   the right half of the panel, not crossing the arrows. Keep the label `夏季午後雷陣雨`.
4. **figs/geo-landforms.svg** — move `多高於 1,000 公尺` to sit directly under the `山地` label at the
   top (a small second line), and delete the long diagonal leader line.
5. **figs/geo-mapparts.svg** — in the legend box the tree overlaps the school symbol. Make the
   legend box taller and the three legend symbols small (about 12 px), one per row, each next to
   its word: `學校`, `公園`, `道路`. Make the tree on the map itself the same small style.
6. **figs/geo-watercycle.svg** — the label `地下逕流` sits on the bottom border. Move it up so it is
   inside the land, just above the dashed underground arrow.
7. **figs/his-periods.svg** — change the tick label `1624` to `約 400 年前` (the start of written
   records). Keep `1684`, `1895`, `1945` and everything else.

## Finish

Run `python check_svg.py figs` until all files pass, then list what you changed in each file.

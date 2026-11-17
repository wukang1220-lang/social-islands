"""Check SVG artwork for the social-islands page.

python check_svg.py isles      -> checks isles/*.svg
python check_svg.py figs       -> checks figs/*.svg
python check_svg.py icons      -> checks icons/*.svg (48 x 48 museum / avatar icons)
python check_svg.py folk       -> checks folk/*.svg (96 x 96 islander portraits)
python check_svg.py <file.svg> -> checks one file

Rules (both kinds):
  * well-formed XML, root <svg> with xmlns and a viewBox, no width/height on the root
  * only these elements: svg g path circle ellipse rect line polyline polygon text tspan title defs marker
  * no scripts, no event handlers, no external links, no <image>/<foreignObject>/<style>
  * every colour (fill / stroke / stop-color) is none, transparent, or var(--fig-*) / var(--ic)
  * every id starts with the file name (e.g. id="geo-rain-arrow" in geo-rain.svg)
  * file size limit: isles 3.5 KB, figs 9 KB, icons 1.6 KB
Extra rules for icons: viewBox 0 0 48 48, no <text>/<title>
Extra rules for folk: viewBox 0 0 96 96, no <text>/<title>, 4 KB
Extra rules for figs:
  * viewBox width is exactly 360, height between 140 and 280
  * has a <title>
  * text is 11px or larger, sits inside the viewBox, and no two text boxes overlap
    (rough box: CJK char = 1.0 x font-size, other char = 0.56 x font-size)
  * text may only be moved by translate() on parent <g>; no rotate/scale on text
"""
import os, re, sys
import xml.etree.ElementTree as ET

NS = "{http://www.w3.org/2000/svg}"
OK_EL = {"svg", "g", "path", "circle", "ellipse", "rect", "line", "polyline", "polygon",
         "text", "tspan", "title", "defs", "marker"}
OK_ATTR = {"viewBox", "xmlns", "role", "aria-label", "aria-hidden", "id", "d", "cx", "cy", "r", "rx", "ry",
           "x", "y", "x1", "y1", "x2", "y2", "dx", "dy", "width", "height", "points", "fill", "stroke",
           "stroke-width", "stroke-linecap", "stroke-linejoin", "stroke-dasharray", "stroke-opacity",
           "fill-opacity", "opacity", "fill-rule", "transform", "text-anchor", "font-size", "font-weight",
           "letter-spacing", "dominant-baseline", "markerWidth", "markerHeight", "refX", "refY", "orient",
           "markerUnits", "marker-end", "marker-start", "marker-mid", "vector-effect", "paint-order",
           "stroke-miterlimit"}
COLOR_OK = re.compile(r"^(none|transparent|var\(--(fig-[a-z]+|ic)\)|url\(#[\w-]+\))$")
CJK = re.compile(r"[⺀-鿿豈-﫿＀-￯　-〿]")


def text_width(s, size):
    return sum(size * (1.0 if CJK.match(ch) else 0.56) for ch in s)


def translate_of(chain):
    tx = ty = 0.0
    for el in chain:
        t = el.get("transform")
        if not t:
            continue
        m = re.fullmatch(r"\s*translate\(\s*([-\d.]+)(?:[\s,]+([-\d.]+))?\s*\)\s*", t)
        if not m:
            return None
        tx += float(m.group(1)); ty += float(m.group(2) or 0)
    return tx, ty


def check(path, kind):
    errs = []
    name = os.path.splitext(os.path.basename(path))[0]
    raw = open(path, encoding="utf-8").read()
    limit = {"isles": 3500, "icons": 1600, "folk": 4000}.get(kind, 9000)
    if len(raw.encode("utf-8")) > limit:
        errs.append(f"file is {len(raw.encode('utf-8'))} bytes, limit {limit}")
    if re.search(r"<\?xml|<!DOCTYPE|<!--|<script|<style|javascript:|href", raw, re.I):
        errs.append("contains a forbidden token (xml declaration, comment, script, style or href)")
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as e:
        return [f"XML parse error: {e}"]
    if root.tag != NS + "svg":
        errs.append("root element must be <svg xmlns=\"http://www.w3.org/2000/svg\">")
    vb = root.get("viewBox")
    if not vb:
        errs.append("root <svg> needs a viewBox")
        vb = "0 0 0 0"
    if root.get("width") or root.get("height"):
        errs.append("do not set width/height on the root <svg>")
    vx, vy, vw, vh = map(float, vb.split())
    if kind == "isles" and (vw, vh) != (120, 120):
        errs.append("isles viewBox must be 0 0 120 120")
    if kind in ("icons", "folk"):
        side = 48 if kind == "icons" else 96
        if (vx, vy, vw, vh) != (0, 0, side, side):
            errs.append(f"{kind} viewBox must be 0 0 {side} {side}")
        if root.find(".//" + NS + "text") is not None or root.find(".//" + NS + "title") is not None:
            errs.append(f"{kind} have no <text> or <title>")
    if kind == "figs":
        if vw != 360 or not 140 <= vh <= 280:
            errs.append("figs viewBox must be 0 0 360 H with 140 <= H <= 280")
        if root.find(NS + "title") is None:
            errs.append("figs need a <title> as the first child")

    boxes = []

    def walk(el, chain):
        tag = el.tag.replace(NS, "")
        if tag not in OK_EL:
            errs.append(f"element <{tag}> not allowed")
        for a, v in el.attrib.items():
            a2 = a.split("}")[-1]
            if a2 not in OK_ATTR and not a2.startswith("xmlns"):
                errs.append(f"attribute {a2} on <{tag}> not allowed")
            if a2 in ("fill", "stroke") and not COLOR_OK.match(v.strip()):
                errs.append(f'{a2}="{v}" on <{tag}>: use none or var(--fig-*) / var(--ic)')
            if a2 == "id" and not v.startswith(name):
                errs.append(f'id="{v}" must start with "{name}"')
            if a2 in ("marker-end", "marker-start", "marker-mid") and not COLOR_OK.match(v):
                errs.append(f"{a2}={v} must be url(#id)")
        if kind == "figs" and tag == "text":
            size = float(el.get("font-size") or next((p.get("font-size") for p in reversed(chain) if p.get("font-size")), 0) or 12)
            if size < 11:
                errs.append(f"text {''.join(el.itertext())!r} font-size {size} < 11")
            if el.get("transform"):
                errs.append("no transform directly on <text>; use x/y")
            off = translate_of(chain)
            if off is None:
                errs.append("only translate() is allowed on groups that contain text")
                off = (0, 0)
            anchor = el.get("text-anchor") or next((p.get("text-anchor") for p in reversed(chain) if p.get("text-anchor")), "start")
            lines = [el] + [t for t in el if t.tag == NS + "tspan" and (t.get("x") or t.get("dy"))]
            x0 = float(el.get("x", 0)); y0 = float(el.get("y", 0))
            for ln in lines:
                s = (ln.text or "") if ln is not el else (el.text or "") + "".join((t.text or "") + (t.tail or "") for t in el if not (t.get("x") or t.get("dy")))
                s = s.strip()
                if not s:
                    continue
                x = float(ln.get("x", x0)); y = float(ln.get("y", y0)) + float(ln.get("dy", 0) or 0)
                if ln is not el:
                    y0 = y
                w = text_width(s, size)
                left = x - (w / 2 if anchor == "middle" else w if anchor == "end" else 0)
                box = (left + off[0], y - 0.86 * size + off[1], left + w + off[0], y + 0.22 * size + off[1], s)
                boxes.append(box)
        for ch in el:
            walk(ch, chain + [el])

    walk(root, [])
    for i, (l, t, r, b, s) in enumerate(boxes):
        if l < vx - 0.5 or t < vy - 0.5 or r > vx + vw + 0.5 or b > vy + vh + 0.5:
            errs.append(f"text {s!r} runs outside the viewBox (box {l:.0f},{t:.0f}–{r:.0f},{b:.0f})")
        for (l2, t2, r2, b2, s2) in boxes[i + 1:]:
            if min(r, r2) - max(l, l2) > 1 and min(b, b2) - max(t, t2) > 1:
                errs.append(f"text {s!r} overlaps text {s2!r}")
    return errs


def main():
    arg = sys.argv[1]
    here = os.path.dirname(os.path.abspath(__file__))
    if arg in ("isles", "figs", "icons", "folk"):
        kind, files = arg, sorted(os.path.join(here, arg, f) for f in os.listdir(os.path.join(here, arg)) if f.endswith(".svg"))
    else:
        kind = next((k for k in ("isles", "icons", "folk") if os.sep + k + os.sep in os.path.abspath(arg)), "figs")
        files = [arg]
    bad = 0
    for f in files:
        e = check(f, kind)
        if e:
            bad += 1
            print(f"FAIL {os.path.basename(f)}")
            for x in e[:12]:
                print("   -", x)
        else:
            print(f"ok   {os.path.basename(f)}")
    print(f"{len(files) - bad}/{len(files)} passed")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()

"""Build social-islands.html from structure.json + content/*.json + extras.json + art/ + tpl.html.

python build.py [preview_out]
Writes ../social-islands.html (published as the claude.ai artifact, which adds its own page
skeleton) and docs/index.html (the same page as a full document, served by GitHub Pages).
Options are shuffled per question with a fixed seed so answers spread over A–D;
questions whose options are all numbers (years, ages, counts) keep their order.

museum.tsv gives every section one museum exhibit, in section order: "<subj> <isle> <no>|<icon>|<name>|<label>".
Icons come from art/icons/<icon>.svg (museum exhibits, avatars, camp buildings, decorations)
and art/folk/<name>.svg (islander portraits, emitted as "folk-<name>"), and art/guide/<name>.svg
(half-body islander guides for the tour and island intros, emitted as "guide-<name>").
extras.json maps a section id to {"fig": [diagram ids], "w": widget name, "wd": widget data}.
Diagrams come from art/figs/<id>.svg and island emblems from art/isles/<subj>-<id>.svg.
Every SVG must pass art/check_svg.py (no scripts, links or foreign colours); a file that
is missing or fails is left out with a warning, so the page still builds.
"""
import glob, json, os, random, re, sys, zlib

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "social-islands.html")
DOCS = os.path.join(HERE, "docs", "index.html")
# full-document skeleton for docs/index.html and the local preview (the artifact gets its own)
HEAD = ('<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" '
        'content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}'
        'body{margin:0;font:14px system-ui,sans-serif}[hidden]{display:none!important}</style></head><body>')
sys.path.insert(0, os.path.join(HERE, "art"))
from check_svg import check  # noqa: E402

st = json.load(open(os.path.join(HERE, "structure.json"), encoding="utf-8"))
content = {}
for f in sorted(glob.glob(os.path.join(HERE, "content", "*.json"))):
    content.update(json.load(open(f, encoding="utf-8")))
extras = json.load(open(os.path.join(HERE, "extras.json"), encoding="utf-8"))
# question counts before Version 10; a section that has grown since carries "n0" so the page
# can keep the stamps of students who had answered every one of its original questions
qbase = json.load(open(os.path.join(HERE, "qbase.json"), encoding="utf-8"))
# museum exhibits: one line per section, in the same order as structure.json
mus_lines = [l.rstrip("\r\n") for l in open(os.path.join(HERE, "museum.tsv"), encoding="utf-8") if l.strip()]
# past 會考 items per section, counted from the question bank by tally_cap.py (counts only)
CAP_P = os.path.join(HERE, "cap.json")
cap = json.load(open(CAP_P, encoding="utf-8")) if os.path.exists(CAP_P) else {}
HPUNC = re.compile(r"[\s，。、；：「」『』（）()？！,.?!*]")


def grams(t):
    t = HPUNC.sub("", t)
    return {t[i:i + 2] for i in range(len(t) - 1)}


def make_hint(stem, ans, kps):
    """提示卡的內容：和題目、答案最相關的一點重點，答案的字挖空成＿＿"""
    tg, ag = grams(stem), grams(ans)
    best, score = kps[0], -1
    for kp in kps:
        g = grams(kp)
        sc = len(g & tg) + 2 * len(g & ag)
        if sc > score:
            best, score = kp, sc
    a = ans.strip("。")
    out, hit = best, False
    for r in re.findall(r"\*\*(.+?)\*\*", best):
        if r in a or (len(a) >= 2 and a in r):
            out, hit = out.replace(f"**{r}**", "＿＿"), True
    out = out.replace("**", "")
    if not hit and len(a) >= 2 and a in out:
        out = out.replace(a, "＿＿", 1)
    return out


WIDGETS = {"tz", "scale", "climo", "era", "kin", "meet", "growth", "pyr", "fair", "sort", "chclim", "refer", "order", "branch", "wclim", "cap", "oppc", "profit", "fx", "foodmile"}
warn = []


def svg(kind, name):
    path = os.path.join(HERE, "art", kind, name + ".svg")
    if not os.path.exists(path):
        warn.append(f"missing art/{kind}/{name}.svg")
        return None
    errs = check(path, kind)
    if errs:
        warn.append(f"skipped art/{kind}/{name}.svg: {errs[0]}")
        return None
    s = open(path, encoding="utf-8").read().strip()
    s = re.sub(r">\s+<", "><", s)
    s = re.sub(r"\s+", " ", s)
    if kind == "isles":  # decorative: no tooltip, hidden from screen readers
        s = re.sub(r"<title>.*?</title>", "", s)
        s = s.replace("<svg ", '<svg aria-hidden="true" focusable="false" ', 1)
    return s


icons = {}
for f in sorted(glob.glob(os.path.join(HERE, "art", "icons", "*.svg"))):
    n = os.path.splitext(os.path.basename(f))[0]
    errs = check(f, "icons")
    if errs:
        warn.append(f"skipped art/icons/{n}.svg: {errs[0]}")
        continue
    t = open(f, encoding="utf-8").read().strip()
    t = re.sub(r">\s+<", "><", re.sub(r"\s+", " ", t))
    icons[n] = t.replace("<svg ", '<svg aria-hidden="true" focusable="false" ', 1)
# islander portraits (96 x 96) go in the same table as "folk-<name>"
for f in sorted(glob.glob(os.path.join(HERE, "art", "folk", "*.svg"))):
    n = os.path.splitext(os.path.basename(f))[0]
    errs = check(f, "folk")
    if errs:
        warn.append(f"skipped art/folk/{n}.svg: {errs[0]}")
        continue
    t = open(f, encoding="utf-8").read().strip()
    t = re.sub(r">\s+<", "><", re.sub(r"\s+", " ", t))
    icons["folk-" + n] = t.replace("<svg ", '<svg aria-hidden="true" focusable="false" ', 1)
# half-body guide portraits (160 x 200), "<islander>-<idle|point|cheer>", emitted as "guide-<name>"
for f in sorted(glob.glob(os.path.join(HERE, "art", "guide", "*.svg"))):
    n = os.path.splitext(os.path.basename(f))[0]
    errs = check(f, "guide")
    if errs:
        warn.append(f"skipped art/guide/{n}.svg: {errs[0]}")
        continue
    t = open(f, encoding="utf-8").read().strip()
    t = re.sub(r">\s+<", "><", re.sub(r"\s+", " ", t))
    icons["guide-" + n] = t.replace("<svg ", '<svg aria-hidden="true" focusable="false" ', 1)
mus_i = 0
numeric = re.compile(r"^[0-9０-９]")
spread = [0, 0, 0, 0]
nsec = nq = nfig = nw = nisle = npts = nkey = 0
for subj, sd in st.items():
    for isle in sd["isles"]:
        a = svg("isles", f"{subj}-{isle['id']}")
        if a:
            isle["svg"] = a
            nisle += 1
    for ch in sd["ch"]:
        for s in ch["secs"]:
            c = content[s["id"]]
            s["k"] = c["k"]
            for t in c["k"]:
                assert t.count("**") % 2 == 0, f"unclosed ** marker in {s['id']}: {t[:40]}"
            nkey += sum(t.count("**") // 2 for t in c["k"])
            npts += len(c["k"])
            qs = []
            for qi, (stem, opts, ans, exp) in enumerate(c["q"]):
                order = list(range(4))
                if not all(numeric.match(o) for o in opts):
                    random.Random(zlib.crc32(f"{s['id']}.{qi}".encode())).shuffle(order)
                new_opts = [opts[i] for i in order]
                new_ans = order.index(ans)
                spread[new_ans] += 1
                qs.append([stem, new_opts, new_ans, exp, make_hint(stem, opts[ans], c["k"])])
            s["q"] = qs
            assert len(qs) >= qbase[s["id"]], f"{s['id']} lost questions; only append new ones"
            if len(qs) > qbase[s["id"]]:
                s["n0"] = qbase[s["id"]]
            key, ic, mn, md = mus_lines[mus_i].split("|")
            mus_i += 1
            assert key == f"{subj} {ch['isle']} {s['id'].split('_')[-1]}", f"museum.tsv line {mus_i} is {key!r}, expected {subj} {ch['isle']} {s['id'].split('_')[-1]}"
            assert ic in icons, f"museum.tsv line {mus_i}: no icon {ic}"
            assert mn and md and len(mn) <= 9 and len(md) <= 34, f"museum.tsv line {mus_i}: name or label too long"
            s["mu"] = [ic, mn, md]
            if cap.get(s["id"]):
                s["cap"] = cap[s["id"]]
            ex = extras.get(s["id"], {})
            figs = [f for f in (svg("figs", n) for n in ex.get("fig", [])) if f]
            if figs:
                s["fig"] = figs
                nfig += len(figs)
            if ex.get("w"):
                assert ex["w"] in WIDGETS, ex["w"]
                s["w"] = ex["w"]
                if "wd" in ex:  # widget data
                    d = ex["wd"]
                    if ex["w"] == "sort":  # {"t": title, "c": [categories], "i": [[item, category index, note]]}
                        assert all(0 <= it[1] < len(d["c"]) for it in d["i"]), s["id"]
                    if ex["w"] == "branch":  # {"t": title, "s": start node, "n": {id: {"q": text, "o": [[label, next]]} | {"e": end text}}}
                        assert all(o[1] in d["n"] for n in d["n"].values() for o in n.get("o", [])), s["id"]
                    s["wd"] = d
                assert ex["w"] not in ("sort", "order", "branch") or "wd" in ex, s["id"]
                nw += 1
            nsec += 1
            nq += len(qs)
assert mus_i == len(mus_lines), f"museum.tsv has {len(mus_lines)} lines for {mus_i} sections"
unknown = set(extras) - {s["id"] for sd in st.values() for ch in sd["ch"] for s in ch["secs"]}
assert not unknown, f"extras.json has unknown section ids: {unknown}"

data = json.dumps(st, ensure_ascii=False, separators=(",", ":"))
assert "</script" not in data.lower()
tpl = open(os.path.join(HERE, "tpl.html"), encoding="utf-8").read()
assert "/*@DATA@*/null" in tpl
assert "/*@ICONS@*/null" in tpl
icon_js = json.dumps(icons, ensure_ascii=False, separators=(",", ":"))
html = tpl.replace("/*@DATA@*/null", data).replace("/*@ICONS@*/null", icon_js)
open(OUT, "w", encoding="utf-8", newline="\n").write(html)
for w in warn:
    print("warning:", w)
print(f"wrote {os.path.normpath(OUT)}: {len(html):,} chars, {nsec} sections, {npts} key points ({nkey} red terms), {nq} questions, "
      f"{nfig} diagrams, {nw} widgets, {nisle} emblems, {len(icons)} icons, {mus_i} exhibits, answer spread A–D {spread}")

os.makedirs(os.path.dirname(DOCS), exist_ok=True)
open(DOCS, "w", encoding="utf-8", newline="\n").write(HEAD + html + "</body></html>")
open(os.path.join(HERE, "docs", ".nojekyll"), "w").close()  # GitHub Pages: serve files as they are
print("wrote", os.path.normpath(DOCS))

if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8", newline="\n").write(HEAD + html + "</body></html>")
    print("preview", sys.argv[1])

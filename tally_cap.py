"""Count past 會考 items per section and write cap.json ({section id: number of items}).

python -I tally_cap.py <folder of text files>
The folder holds the question bank's 各章節會考試題 files converted to text (antiword -m UTF-8.txt),
named v<volume>__<original name>.txt, e.g. v1__01_01_1-1_1-1_如何表示位置.txt.
Only the number of items is used: each item has one "出處：" line. No question text is copied
into this project.
"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
st = json.load(open(os.path.join(HERE, "structure.json"), encoding="utf-8"))
ids = {s["id"] for sd in st.values() for ch in sd["ch"] for s in ch["secs"]}
pat = re.compile(r"^v(\d)__\d+_(\d\d)_(\d-[\dA-Z])(?:_(\d-\d))?")
cap, unknown = {}, []
for f in sorted(glob.glob(os.path.join(sys.argv[1], "*.txt"))):
    name = os.path.basename(f)
    m = pat.match(name)
    sid = None
    if m:
        v, code, chap, sec = m.groups()
        sid = f"{v}_{code}_{chap}" + (f"_{sec}" if sec else "")
    if sid not in ids:
        unknown.append(name)
        continue
    n = open(f, encoding="utf-8", errors="replace").read().count("出處：")
    cap[sid] = cap.get(sid, 0) + n
json.dump(dict(sorted(cap.items())), open(os.path.join(HERE, "cap.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(f"{sum(cap.values())} items in {len(cap)} sections")
for u in unknown:
    print("not matched:", u)

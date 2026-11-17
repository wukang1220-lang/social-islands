"""Version 10 merge: replace key points and append new questions.

python merge_v10.py <content-name e.g. geo-1> <v10 json> [--check]
The v10 json maps section id -> {"k": [10-15 points], "q": [new questions to append]}.
Rules checked: every section present; 10-15 points; each point has 1-2 red terms (**...**),
balanced markers and no '****'; existing questions are kept as they are and new ones
are appended so the section ends with exactly 6; each new question has 4 distinct options,
an answer index 0-3 and an explanation; no stem repeats within the section.
"""
import json, sys

name, src = sys.argv[1], sys.argv[2]
check_only = "--check" in sys.argv
P = f"D:/cluade/social-islands-src/content/{name}.json"
c = json.load(open(P, encoding="utf-8"))
new = json.load(open(src, encoding="utf-8"))
missing = [k for k in c if k not in new]
extra = [k for k in new if k not in c]
assert not missing and not extra, (missing, extra)
errs = []
for sid, v in new.items():
    k = v["k"]
    if not 10 <= len(k) <= 15:
        errs.append(f"{sid}: {len(k)} points")
    for t in k:
        n = t.count("**")
        if n % 2 or "****" in t:
            errs.append(f"{sid}: bad markers in {t[:30]}")
        elif not 1 <= n // 2 <= 2:
            errs.append(f"{sid}: {n // 2} red terms in {t[:30]}")
    qs = c[sid]["q"] + v.get("q", [])
    if len(qs) != 6:
        errs.append(f"{sid}: {len(c[sid]['q'])}+{len(v.get('q', []))} questions")
    for q in v.get("q", []):
        ok = (len(q) == 4 and isinstance(q[0], str) and q[0] and isinstance(q[1], list) and len(q[1]) == 4
              and len(set(q[1])) == 4 and q[2] in (0, 1, 2, 3) and isinstance(q[3], str) and q[3])
        if not ok:
            errs.append(f"{sid}: malformed question {str(q)[:40]}")
    stems = [q[0] for q in qs]
    if len(set(stems)) != len(stems):
        errs.append(f"{sid}: repeated stem")
if errs:
    print("\n".join(errs))
    sys.exit(1)
before_k = sum(len(v["k"]) for v in c.values())
before_q = sum(len(v["q"]) for v in c.values())
if not check_only:
    for sid, v in new.items():
        c[sid]["k"] = v["k"]
        c[sid]["q"] = c[sid]["q"] + v.get("q", [])
    rows = [json.dumps(k, ensure_ascii=False) + ":" + json.dumps(v, ensure_ascii=False, separators=(",", ":")) for k, v in c.items()]
    open(P, "w", encoding="utf-8").write("{\n" + ",\n".join(rows) + "\n}\n")
after_k = sum(len(v["k"]) for v in new.values())
after_q = before_q + sum(len(v.get("q", [])) for v in new.values())
red = sum(t.count("**") // 2 for v in new.values() for t in v["k"])
print(f"{name}{' (check only)' if check_only else ''}: {len(c)} sections, key points {before_k} -> {after_k}, red terms {red}, questions {before_q} -> {after_q}")

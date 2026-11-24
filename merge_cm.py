"""Merge 會考題型 (c) and 常見迷思 (m) into content/<name>.json.

python -I merge_cm.py <name> <file.json> [--check]
<file.json> is {section id: {"c": [2 questions], "m": [2–3 [迷思, 正解] pairs]}}.
A question is [stem, [4 options], answer index, explanation]. Key points and practice
questions are not touched. Once published, keep the two c questions in the same order
(their ids are <section>.c0 / .c1).
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
name, src = sys.argv[1], sys.argv[2]
check = "--check" in sys.argv
path = os.path.join(HERE, "content", name + ".json")
content = json.load(open(path, encoding="utf-8"))
new = json.load(open(src, encoding="utf-8"))
errs = []
for sid, v in new.items():
    if sid not in content:
        errs.append(f"{sid}: not in {name}.json")
        continue
    c, m = v.get("c", []), v.get("m", [])
    if len(c) != 2:
        errs.append(f"{sid}: needs exactly 2 會考題型, has {len(c)}")
    for i, q in enumerate(c):
        if not (isinstance(q, list) and len(q) == 4):
            errs.append(f"{sid} c{i}: must be [stem, options, answer, explanation]")
            continue
        stem, opts, ans, exp = q
        if not (isinstance(opts, list) and len(opts) == 4 and len(set(opts)) == 4 and all(isinstance(o, str) and o.strip() for o in opts)):
            errs.append(f"{sid} c{i}: needs 4 different non-empty options")
        if ans not in (0, 1, 2, 3):
            errs.append(f"{sid} c{i}: answer must be 0-3")
        if not (isinstance(stem, str) and len(stem) >= 25):
            errs.append(f"{sid} c{i}: stem should set up a situation (25+ characters)")
        if not (isinstance(exp, str) and exp.strip()):
            errs.append(f"{sid} c{i}: explanation missing")
    if not 2 <= len(m) <= 3:
        errs.append(f"{sid}: needs 2–3 迷思, has {len(m)}")
    for i, pr in enumerate(m):
        if not (isinstance(pr, list) and len(pr) == 2 and all(isinstance(x, str) and x.strip() and "**" not in x for x in pr)):
            errs.append(f"{sid} m{i}: must be [迷思, 正解] plain text")
missing = [sid for sid in content if sid not in new]
for e in errs:
    print("ERROR", e)
print(f"{len(new)} sections checked, {len(missing)} sections of {name} not in the file")
if errs:
    sys.exit(1)
if not check:
    for sid, v in new.items():
        content[sid]["c"] = v["c"]
        content[sid]["m"] = v["m"]
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("{\n" + ",\n".join(json.dumps(k, ensure_ascii=False) + ":" + json.dumps(v, ensure_ascii=False, separators=(",", ":")) for k, v in content.items()) + "\n}\n")
    print("merged into", path)

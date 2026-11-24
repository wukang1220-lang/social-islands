"""Flag 會考題型 / 常見迷思 text that copies long runs from source material (handouts, question bank).

python -I overlap_cm.py <cm json> <source txt>...
Prints every run of MIN or more characters (punctuation and spaces ignored) that also appears in the sources.
"""
import json, re, sys

MIN = 14
new = json.load(open(sys.argv[1], encoding="utf-8"))
norm = lambda t: re.sub(r"[\s\*「」『』《》【】（）()，。、；：！？,.;:!?─—…·\-｜|]", "", t)
S = norm("".join(open(p, encoding="utf-8", errors="replace").read() for p in sys.argv[2:]))
hits = 0
for sid, v in new.items():
    texts = [("c", " ".join([q[0]] + q[1] + [q[3]])) for q in v.get("c", [])] + [("m", a + " " + b) for a, b in v.get("m", [])]
    for kind, t in texts:
        n = norm(t)
        i = 0
        while i + MIN <= len(n):
            if n[i:i + MIN] in S:
                L = MIN
                while i + L < len(n) and n[i:i + L + 1] in S:
                    L += 1
                print(f"{sid} {kind}: {n[i:i + L]}")
                hits += 1
                i += L
            else:
                i += 1
print(f"{hits} overlapping runs")

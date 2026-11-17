"""Flag new text that copies long runs from the handout text.
python -I overlap.py <v10 json> <handout txt>... ; prints runs of >= MIN chars."""
import json, re, sys
MIN = 14
new = json.load(open(sys.argv[1], encoding="utf-8"))
src = "".join(open(p, encoding="utf-8").read() for p in sys.argv[2:])
norm = lambda t: re.sub(r"[\s\*「」『』《》【】（）()，。、；：！？,.;:!?─—…·\-]", "", t)
S = norm(src)
hits = 0
for sid, v in new.items():
    texts = [("k", t) for t in v["k"]] + [("q", " ".join([q[0]] + q[1] + [q[3]])) for q in v.get("q", [])]
    for kind, t in texts:
        n = norm(t)
        best = ""
        i = 0
        while i + MIN <= len(n):
            L = MIN
            if n[i:i+L] in S:
                while i + L < len(n) and n[i:i+L+1] in S:
                    L += 1
                if L > len(best):
                    best = n[i:i+L]
                i += L
            else:
                i += 1
        if best:
            hits += 1
            print(f"{sid} {kind} [{len(best)}] {best}")
print("flagged:", hits)

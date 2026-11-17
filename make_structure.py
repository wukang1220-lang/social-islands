"""One-time: build structure.json (subjects -> chapters -> sections) from the
question-bank file names plus the chapter titles found inside the files.

Usage: python make_structure.py <題本檔案 folder> <heads.json> <islands-meta.json> <out structure.json>
Only titles and numbering are taken from the bank; no question text is read here.
"""
import json, os, re, sys

root, heads_p, meta_p, out = sys.argv[1:5]
heads = json.load(open(heads_p, encoding="utf-8"))
heads.update({
    "2_01_1-1": "人口成長與分布", "2_01_1-2": "人口組成與族群文化", "2_01_1-3": "第一級產業",
    "2_01_1-4": "第二、三級產業", "2_01_1-5": "聚落體系與都市發展", "2_01_1-6": "區域發展與差異",
    "2_02_2-1": "日治時期的政治", "2_02_2-2": "日治時期的經濟", "2_02_2-3": "日治時期的社會與文化",
    "2_02_2-4": "戰後臺灣的政治", "2_02_2-5": "戰後臺灣的外交", "2_02_2-6": "戰後臺灣的經濟與社會",
    "2_03_3-1": "多元文化", "2_03_3-2": "社會規範", "2_03_3-3": "團體與志願結社",
    "2_03_3-4": "公共意見", "2_03_3-5": "公平正義", "2_03_3-6": "社會安全與國家責任",
    "1_02_2-0": "導言", "4_01_1-A": "導論",
})
meta = json.load(open(meta_p, encoding="utf-8"))

SUBJ_OF = {  # (book, subject code in file name) -> subject
    **{(b, "01"): "geo" for b in range(1, 7)},
    **{(b, "02"): "his" for b in (1, 2, 4, 5, 6)},
    **{(b, "03"): "civ" for b in (1, 2, 4, 5, 6)},
    (3, "02"): "geo", (3, "03"): "his", (3, "04"): "civ",
}
SEM = {"geo": "七上 七下 八上 八下 九上 九下".split(), "his": "七上 七下 八上 八下 九上 九下".split(),
       "civ": "七上 七下 八上 八下 九上 九下".split()}
# island by subject -> book -> list of (first chapter, last chapter, island id)
ISLE = {
    "geo": {1: [(0, 2, "map"), (3, 4, "land"), (5, 6, "climate")], 2: [(1, 3, "people"), (4, 6, "city")],
            3: [(1, 4, "china"), (5, 6, "neasia")], 4: [(0, 2, "seasia"), (3, 4, "mideast"), (5, 6, "africa")],
            5: [(1, 2, "europe"), (3, 4, "america"), (5, 6, "oceania")], 6: [(1, 3, "taiwan")]},
    "his": {1: [(0, 3, "prehist"), (4, 6, "qing")], 2: [(1, 3, "japan"), (4, 6, "postwar")],
            3: [(1, 3, "ancient"), (4, 6, "modern")], 4: [(1, 3, "republic"), (4, 6, "eastasia")],
            5: [(1, 3, "classic"), (4, 6, "earlymod")], 6: [(1, 4, "worldwar")]},
    "civ": {1: [(1, 2, "rights"), (3, 6, "family")], 2: [(1, 3, "culture"), (4, 6, "justice")],
            3: [(1, 6, "demo")], 4: [(1, 3, "law"), (4, 6, "rescue")],
            5: [(1, 3, "market"), (4, 6, "trade")], 6: [(1, 3, "global")]},
}

chapters = {}  # (subj, book, ch) -> chapter dict
for book in sorted(os.listdir(root)):
    m = re.match(r"0([1-6])_", book)
    if not m:
        continue
    b = int(m.group(1))
    d = os.path.join(root, book, "01_試題")
    for fn in sorted(os.listdir(d), key=lambda s: int(s.split("_")[0])):
        parts = os.path.splitext(fn)[0].split("_")
        subj_code, chap = parts[1], parts[2]
        subj = SUBJ_OF[(b, subj_code)]
        if len(parts) > 3 and re.fullmatch(r"\d-\d", parts[3]):
            sec, title = parts[3], "_".join(parts[4:])
        else:
            sec, title = None, "_".join(p for p in parts[3:] if p != "導言")
        title = title.strip().replace(" ", "")
        cn = chap.split("-")[1]
        ch = 0 if not cn.isdigit() or cn == "0" else int(cn)
        if b == 3 and subj_code == "02":
            ch += 4
        isle = next(i for lo, hi, i in ISLE[subj][b] if lo <= ch <= hi)
        key = (subj, b, ch)
        if key not in chapters:
            chapters[key] = {"b": b, "sem": SEM[subj][b - 1], "ch": ch, "name": heads[f"{b}_{subj_code}_{chap}"],
                             "isle": isle, "secs": []}
        cid = f"{b}_{subj_code}_{chap}" + (f"_{sec}" if sec else "")
        no = f"{ch}-{sec.split('-')[1]}" if (sec and ch) else ""
        chapters[key]["secs"].append({"id": cid, "no": no, "t": title})

data = {}
for subj in ("geo", "his", "civ"):
    chs = [chapters[k] for k in sorted(k for k in chapters if k[0] == subj)]
    isles = [{k: v for k, v in i.items() if k in ("id", "name", "tag", "c", "cl")} for i in meta[subj]["isles"]]
    data[subj] = {"isles": isles, "ch": chs}
    print(subj, len(isles), "isles,", len(chs), "chapters,", sum(len(c["secs"]) for c in chs), "sections")
json.dump(data, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

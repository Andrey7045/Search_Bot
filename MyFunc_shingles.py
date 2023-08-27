import json

import Shingles

with open('train.json', 'r', encoding='utf-8') as f:
    BD = json.load(f)
# print(BD)


def question(Q):
    global BD
    max = 0
    max_an = "-"
    for i in range(len(BD)):
        sdv = Shingles.compare_texts(Q, BD[i]["QUESTION"])
        if sdv > max:
            max = sdv
            max_an = BD[i]["ANSWER"]
    return {"question": Q, "answer": max_an, "percent": max}


import os 
import re
import json

with open('data/medicina.json', 'r') as f:
    data = json.load(f)


dataTreated = {}

for entry in data["entries"]:
    treatedEntry = {}

    # get galician word
    galego = list(entry.keys())[0]

    # get entry number
    number = entry[galego]["number"]

    # get entry info
    info = entry[galego]
    info.pop("number")
    # get keys inside info
    infoKeys = list(info.keys())

    info["languages"]["ga"] = galego

    # clean info
    for i in infoKeys:
        if i == "languages":
            for j in list(info[i].keys()):
                info[i][j] = re.sub(r'[\n\t]', r'', info[i][j])
        else:
            info[i] = re.sub(r'[\n\t]', r'', info[i])


    treatedEntry[number] = info
    
    dataTreated.update(treatedEntry)


with open('out/medicina_treated.json', 'w', encoding='utf-8') as f:
    json.dump(dataTreated, f, sort_keys=True, indent=1, ensure_ascii=False)
import os 
import re
import json

file = open("data/medicina.txt")
data = file.read()

# new Page identifiers: regex
newPageRe = re.compile(r'\f*Vocabulario\n\d+\n')
newPageRe2 = re.compile(r'\f')

# remove new page identifiers
data = newPageRe.sub('', data)
data = newPageRe2.sub('', data)

# write data to a clean file
with open('data/medicina_clean.txt', 'w') as f:
    f.write(data)

# get the clean data
lines = data.splitlines(keepends=True)

# regex to identify the first line of each entry
entryRe = re.compile(r'(^(\d+) [^\n]+\n)')

# get all the matches
# there is a trick in the line:
# "60 do pasado século co nome de"
# which is not the beggining of an entry
matches = []

for line in lines:
    match = entryRe.match(line)
    if match:
        if line == "60 do pasado século co nome de\n":
            continue
        else:
            matches.append(match.group(0))


# get the complete entries
entries = []
# we start at 1 because we want to skip the first line
numLine = 1
totalMatches = len(matches)
numMatch = 0
for match in matches:
    entry = []
    for line in lines[numLine:]:
        if numMatch+1 < totalMatches and line == matches[numMatch+1]:
            numMatch += 1
            break
        entry.append(line)
    entries.append(entry)
    numLine += len(entry)

# convert the entries to strings
entries = [''.join(entry) for entry in entries]

# regex helpers
genderRe = re.compile(r'([a-z]{1}\n)')
notesInitRe = re.compile(r'Nota\.\- ')
notesEndRe = re.compile(r'\.')
esRe = re.compile(r'\nes ')
enRe = re.compile(r'\nen ')
ptRe = re.compile(r'\npt ')
laRe = re.compile(r'\nla ')

# languages helper
def languagesHelper(data):
    languages = {}
    subdomain = ""
    data1 = re.split(esRe, data, 1)
    if len(data1) > 1:
        subdomain = data1[0]
        data2 = re.split(enRe, data1[1], 1)
    else:
        data2 = re.split(enRe, data1[0], 1)
    if len(data2) > 1:
        languages["es"] = data2[0]
        data3 = re.split(ptRe, data2[1], 1)
    else:
        data3 = re.split(ptRe, data2[0], 1)
    if len(data3) > 1:
        languages["en"] = data3[0]
        data4 = re.split(laRe, data3[1], 1)
    else:
        data4 = re.split(laRe, data3[0], 1)
    if len(data4) > 1:
        languages["pt"] = data4[0]
        languages["la"] = data4[1]
    else:
        languages["pt"] = data4[0]

    return subdomain, languages


# treat each entry and populate the dictionary
dictionary = {}
entriesDict = []
for entry in entries:
    entryDict = {}
    entryInfo = {}
    data = entry.split(" ",1)
    # get the number of the entry
    number = data[0]
    data = data[1]
    # get the name of the entry
    data = re.split(genderRe, data, 1)
    name = data[0]
    # remove ending spaces from the name
    name = name.rstrip()
    data = data[1:]
    # get the gender of the entry, removing the ending new line
    gender = data[0].split("\n")[0]
    # add info to the dictionary
    entryInfo["number"] = int(number)
    entryInfo["gender"] = gender
    data = re.split(notesInitRe, data[1], 1)
    notes_ = ""
    remissiveEntries = ""
    if len(data) > 1:
        notes = data[1]
        notes = notes.rstrip()
        notes = re.split(notesEndRe, notes, 1)
        notes_ = notes[0]
        if len(notes) > 1:
            remissiveEntries = notes[1]
        data = [data[0]]
    subdomain, languages= languagesHelper(data[0])
    entryInfo["subdomain"] = subdomain
    entryInfo["languages"] = languages
    entryInfo["notes"] = notes_
    entryInfo["remissiveEntries"] = remissiveEntries
    entryDict[name] = entryInfo
    entriesDict.append(entryDict)

dictionary["entries"] = entriesDict

dif = 0
dicto = {}
for entry in dictionary["entries"]:
    # count number of different keys
    for key in entry.keys():
        if key not in dicto:
            dicto[key] = 1
            dif += 1
        else:
            dicto[key] += 1

print("We have ", len(dictionary["entries"]), " different entries.")
print("We have ", dif, " different entries names.")

# write the dictionary to a JSON file with proper encoding
with open('out/medicina_txt.json', 'w', encoding='utf-8') as f:
    json.dump(dictionary, f, sort_keys=True, indent=1, ensure_ascii=False)





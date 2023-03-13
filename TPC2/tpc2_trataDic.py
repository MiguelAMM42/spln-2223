import os 
import re
import json


def cleanRemissiveEntries(info):
    rEntries = info.get('remissiveEntries')
    if rEntries == '':
        info['remissiveEntries'] = [] 
        info['VAR'] = []
    else:
        split = re.split(r'Vid\.-', rEntries)
        if len(split) > 1:
            info['VAR'] = split[:1]
        else:
            info['VAR'] = []   
        info['remissiveEntries'] = split[0]




def getSIN(info):
    subdomain = info.get('subdomain')
    if subdomain != '':
        split = re.split(r'SIN\.-', subdomain)
        if len(split) > 1:
            sins = re.split(r';', split[1])
            info['SIN'] = sins
        else:
            info['SIN'] = []   
        info['subdomain'] = split[0]
    else:
        info['subdomain'] = ""
        info['SIN'] = []



def cleanLanguages(langs, gaSIN, gaVid):
    if "en" in langs:
        enDict = {}
        enDict["variables"] = []
        enDict["synonyms"] = []
        enDict["values"] = re.split(r';', langs["en"])
        for i in range(len(enDict["values"])):
            enVars = re.split(r'Vid\.-', enDict["values"][i])
            enDict["values"][i] = enVars[0]
            if len(enVars) > 1:
                enDict["variables"].extend(enVars[:1])
            enSins = re.split(r'SIN\.-', enDict["values"][i])
            enDict["values"][i] = enSins[0]
            if len(enSins) > 1:
                enDict["variables"].extend(enSins[:1])
        langs["en"] = enDict
    if "es" in langs:
        esDict = {}
        esDict["variables"] = []
        esDict["synonyms"] = []
        esDict["values"] = re.split(r';', langs["es"])
        for i in range(len(esDict["values"])):
            esVars = re.split(r'Vid\.-', esDict["values"][i])
            esDict["values"][i] = esVars[0]
            if len(esVars) > 1:
                esDict["variables"].extend(esVars[:1])
            esSins = re.split(r'SIN\.-', esDict["values"][i])
            esDict["values"][i] = esSins[0]
            if len(esSins) > 1:
                esDict["variables"].extend(esSins[:1])
        langs["es"] = esDict
    if "pt" in langs:
        ptDict = {}
        ptDict["variables"] = []
        ptDict["synonyms"] = []
        ptDict["values"] = re.split(r';', langs["pt"])
        for i in range(len(ptDict["values"])):
            ptVars = re.split(r'Vid\.-', ptDict["values"][i])
            ptDict["values"][i] = ptVars[0]
            if len(ptVars) > 1:
                ptDict["variables"].extend(ptVars[:1])
            ptSins = re.split(r'SIN\.-', ptDict["values"][i])
            ptDict["values"][i] = ptSins[0]
            if len(ptSins) > 1:
                ptDict["variables"].extend(ptSins[:1])
        langs["pt"] = ptDict
    if "ga" in langs:
        gaDict = {}
        gaDict["variables"] = gaVid
        gaDict["synonyms"] = gaSIN
        gaDict["values"] = re.split(r';', langs["ga"])
        langs["ga"] = gaDict
    if "la" in langs:
        laDict = {}
        laDict["variables"] = []
        laDict["synonyms"] = []
        laDict["values"] = re.split(r';', langs["la"])
        for i in range(len(laDict["values"])):
            laVars = re.split(r'Vid\.-', laDict["values"][i])
            laDict["values"][i] = laVars[0]
            if len(laVars) > 1:
                laDict["variables"].extend(laVars[:1])
            laSins = re.split(r'SIN\.-', laDict["values"][i])
            laDict["values"][i] = laSins[0]
            if len(laSins) > 1:
                laDict["variables"].extend(laSins[:1])
        langs["la"] = laDict

    



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

    
    # clean remissive entries
    cleanRemissiveEntries(info)
    # clean synonyms
    getSIN(info)
    # clean languages and its synonyms and variables
    cleanLanguages(info["languages"],info["SIN"],info["VAR"])
    # delete SIN $ VAR
    del info["SIN"]
    del info["VAR"]


    treatedEntry[number] = info
    
    dataTreated.update(treatedEntry)


with open('out/medicina_treated.json', 'w', encoding='utf-8') as f:
    json.dump(dataTreated, f, sort_keys=True, indent=1, ensure_ascii=False)


def jsonToTxt(data):
    txtTreated = ""
    for k,v in data.items():
        txtTreated += "--- " + str(k) + "\n"
        for i,j in v.items():
            if i == "gender":
                txtTreated += "# " + j + "\n"

            elif i == "subdomain":
                txtTreated += "$ " + j + "\n"

            elif i == "languages":
                ##txtTreated += "\t" + i + "\n"
                for l,m in j.items():
                    txtTreated += "> " + l + " :\n"
                    for n,o in m.items():
                        txtTreated += "% " + n + " : "
                        for i in range(len(o)-1):
                            txtTreated += str(o[i]) + " ; "
                        if len(o) > 0:
                            txtTreated += str(o[-1]) + "\n"
                        else:
                            txtTreated += "\n"

            elif i == "notes":
                txtTreated += "! notes:" + j + "\n"
            
            elif i == "remissiveEntries":
                txtTreated += "& " + i + " :\n"
                for p in range(len(j)-1):
                    txtTreated += str(j[p]) + " ; "
                    if len(j) > 0:
                        txtTreated += str(j[-1]) + " ; "
                    else:
                        txtTreated += "\n"

            else:
                pass


    return txtTreated

txtTreated = jsonToTxt(dataTreated)
with open('out/medicina_treated.txt', 'w', encoding='utf-8') as f:
    f.write(txtTreated)

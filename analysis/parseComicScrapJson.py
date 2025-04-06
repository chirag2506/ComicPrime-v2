from utilities import *
import re
from datetime import datetime

comics = readJson("files/json/comicsScrap.json")

i = 0
j = 0

toBeChecked = {"comics": []}
write = True

for month, metadata in comics.items():

    # # check if commics specified same as array length
    # countComics = metadata.get("totalComics", 0) == len(metadata.get("comics", []))
    # if countComics == False:
    #     print(month)

    # # checking for vol, issue
    # regex = "Vol [0-9]+ -?'?([0-9]+|∞|½|X)"
    
    # for comic in metadata.get("comics", []):
    #     pattern = re.compile(regex)
    #     occ = pattern.finditer(comic)
    #     if(len(tuple(occ)) != 1):
    #         i += 1
    #         log.info("https://marvel.fandom.com/wiki/{}".format(comic.replace(" ", "_")))
    #         log.info(month)
    #         log.info("*"*100)
    #     else:
    #         for m in occ:
    #             print(m.start(), ":", m.group())
            

    # checking if vol, issue appears at end of each issue
    regex = "Vol [0-9]+ -?'?([0-9]+|∞|½|X)(AU)?A?B?(.[0-9]+)?" #issues can be [-1, 1, ∞, ½, X, '96, 4B, 9A, 14AU, 102.5]
    
    for comic in metadata.get("comics", []):
        pattern = re.compile(regex)
        occ = pattern.finditer(comic)
        occ = tuple(occ)
        start = occ[0].start()
        end = occ[0].end()
        if (end != len(comic)):
            if "TPB" in comic or " HC " in comic:
                j += 1 # trade paperback (reprint)
            else:
                i += 1
                toBeChecked["regex"] = regex
                toBeChecked["comics"].append("https://marvel.fandom.com/wiki/{}".format(comic.replace(" ", "_")))
                log.info(month)
                log.info(comic)
                log.info("*"*100)
        #1229 comics (with TPB)
        #307 without TPB
    True

print(i)
print(j)
if write == True:
    writeJson("files/json/comicsWithVolInBetween{}.json".format(int(datetime.now().timestamp()*1000)), toBeChecked)
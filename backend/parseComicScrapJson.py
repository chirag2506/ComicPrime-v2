from utilities import *
import re

comics = readJson("./comicsScrap.json")

i = 0
for month, metadata in comics.items():

    # # check if commics specified same as array length
    # countComics = metadata.get("totalComics", 0) == len(metadata.get("comics", []))
    # if countComics == False:
    #     print(month)

    # checking for vol, issue
    regex = "Vol [0-9]+ -?'?([0-9]+|∞|½|X)"
    
    for comic in metadata.get("comics", []):
        
        # occ = re.findall(regex, comic)
        occ = re.compile(regex)
        for m in occ.finditer(comic):
            print(m.start(), "helloo", m.group())
        # if len(occ) != 1:
        #     i += 1
        #     log.info("https://marvel.fandom.com/wiki/{}".format(comic.replace(" ", "_")))
        #     log.info(month)
        #     log.info("*"*100)
        # else:
        #     print(occ)
            

    # # checking if vol, issue appears at end of each issue
    # regex = "Vol [0-9]+ -?'?([0-9]+|∞|½|X)"

    # for comic in metadata.get("comics", []):
    #     occ = re.findall(regex, comic)

    #     # nameComponents = comic.split(" ")
    #     # issueNumber = nameComponents[-1]
    #     # if not str(issueNumber).startswith("#"):
    #     #     print(month)
    #     #     print(comic)
    #     #     print("*"*100)
    #     # found 12 occurances: 1971, Apr, Nov  2006...

    True
print(i)
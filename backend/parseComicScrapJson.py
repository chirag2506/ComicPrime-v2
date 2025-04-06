from utilities import *
import re

comics = readJson("./comicsScrap.json")

i = 0
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
            

    # # checking if vol, issue appears at end of each issue
    # regex = "Vol [0-9]+ -?'?([0-9]+|∞|½|X)"
    
    # for comic in metadata.get("comics", []):
    #     pattern = re.compile(regex)
    #     occ = pattern.finditer(comic)
    #     occ = tuple(occ)
    #     start = occ[0].start()
    #     end = occ[0].end()
    #     if (end != len(comic)):
    #         i += 1
    #         log.info(month)
    #         log.info(comic)
    #         log.info("*"*100)
    #     #1229 comics
    True
print(i)
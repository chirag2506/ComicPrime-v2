from utilities import *
import re

comics = readJson("files/json/comicsScrap.json")
volumes = []
content = {"volumes": []}
read = False
regex = "Vol [0-9]+"

for month, metadata in comics.items():
    if month == "November, 1961":
        read = True
    if month == "May, 1972":
        read = False
    if read == True:
        for comic in metadata.get("comics", []):
            pattern = re.compile(regex)
            occ = pattern.finditer(comic)
            occ = tuple(occ)
            if(len(occ) == 1):
                volumes.append(comic[0:occ[0].end()].strip())
            else:
                print(comic)

content["volumes"] = sorted(list(set(volumes)))
for i, volume in enumerate(content["volumes"]):
    content["volumes"][i] = [volume, "https://marvel.fandom.com/wiki/{}".format(volume.replace(" ", "_"))]
writeJson("files/json/volumesFromFF1ToJun1972.json", content)

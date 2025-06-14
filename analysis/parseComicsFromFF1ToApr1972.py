from utilities import *

comics = readJson("files/json/comicsScrap.json")
subComics = {}
read = False

for month, metadata in comics.items():
    if month == "November, 1961":
        read = True
    if month == "May, 1972":
        read = False
    if read == True:
        subComics[month] = metadata

writeJson("files/json/comicsScrapFF1ToApr1972.json", subComics)

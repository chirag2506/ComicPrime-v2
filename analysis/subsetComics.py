from utilities import *

comics = readJson("files/json/comicsScrap.json")
subComics = {}
read = False

#70s - 5800
start = "May, 1972"
end = "January, 1980"
fileName = "files/json/comics1970s.json"
#80s - 7519
start = "January, 1980"
end = "January, 1990"
fileName = "files/json/comics1980s.json"
#90s - 10145
start = "January, 1990"
end = "January, 2000"
fileName = "files/json/comics1990s.json"
#2000s - 10584
start = "January, 2000"
end = "January, 2010"
fileName = "files/json/comics2000s.json"
#2010s - 15419
start = "January, 2010"
end = "January, 2020"
fileName = "files/json/comics2010s.json"
#2020s - 7677
start = "January, 2020"
end = "January, 2030"
fileName = "files/json/comics2020s.json"

# num = 0

for month, metadata in comics.items():
    if month == start:
        read = True
    if month == end:
        read = False
    if read == True:
        subComics[month] = metadata
        # num += metadata["totalComics"]

writeJson(fileName, subComics)
# print(num)

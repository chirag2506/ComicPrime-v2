from utilities import *

comics = readJson("./comics.json")

for month, metadata in comics.items():
    print(month)
    if month == "November, 1961":
        break
    True
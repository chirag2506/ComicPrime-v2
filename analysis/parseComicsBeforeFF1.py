from utilities import *

comics = readJson("files/json/comics.json")

for month, metadata in comics.items():
    print(month)
    if month == "November, 1961":
        break

    for comic in metadata.get("comics", []):
        nameComponents = comic.split(" ")
        issueNumber = nameComponents[-1]
        if not str(issueNumber).startswith("#"):
            print(month)
            print(comic)
            print("*"*100)

    True
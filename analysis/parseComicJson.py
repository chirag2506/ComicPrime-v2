from utilities import *

comics = readJson("files/json/comics.json")

for month, metadata in comics.items():

    # # check if commics specified same as array length
    # countComics = metadata.get("totalComics", 0) == len(metadata.get("comics", []))
    # if countComics == False:
    #     print(month)

    # # checking for #
    # for comic in metadata.get("comics", []):
    #     if comic.count("#") > 1:
    #         print(month)
    #         print(comic)
    #         print("*"*100)
    #     # found 3 occurances 
    #     # July, 2004, Kabuki #1 (Variant) #0
    #     # November, 2006, Official Handbook of the Ultimate Marvel Universe #2 Book 2 #1
    #     # January, 2021, Captain America #117: Facsimile Edition #0

    # # checking if #issueNumber appears at end of each issue
    # for comic in metadata.get("comics", []):
    #     nameComponents = comic.split(" ")
    #     issueNumber = nameComponents[-1]
    #     if not str(issueNumber).startswith("#"):
    #         print(month)
    #         print(comic)
    #         print("*"*100)
    #     # found 12 occurances: 1971, Apr, Nov  2006...

    True
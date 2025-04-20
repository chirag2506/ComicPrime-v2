import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter
from utilities import *
import re

cred = credentials.Certificate("files/json/credentials.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

months = readJson("files/json/comicsScrapBeforeFF1.json")

regex = "Vol [0-9]+"

titlesRef = db.collection("titles")
titles = titlesRef.stream()
query1 = titlesRef.where(filter=FieldFilter("volume", "==", 2)).stream()
query2 = titlesRef.where(filter=FieldFilter("volume", "==", 1)).stream()

print(len(titles))
print(len(query1))
print(len(query2))

# docs = (
#     db.collection("cities")
#     .where(filter=FieldFilter("capital", "==", True))
#     .stream()
# )

# for doc in query1:
#     print(f"{doc.id} => {doc.to_dict()}")

# for doc in titles:
#     print(f"{doc.id} => {doc.to_dict()}")


# for month, metadata in months.items():
#     print(month)
#     comics = metadata.get("comics", [])
#     for comic in comics:
#         pattern = re.compile(regex)
#         occ = pattern.finditer(comic)
#         occ = tuple(occ)
#         if(len(occ) == 1):
#             name = comic[ : occ[0].start()].strip()
#             vol = int(comic[occ[0].start()+4 : occ[0].end()+1].strip())
#             issue = comic[occ[0].end()+1 : ]
#             print(name, ":", vol, ":", issue)
#             volumeUrl = "https://marvel.fandom.com/wiki/{}_Vol_{}".format(name.replace(" ", "_"), vol)
#             comicUrl = "https://marvel.fandom.com/wiki/{}".format(comic.replace(" ", "_"))
#             print(volumeUrl)
#             print("*"*100)


# for volume in toBeRead:
#     pattern = re.compile(regex)
#     occ = pattern.finditer(volume)
#     occ = tuple(occ)
#     if(len(occ) == 1):
#         name = volume[:occ[0].start()].strip()
#         num = int(volume[occ[0].start()+4:].strip())
#         print("{}, Vol {}".format(name, num))
#         keyName = re.sub("[^A-Za-z0-9]+", "", "{}vol{}".format(name, num)).lower()
#         url = "https://marvel.fandom.com/wiki/{}".format(volume.replace(" ", "_"))
#         docRef = db.collection("titles").document(keyName)
#         docRef.set({
#             "volume": num,
#             "title": name,
#             "toBeRead": True,
#             "url": url
#         })
#     else:
#         print("Not possible: {}".format(volume))

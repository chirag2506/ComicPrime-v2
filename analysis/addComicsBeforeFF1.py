import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from utilities import *
import re

cred = credentials.Certificate("files/json/credentials.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

volumes = readJson("files/json/comicsScrapBeforeFF1.json")


regex = "Vol [0-9]+"

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

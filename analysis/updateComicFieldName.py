import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter
from utilities import *

cred = credentials.Certificate("files/json/credentials.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

comicsRef = db.collection("comics")
comics = comicsRef.stream()
for comic in comics:
    # print(comic.id)
    metadata = comic.to_dict()
    # print(metadata)
    keyName = "coverDate"
    if keyName in metadata.keys():
        print(comic.id)
        metadata["coverYear"] = metadata.pop(keyName)
        # print(type(metadata))
        # print(metadata)
        comicRef = comicsRef.document(comic.id)
        comicRef.set(metadata)
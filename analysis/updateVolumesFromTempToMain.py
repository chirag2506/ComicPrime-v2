import firebase_admin
from utilities import *
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate("files/json/credentials.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

titlesTempRef = db.collection("titlesTemp")
titlesRef = db.collection("titles")
tempTitles = titlesTempRef.get()

for tTitle in tempTitles:
    meta = tTitle.to_dict()
    query = titlesRef.where(filter=FieldFilter("title", "==", meta["title"])).where(filter=FieldFilter("volume", "==", meta["volume"])).get()

    if (len(query) > 1 ):
        log.debug("{} for {} Vol {}".format(len(query), meta["title"], meta["volume"]))
    if (len(query) < 1):
        log.info("Addding for: {} Vol {}".format(meta["title"], meta["volume"]))

        volKeyName = "{}vol{}".format(meta["title"], meta["volume"]).replace(" ", "space").replace("/", "solidus").lower()
        volRef = titlesRef.document(volKeyName)
        volRef.set(meta)
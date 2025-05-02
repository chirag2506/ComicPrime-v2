
from utilities import *
from schema import *
import re
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate("files/json/credentials.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

months = readJson("files/json/comicsScrapFF1ToApr1972.json")
regex = "Vol [0-9]+"
comicsRef = db.collection("comics")

for month, metadata in months.items():
    print(month)
    comics = metadata.get("comics", [])
    for comic in comics:
        pattern = re.compile(regex)
        occ = pattern.finditer(comic)
        occ = tuple(occ)
        if(len(occ) == 1):
            cMonth = month.split(",")[0].strip()
            cYear = int(month.split(",")[1].strip())
            name = comic[ : occ[0].start()].strip()
            vol = int(comic[occ[0].start()+4 : occ[0].end()+1].strip())
            issue = comic[occ[0].end()+1 : ]
            query = comicsRef.where(
                filter=FieldFilter("title", "==", name)
            ).where(filter=FieldFilter("volume", "==", vol)).where(filter=FieldFilter("issue", "==", str(issue))).get()
            if (len(query) != 1 ):
                log.info("{} Vol {} Issue {}: {} {}".format(name, vol, issue, cMonth, cYear))
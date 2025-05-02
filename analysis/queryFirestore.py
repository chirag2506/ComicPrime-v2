from utilities import *
from schema import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate("files/json/credentials.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

comicsRef = db.collection("comics").where(
    filter=FieldFilter("coverYear", "==", 1972)
).where(filter=FieldFilter("coverMonth", "==", "May")).where(filter=FieldFilter("toBeRead", "==", True)).get()

for comic in comicsRef:
    print(comic.to_dict())
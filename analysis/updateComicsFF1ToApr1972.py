## Update toBeRead to False for some comics which I remember
## as of April 1972 (actual update when reading June 1972)

from utilities import *
from schema import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate("files/json/credentials.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

comicsRef = db.collection("comics")

def updateToFalse(id):
    comicsRef.document(id).set({"toBeRead": False}, merge=True)

def updateToTrue(id):
    comicsRef.document(id).set({"toBeRead": True}, merge=True)

name = "X-Men"
vol = 1
comics = comicsRef.where(filter=FieldFilter("title", "==", name)).where(filter=FieldFilter("volume", "==", vol)).stream()
for comic in comics:
    print(f"{comic.id} => {comic.to_dict()}")
    # issues = [80, 82, 84, 86]
    # if int(comic.to_dict()["issue"]) > 92 and comic.to_dict()["toBeRead"] == True:
    #     print("updating {}".format(comic.id))
    #     updateToFalse(comic.id)
    # if int(comic.to_dict()["issue"]) == 103 and comic.to_dict()["toBeRead"] == False:
    #     print("updating {}".format(comic.id))
    #     updateToTrue(comic.id)
    # updateToFalse(comic.id)

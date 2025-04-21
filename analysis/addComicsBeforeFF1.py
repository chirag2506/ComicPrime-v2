import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter
from utilities import *
import re
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from scrapPublishDate import getPublishDate
from checkForReprint import checkReprint

cred = credentials.Certificate("files/json/credentials.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

months = readJson("files/json/comicsScrapBeforeFF1.json")

regex = "Vol [0-9]+"

titlesRef = db.collection("titlesTemp")
comicsRef = db.collection("comics")
titles = titlesRef.stream()

inDb = []

for doc in titles:
    inDb.append(doc.id)
    # print(f"{doc.id} => {doc.to_dict()}")

print(inDb)

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
            #check if volume added
            volKeyName = re.sub("[^A-Za-z0-9]+", "", "{}vol{}".format(name, vol)).lower()
            if volKeyName not in inDb:
                volumeUrl = "https://marvel.fandom.com/wiki/{}_Vol_{}".format(name.replace(" ", "_"), vol)
                # log.info("{} : {} : {}".format(name, vol, issue))
                volRef = titlesRef.document(volKeyName)
                volRef.set({
                    "volume": vol,
                    "title": name,
                    "toBeRead": False,
                    "url": volumeUrl
                })
                inDb.append(volKeyName)            
            comicUrl = "https://marvel.fandom.com/wiki/{}".format(comic.replace(" ", "_"))
            uClient = uReq(comicUrl)
            pageHtml = uClient.read()
            uClient.close()
            pageSoup = soup(pageHtml, "html.parser")
            isReprint = checkReprint(pageSoup, name, vol, issue)
            publishDate = getPublishDate(pageSoup)
            keyName = re.sub("[^A-Za-z0-9]+", "", "{}vol{}issue{}".format(name, vol, issue)).lower()
            comicRef = comicsRef.document(keyName)
            comicRef.set({
                "volume": vol,
                "title": name,
                "issue": str(issue),
                "toBeRead": False,
                "coverMonth": cMonth,
                "coverDate": cYear,
                "releaseDate": publishDate,
                "reprint": isReprint,
                "url": comicUrl
            })
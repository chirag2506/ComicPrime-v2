import multiprocessing
import multiprocessing.queues
from utilities import *
from schema import *
import re
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.parse import quote
from scrapPublishDate import getPublishDate
from checkForReprint import checkReprint
from datetime import datetime

cred = credentials.Certificate("files/json/credentials.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

months = readJson("files/json/comicsScrapFF1ToApr1972.json")
volumes = readJson("files/json/volumesFromFF1ToApr1972Clean.json")
volumesToBeRead = volumes["ToBeRead"]
volumesIgnore = volumes["Ignore"]
regex = "Vol [0-9]+"
comicsRef = db.collection("comics")

def getComicDetails(month, comic, firestoreComicQueue):
    pattern = re.compile(regex)
    occ = pattern.finditer(comic)
    occ = tuple(occ)
    if(len(occ) == 1):
        cMonth = month.split(",")[0].strip()
        cYear = int(month.split(",")[1].strip())
        name = comic[ : occ[0].start()].strip()
        vol = int(comic[occ[0].start()+4 : occ[0].end()+1].strip())
        issue = comic[occ[0].end()+1 : ]
        comicUrl = "https://marvel.fandom.com/wiki/{}".format(quote(comic.replace(" ", "_")))
        uClient = uReq(comicUrl)
        pageHtml = uClient.read()
        uClient.close()
        pageSoup = soup(pageHtml, "html.parser")
        isReprint = checkReprint(pageSoup, name, vol, issue)
        publishDate = getPublishDate(pageSoup)
        volumeName = "{} Vol {}".format(name, vol)
        if volumeName in volumesIgnore or isReprint == True:
            toBeRead = False
        elif volumeName in volumesToBeRead:
            toBeRead = True
        else:
            toBeRead = None
            log.error("Not found volume: {} for issue {}".format(volumeName, issue))
        if toBeRead is not None:
            comicDetails = Comic(
                coverYear=cYear, coverMonth=cMonth, issue=str(issue), releaseDate=publishDate,
                reprint=isReprint, title=name, toBeRead=toBeRead, url=comicUrl, volume=vol
            )
            firestoreComicQueue.put(comicDetails)
    
def addComicToFirestore(details: Comic):
    print("Calling firestore comics for: {} Vol {} Issue {}".format(details.title, details.volume, details.issue))
    keyName = re.sub("[^A-Za-z0-9]+", "", "{}vol{}issue{}".format(details.title, details.volume, details.issue)).lower()
    comicRef = comicsRef.document(keyName)
    comicRef.set({
        "volume": details.volume,
        "title": details.title,
        "issue": details.issue,
        "toBeRead": details.toBeRead,
        "coverMonth": details.coverMonth,
        "coverYear": details.coverYear,
        "releaseDate": details.releaseDate,
        "reprint": details.reprint,
        "url": details.url
    })
        

# Worker function for processing tasks
def workerComic(taskQueue, processId, firestoreComicQueue):
    while True:
        try:
            task = taskQueue.get(timeout=300)  # wait for a task
            print(f"Comic worker Process-{processId} processing {task}")
            # time.sleep(random.uniform(0.5, 2))  # simulate work
            getComicDetails(task[0], task[1], firestoreComicQueue)
        except multiprocessing.queues.Empty:
            print(f"Comic worker Process-{processId}: No more tasks, exiting.")
            break
        taskQueue.task_done()
        

def workerFirestoreComic(taskQueue, processId):
    while True:
        try:
            task = taskQueue.get(timeout=300)
            print(f"Firestore comic Process-{processId} processing {task}")
            addComicToFirestore(task)
        except multiprocessing.queues.Empty:
            print(f"Firestore comic Process-{processId}: No more tasks, exiting.")
            break
        taskQueue.task_done()

if __name__ == "__main__":
    start = datetime.now()
    multiprocessing.set_start_method("spawn")

    numProcesses = 7
    manager = multiprocessing.Manager()
    taskQueue = manager.Queue()
    firestoreComicQueue = manager.Queue()

    for month, metadata in months.items():
        comics = metadata.get("comics", [])
        for comic in comics:
            taskQueue.put([month, comic])
            
    # Start worker processes
    processes: list[multiprocessing.Process] = []
    
    for i in range(numProcesses):
        p = multiprocessing.Process(target=workerComic, args=(taskQueue, i, firestoreComicQueue))
        p.start()
        processes.append(p)

    for i in range(numProcesses):
        p = multiprocessing.Process(target=workerFirestoreComic, args=(firestoreComicQueue, i))
        p.start()
        processes.append(p)

    # # Wait for the queue to be empty
    # while not taskQueue.empty():
    #     time.sleep(0.5)
    # while not firestoreComicQueue.empty():
    #     time.sleep(0.5)

    # Wait for all processes to finish
    # taskQueue.join()
    # firestoreComicQueue.join()
    for p in processes:
        p.join()  ####### SAME AS ABOVE, BUT JOINS FOR EACH QUEUE FOR EACH LOOP

    print("All tasks completed.")
    print("time for multiple thread: {}".format(datetime.now() - start))

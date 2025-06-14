from utilities import *
from schema import *
import re
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter
import multiprocessing
import multiprocessing.queues
from datetime import datetime

cred = credentials.Certificate("files/json/credentials.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

months = readJson("files/json/comics1990s.json")
regex = "Vol [0-9]+"
comicsRef = db.collection("comics")
skippedComics = {}

def deleteComic(month, comic):
    try:
        pattern = re.compile(regex)
        occ = pattern.finditer(comic)
        occ = tuple(occ)
        if(len(occ) == 1):
            name = comic[ : occ[0].start()].strip()
            vol = int(comic[occ[0].start()+4 : occ[0].end()+1].strip())
            issue = comic[occ[0].end()+1 : ]
            keyName = re.sub("[^A-Za-z0-9]+", "", "{}vol{}issue{}".format(name, vol, issue)).lower()
            comicsRef.document(keyName).delete()
    except Exception as e:
        log.error("Error in deleting {}: {}".format(comic, e))
        

# Worker function for processing tasks
def workerComic(taskQueue, processId):
    while True:
        try:
            task = taskQueue.get(timeout=30)
            print(f"Comic worker Process-{processId} processing {task}")
            deleteComic(task[0], task[1])
        except multiprocessing.queues.Empty:
            print(f"Comic worker Process-{processId}: No more tasks, exiting.")
            break
        taskQueue.task_done()


if __name__ == "__main__":
    start = datetime.now()
    multiprocessing.set_start_method("spawn")

    numProcesses = 10
    manager = multiprocessing.Manager()
    taskQueue = manager.Queue()

    for month, metadata in months.items():
            comics = metadata.get("comics", [])
            for comic in comics:
                taskQueue.put([month, comic])
            
    # Start worker processes
    processes: list[multiprocessing.Process] = []
    
    for i in range(numProcesses):
        p = multiprocessing.Process(target=workerComic, args=(taskQueue, i))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    

    print("All tasks completed.")
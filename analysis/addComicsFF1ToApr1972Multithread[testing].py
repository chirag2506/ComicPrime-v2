import multiprocessing
import multiprocessing.queues
import time, random
from utilities import *
from schema import *
import re
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from scrapPublishDate import getPublishDate
from checkForReprint import checkReprint
from datetime import datetime

months = readJson("files/json/comicsScrapBeforeFF1Temp.json")
regex = "Vol [0-9]+"

# start = datetime.now()
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
#             comicUrl = "https://marvel.fandom.com/wiki/{}".format(comic.replace(" ", "_"))
#             uClient = uReq(comicUrl)
#             pageHtml = uClient.read()
#             uClient.close()
#             pageSoup = soup(pageHtml, "html.parser")
#             isReprint = checkReprint(pageSoup, name, vol, issue)
#             publishDate = getPublishDate(pageSoup)

# print("time for single thread: {}".format(datetime.now() - start))
# time for single thread: 0:01:15.741970


def getComicDetails(month, comic):
    pattern = re.compile(regex)
    occ = pattern.finditer(comic)
    occ = tuple(occ)
    if(len(occ) == 1):
        cMonth = month.split(",")[0].strip()
        cYear = int(month.split(",")[1].strip())
        name = comic[ : occ[0].start()].strip()
        vol = int(comic[occ[0].start()+4 : occ[0].end()+1].strip())
        issue = comic[occ[0].end()+1 : ]
        comicUrl = "https://marvel.fandom.com/wiki/{}".format(comic.replace(" ", "_"))
        uClient = uReq(comicUrl)
        pageHtml = uClient.read()
        uClient.close()
        pageSoup = soup(pageHtml, "html.parser")
        isReprint = checkReprint(pageSoup, name, vol, issue)
        publishDate = getPublishDate(pageSoup)

# Worker function for processing tasks
def worker(taskQueue, processId):
    while True:
        try:
            task = taskQueue.get(timeout=3)  # wait for a task
        except multiprocessing.queues.Empty:
            print(f"Process-{processId}: No more tasks, exiting.")
            break
        print(f"Process-{processId} processing {task}")
        # time.sleep(random.uniform(0.5, 2))  # simulate work
        getComicDetails(task[0], task[1])
        print(f"Process-{processId} finished {task}")
        taskQueue.task_done()

if __name__ == "__main__":
    start = datetime.now()
    # multiprocessing.set_start_method("fork")  # or "spawn" on Windows
    multiprocessing.set_start_method("spawn")

    numProcesses = 4
    manager = multiprocessing.Manager()
    taskQueue = manager.Queue()

    # Populate the task queue
    # for i in range(20):
    #     taskQueue.put(f"Task-{i}")
    for month, metadata in months.items():
        comics = metadata.get("comics", [])
        for comic in comics:
            taskQueue.put([month, comic])
            
    # Start worker processes
    processes: list[multiprocessing.Process] = []
    for i in range(numProcesses):
        p = multiprocessing.Process(target=worker, args=(taskQueue, i))
        p.start()
        processes.append(p)

    # Wait for the queue to be empty
    while not taskQueue.empty():
        time.sleep(0.5)

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("All tasks completed.")
    print("time for multiple thread: {}".format(datetime.now() - start))
# time for multiple thread: 0:00:21.563960

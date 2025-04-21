from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from utilities import *

def checkReprint(pageSoup: soup, name, volume, issue):
    isReprint = True
    try:
        containers = pageSoup.findAll("aside", {"role": "region", "class": ["portable-infobox", "pi-background", "pi-border-color", "pi-theme-comic", "pi-layout-default"]})
        # print(len(containers))
        if(len(containers) == 2):
            container = containers[1]
            for i in range(1, 101):
                link = container.findAll("div",  {"data-source": "Links{}".format(i)})
                reprint = container.findAll("div",  {"data-source": "ReprintOf{}".format(i)})
                if(len(link) > 0):
                    if(len(reprint) == 0):
                        isReprint = False
                else:
                    break
    except Exception as e:
        log.error("Error in checking reprint for {} {} {}: {}".format(name, volume, issue, e))
        isReprint = False
    return isReprint

if __name__ == "__main__":
    name = "House of Harkness Infinity Comic"
    volume = 1
    issue = 12 # not a reprint
    name = "X-Men"
    volume = 1
    issue = 75 # single story, reprint
    name = "X-Men"
    volume = 1
    issue = 10 # not a reprint
    name = "Western Gunfighters"
    volume = 2
    issue = 2 # multiple story, 1 new
    name = "Western Gunfighters"
    volume = 2
    issue = 10 # multiple story, all reprint

    URL = "https://marvel.fandom.com/wiki/{name}_Vol_{volume}_{issue}".format(
        name = name.replace(" ", "_"),
        volume = volume,
        issue = issue
    )

    myUrl = URL
    uClient = uReq(myUrl)
    pageHtml = uClient.read()
    uClient.close()
    pageSoup = soup(pageHtml, "html.parser")
    isReprint = checkReprint(pageSoup, name, volume, issue)
    print(isReprint)
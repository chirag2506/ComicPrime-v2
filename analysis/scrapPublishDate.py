from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


def getPublishDate(pageSoup: soup):
    text = "Unknown"
    containers = pageSoup.findAll("div", {"data-source": "ReleaseDate"})

    if(len(containers) > 0):
        text = containers[0].div.a.text
    return text

if __name__ == "__main__":
    name = "House of Harkness Infinity Comic"
    volume = 1
    issue = 12

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
    date = getPublishDate(pageSoup)
    print(date)
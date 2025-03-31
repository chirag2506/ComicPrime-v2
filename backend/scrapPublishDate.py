from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

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

containers = pageSoup.findAll("div", {"data-source": "ReleaseDate"})

if(len(containers) > 0):
    text = containers[0].div.a.text
    print(text)

# comicNames = []
# for container in containers:
#     comicNameLink = container.findAll("a", {"class": "category-page__member-link"})
#     comicNames.append(comicNameLink[0].text)

# print(comicNames)
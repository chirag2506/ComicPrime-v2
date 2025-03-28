from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

month = "June"
year = "1972"
URL = 'https://marvel.fandom.com/wiki/Category:{year},_{month}_Cover_Date'.format(month = month, year = year)

myUrl = URL
uClient = uReq(myUrl)
pageHtml = uClient.read()
uClient.close()
pageSoup = soup(pageHtml, "html.parser")

containers = pageSoup.findAll("li", {"class": "category-page__member"})
comicsInThisVolume = len(containers)

comicNames = []
for container in containers:
    comicNameLink = container.findAll("a", {"class": "category-page__member-link"})
    comicNames.append(comicNameLink[0].text)

print(comicNames)
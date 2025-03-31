from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from datetime import datetime
from dateutil import relativedelta
from copy import deepcopy
from utilities import *

START_MONTH = "December"
END_MONTH = "February"
START_YEAR = "1939"
END_YEAR = "2025" # both inclusive
FILE_NAME = "./comicsScrap.json"

def scrapMonthlyComics(comicsPerMonth, sM, sY, eM, eY):
    start = datetime.strptime("{}, {}".format(sM, sY), "%B, %Y")
    end =  datetime.strptime("{}, {}".format(eM, eY), "%B, %Y")
    current = deepcopy(start)
    while True:
        currentMonth = datetime.strftime(current, "%B")
        currentYear = datetime.strftime(current, "%Y")
        thisMonth = f"{currentMonth}, {currentYear}"
        print(thisMonth)
        comicsPerMonth[thisMonth] = {}
        URL = 'https://marvel.fandom.com/wiki/Category:{year},_{month}_Cover_Date'.format(month = currentMonth, year = currentYear)

        myUrl = URL
        uClient = uReq(myUrl)
        pageHtml = uClient.read()
        uClient.close()
        pageSoup = soup(pageHtml, "html.parser")

        containers = pageSoup.findAll("li", {"class": "category-page__member"})
        comicsInThisMonth = len(containers)
        comicsPerMonth[thisMonth]["totalComics"] = comicsInThisMonth

        comicNames = []
        for container in containers:
            comicNameLink = container.findAll("a", {"class": "category-page__member-link"})
            comicNames.append(comicNameLink[0].text)
        comicsPerMonth[thisMonth]["comics"] = comicNames

        current = current + relativedelta.relativedelta(months=1)
        if(current > end):
            break
        
    return comicsPerMonth

if __name__ == "__main__":
    comicsPerMonth = {}
    comicsPerMonth = scrapMonthlyComics(comicsPerMonth, START_MONTH, START_YEAR, END_MONTH, END_YEAR)
    writeJson(FILE_NAME, comicsPerMonth)
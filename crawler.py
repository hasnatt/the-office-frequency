from bs4 import BeautifulSoup
import requests
import time
from scraper import *

for t in range(25301,25302):
    url = 'https://transcripts.foreverdreaming.org/viewtopic.php?f=574&t='+str(t)

    request = Scraper(url)
    print(request.get_season_and_title())
    # source = requests.get('https://transcripts.foreverdreaming.org/viewtopic.php?f=574&t='+str(t)).text
    # soup = BeautifulSoup(source, 'lxml')
    # print(soup.title.text)
    # time.sleep(1.5)

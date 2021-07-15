from bs4 import BeautifulSoup
import requests
import time
from scraper import *

for t in range(25301,25302):
    url = 'https://transcripts.foreverdreaming.org/viewtopic.php?f=574&t='+str(t)

    request = Scraper(url)
    print(request.get_character_word_frequency())
    # time.sleep(1.5)

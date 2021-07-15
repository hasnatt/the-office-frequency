from bs4 import BeautifulSoup
import requests
import time
from scraper import *


full_dict = list()

for episode in range(25305,25310):
    print(f'writing episode '+str(episode))
    print('**********************************************************************************')
    print('**********************************************************************************')
    word_frequency_dict = dict()
    url = 'https://transcripts.foreverdreaming.org/viewtopic.php?f=574&t='+str(episode)

    request = Scraper(url)

    # construct dictionary
    word_frequency_dict['s'] = request.get_season_and_episode()['s']
    word_frequency_dict['e'] = request.get_season_and_episode()['e']
    word_frequency_dict['title'] = request.get_title()
    word_frequency_dict['frequencies'] = request.get_character_word_frequency()
   
    full_dict.append(word_frequency_dict)
    time.sleep(1)


with open('wf.json', 'w') as f:
    json.dump(full_dict, f)
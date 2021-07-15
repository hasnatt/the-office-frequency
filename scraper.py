from bs4 import BeautifulSoup
import requests
import re
import string
import json
from collections import Counter

class Scraper:
    def __init__(self, url):
        self.url = url

    def get_html(self):
        source = requests.get(self.url).text
        soup = BeautifulSoup(source, 'lxml')
        return(soup)

    def get_season_and_title(self):
        soup = self.get_html()
        title = soup.title.text.split('-')
        season_title = title[0].split('x')
        return({
            's': season_title[0],
            'e': season_title[1]
        })


# with open('01_02.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')


# title = soup.title.text.split('-')
# season_title = title[0].split('x')

# script = soup.find('div', class_='postbody')

# episode_script = dict()
# episode_script['s'] = season_title[0]
# episode_script['e'] = season_title[1]


# script_list = []
# for line in script.select('p'):
#     line = line.text
#     # line = re.sub("[\(\[].*?[\)\]]", "", str(line.text))
#     if line:
#         split_line = line.split(': ')

#         script_line = {
#             'name':split_line[0],
#             'line': split_line[1],
#             'count': len(split_line[1].split())
#         }
#         script_list.append(script_line)
# episode_script['transcript'] = script_list

# characters_list = list()
# for ch in episode_script['transcript']:
#     characters_list.append(ch['name'])
# # print(dict(Counter(characters_list)))

# characters_list = list(dict.fromkeys(characters_list))


# episode_word_count = {}
# for character in characters_list:
#     transcripts = episode_script['transcript']
#     total_word_count = 0
#     for transcript in transcripts:
#         if character == transcript['name']:
#             total_word_count +=transcript['count']

#     episode_word_count[character] = total_word_count


# episode_script['frequencies'] = episode_word_count


# with open('script.json', 'w') as f:
#     json.dump(episode_script, f)
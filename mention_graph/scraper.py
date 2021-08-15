"""Scraper module"""

import re
import json
import time
from collections import Counter
import requests
from bs4 import BeautifulSoup


class Scraper:
    """Scraping the office transcript class """
    def __init__(self, url):
        self.url = url


    def get_html(self):
        """Return the HTML contents of the webpage with lxml parser"""
        source = requests.get(self.url).text
        soup = BeautifulSoup(source, 'lxml')
        return soup


    def is_deleted_scenes(self):
        """Check if transcript page is deleted scenes episode, return bool"""
        soup = self.get_html()
        title = soup.title.text
        substring = 'Deleted Scenes'
        if substring in title:
            return True
        return False


    def get_title(self):
        """Return episode title in the title tag"""
        soup = self.get_html()
        title = soup.title.text.split(' - ')
        return title[1].strip()


    def get_season_and_episode(self):
        """Return the season and episode defined in the webpage"""
        soup = self.get_html()
        title = soup.title.text.split('-')
        season_title = title[0].split('x')
        return({
            's': season_title[0],
            'e': season_title[1]
        })


    def get_transcript(self, include_count=True):
        """Gather the word count for each character in the given episode"""
        soup = self.get_html()
        script = soup.find('div', class_='postbody')
        script_list = []
        for line in script.select('p'):
            line = line.text
            line = re.sub(r"[\(\[].*?[\)\]]", "", str(line))
            if line and (':' in line) :
                split_line = line.split(':')
                script_line = {
                    'name':split_line[0],
                    'line': split_line[1].strip(),
                    'count': len(split_line[1].split())
                }
                script_list.append(script_line)
        return script_list

    def build_transcript_dict(self):
        pass


def main():
    """Main function to gather data"""
    full_dict = list()
    # range is from foreverdreaming url
    for episode in range(25306,25308+1):
        print(f'writing episode {str(episode)}')
        word_frequency_dict = dict()
        url = 'https://transcripts.foreverdreaming.org/viewtopic.php?f=574&t='+str(episode)

        request = Scraper(url)

        if request.is_deleted_scenes() is not True:
            # construct dictionary
            word_frequency_dict['s'] = request.get_season_and_episode()['s']
            word_frequency_dict['e'] = request.get_season_and_episode()['e']
            word_frequency_dict['title'] = request.get_title()

            full_dict.append(word_frequency_dict)
            time.sleep(1)

    with open('scriptdata/statictest.json', 'w') as file:
        json.dump(full_dict, file)

if __name__ == '__main__':
    print('f')
    url = 'https://transcripts.foreverdreaming.org/viewtopic.php?f=574&t=25306'
    request = Scraper(url)
    print(request.get_season_and_episode())


    with open('test.json', 'w') as file:
        json.dump(request.get_transcript(), file)
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


    def get_transcript(self):
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


    def get_characters_list(self):
        """Get list of characters for a given episode"""
        characters_list = list()
        for character in self.get_transcript():
            characters_list.append(character['name'])
        characters_list = list(dict.fromkeys(characters_list))
        return characters_list


    def get_characters_appearance_frequency(self):
        """ get the number of appearances a character makes for a given episode"""
        characters_list = list()
        for character in self.get_transcript():
            characters_list.append(character['name'])
        return dict(Counter(characters_list))


    def get_character_word_frequency(self):
        """Get the number of words spoken for each character"""
        episode_word_count = {}
        for character in self.get_characters_list():
            transcripts = self.get_transcript()
            total_word_count = 0
            for transcript in transcripts:
                if character == transcript['name']:
                    total_word_count +=transcript['count']

            episode_word_count[character] = total_word_count

        return episode_word_count


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
            word_frequency_dict['frequencies'] = request.get_character_word_frequency()
            full_dict.append(word_frequency_dict)
            time.sleep(1)

    with open('scriptdata/statictest.json', 'w') as file:
        json.dump(full_dict, file)

if __name__ == '__main__':
    main()

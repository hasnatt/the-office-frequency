import json
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from operator import itemgetter


class GraphCharacter:
    def __init__(self, character, freq_dir):
        self.character = character
        self.freq_dir = freq_dir


    def load_script(self):
        with open(self.freq_dir) as json_file:
            data = json.load(json_file)
        return(data)
 

    def get_episode_wordfreq_lists(self):
        words_list = list()
        episodes_list = list()
        counter = 0 
        counter_list=list()
        for episode in self.load_script():

            counter_list.append(counter)
            counter +=1    
            if self.character in episode['frequencies'].keys():
                # print(f"{episode['s']}x{episode['e']}: {episode['frequencies'][self.character]")
                words_list.append(int(episode['frequencies'][self.character]))
                episodes_list.append(f"{episode['s']}{episode['e']}")
            
            else:
                # print(f"{episode['s']}x{episode['e']}: 0")    
                words_list.append(0)
                episodes_list.append(f"{episode['s']}x{episode['e']}")

        return({
            'counter_list': counter_list,
            'word_frequencies': words_list,
            'episode_list': episodes_list,
            }
        )

    def get_word_freq_list(self):
        return(self.get_episode_wordfreq_lists()['word_frequencies'])   

    def get_episode_list(self):
        return(self.get_episode_wordfreq_lists()['episode_list']) 

    def get_df(self):
        return(pd.DataFrame({'ep': self.get_episode_list(), 'words': self.get_word_freq_list()}))

    def plot_show(self):
        plt.figure(figsize=(40, 4))
        plt.xlabel("Episodes", size=18)
        plt.ylabel("Word count",size=18)
        plt.rc('font', size=1) 
        plt.title(f'The Office: {self.character} WPO', size=18)
        plt.ylim([0,2300])
        plt.fill_between(self.get_df().ep, self.get_df().words, color='tab:blue',alpha=0.3)
        # plt.axis(False)
        plt.xticks(rotation=90)

        sns.lineplot(x='ep', y='words', data=self.get_df(), sort=False, linewidth=4)
        plt.show()

    def plot_save(self):
        plt.figure(figsize=(40, 4))
        plt.rc('font', size=1) 
        plt.ylim([0,2300])
        plt.fill_between(self.get_df().ep, self.get_df().words, color='tab:blue',alpha=0.3)
        plt.axis(False)
        plt.xticks(rotation=90)

        sns.lineplot(x='ep', y='words', data=self.get_df(), sort=False, linewidth=4)
        plt.savefig(f"img/{self.character}.png", dpi = 400, transparent=True)    


class DataAnalysis():
    def __init__(self, freq_dir):
        self.freq_dir = freq_dir


    def load_script(self):
        with open(self.freq_dir) as json_file:
            data = json.load(json_file)
        return(data)

    def get_character_list(self):
        character_list = list()
        for character in self.load_script():
            for x in character['frequencies']:
                character_list.append(x)
        return(list(dict.fromkeys(character_list)))


    # TODO: below
    def get_popular_character_list(self):
        pass 

    def get_character_total_words(self, range):
        #Parameters:
        #    range (range):The range and amount of character word counts 

        l = list()
        # for each character
        for character in self.get_character_list():
            word_counter = 0
            # in  
            for script in self.load_script():
                for key in script['frequencies']:
                    if key == character:
                        # print(key, '->', script['frequencies'][key])
                        word_counter += int(script['frequencies'][key])
            l.append({'character': character, 'word_count':word_counter})

        new = sorted(l, key=itemgetter('word_count'), reverse=True)
        print(new[0:range]) 

    # TODO: below
    def plot_character_total_words(self):
        pass


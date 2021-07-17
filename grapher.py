import json
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

class Grapher:
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







if __name__ == '__main__':
    graph = Grapher('Michael', 'full_frequency.json')
    print(graph.plot_show())

# # TODO: Implement a class and start using static and class methods


# words_list = list()
# episodes_list = list()
# counter = 0 
# counter_list=list()
# for episode in data:
#     counter_list.append(counter)
#     counter +=1    
#     if "Michael" in episode['frequencies'].keys():

#         print(f"{episode['s']}x{episode['e']}: {episode['frequencies']['Michael']}")
#         words_list.append(int(episode['frequencies']['Michael']))
#         episodes_list.append(f"{episode['s']}{episode['e']}")
    
#     else:
#         print(f"{episode['s']}x{episode['e']}: 0")    
#         words_list.append(0)
#         episodes_list.append(f"{episode['s']}x{episode['e']}")



# data = {'ep': episodes_list, 'words': words_list}
# #convert dictionary to a dataframe
# df = pd.DataFrame(data)
# #Print out all rows        
# print(df)    

# plt.style.use('fivethirtyeight')
# # plt.figure(figsize=(36, 6))
# # # plt.grid(b=None)
# # # plt.axis(False)
# # plt.plot(counter_list, words_list, linewidth=12)
# # plt.savefig("test.png", dpi = 400, transparent=True)



# # fig = plt.figure()
# # ax = fig.add_axes([0,0,1,1])
# # ax.bar(episodes_list,words_list)
# # plt.show()



# plt.figure(figsize=(36, 4))
# plt.rc('font', size=6) 
# plt.fill_between(df.ep, df.words, color='tab:brown')
# # plt.axis(False)
# plt.xticks(rotation=90)

# sns.lineplot(x='ep', y='words', data=df, sort=False, linewidth=4)
# plt.show()


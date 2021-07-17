import json
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# TODO: Implement a class and start using static and class methods


with open('full_frequency.json') as json_file:
    data = json.load(json_file)

words_list = list()
episodes_list = list()
counter = 0 
counter_list=list()
for episode in data:
    counter_list.append(counter)
    counter +=1    
    if "Michael" in episode['frequencies'].keys():

        print(f"{episode['s']}x{episode['e']}: {episode['frequencies']['Michael']}")
        words_list.append(int(episode['frequencies']['Michael']))
        episodes_list.append(f"{episode['s']}{episode['e']}")
    
    else:
        print(f"{episode['s']}x{episode['e']}: 0")    
        words_list.append(0)
        episodes_list.append(f"{episode['s']}x{episode['e']}")



data = {'ep': episodes_list, 'words': words_list}
#convert dictionary to a dataframe
df = pd.DataFrame(data)
#Print out all rows        
print(df)    

plt.style.use('fivethirtyeight')
# plt.figure(figsize=(36, 6))
# # plt.grid(b=None)
# # plt.axis(False)
# plt.plot(counter_list, words_list, linewidth=12)
# plt.savefig("test.png", dpi = 400, transparent=True)



# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.bar(episodes_list,words_list)
# plt.show()



plt.figure(figsize=(36, 6))
plt.fill_between(df.ep, df.words, color='tab:brown')

plt.axis(False)
sns.lineplot(x='ep', y='words', data=df, sort=False, linewidth=4)
plt.show()


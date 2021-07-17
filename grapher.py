import json
from matplotlib import pyplot as plt

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
        episodes_list.append(f"{episode['s']}x{episode['e']}")
    
    else:
        print(f"{episode['s']}x{episode['e']}: 0")    
        words_list.append(0)
        episodes_list.append(f"{episode['s']}x{episode['e']}")
    

plt.style.use('fivethirtyeight')
plt.figure(figsize=(18, 3))
plt.grid(b=None)
plt.plot(counter_list, words_list)

plt.show()
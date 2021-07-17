import json

with open('full_frequency.json') as json_file:
    data = json.load(json_file)

for episode in data:
    if "Michael" in episode['frequencies'].keys():
        print(f"{episode['s']}x{episode['e']}: {episode['frequencies']['Michael']}")
    else:
        print(f"{episode['s']}x{episode['e']}: 0")    

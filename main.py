from graphcharacter import *
from scraper import *

if __name__ == '__main__':

    da = DataAnalysis('scriptdata/full_frequency.json')
    cw = da.get_character_total_words(range=10)
    popular_characters = list()

    for item in cw:
        popular_characters.append(item['character'])
    print(popular_characters)


    
    for character in popular_characters:
        
        graph = GraphCharacter(character, 'scriptdata/full_frequency.json')
        character_colours = graph.get_character_colours()
        graph.plot_save(character_colours[character])

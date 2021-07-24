from graphcharacter import *
from scraper import *


def main():
    da = DataAnalysis('scriptdata/full_frequency.json')
    # Range for only top 10 most spoken characters
    cw = da.get_character_total_words(range=10)
    popular_characters = list()

    for item in cw:
        popular_characters.append(item['character'])


    # Append any extra characters
    # popular_characters.append('Creed')

    for character in popular_characters:
        graph = GraphCharacter(character, 'scriptdata/full_frequency.json')
        character_colours = graph.get_character_colours()
        # graph.plot_save(character_colours[character])
        graph.plot_save2(character_colours[character])


if __name__ == '__main__':
    main()
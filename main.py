from graphcharacter import *
from scraper import *

if __name__ == '__main__':
    main_characters = ['Micheal', 'Dwight', 'Jim', 'Pam', '']
    # graph = GraphCharacter('Pam', 'scriptdata/full_frequency.json')

    da = DataAnalysis('scriptdata/full_frequency.json')
    da.plot_character_total_words(trange=15)



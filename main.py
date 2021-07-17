from graphcharacter import *
from scraper import *

if __name__ == '__main__':
    main_characters = ['Micheal', 'Dwight', 'Jim', 'Pam', '']
    graph = GraphCharacter('Pam', 'scriptdata/full_frequency.json')
    print(graph.plot_show())

from board import Board

class Game:

    def __init__(self, game_mode):
        self.game_mode = game_mode

    def start(self):
        pass


if __name__ == "__main__":
    mode = ['1 - international',
            '2 - Ganaian',
            '3 - Frisian',
            '4 - Canadian',
            '5 - Brazillian',
            '6 - Pool',
            '7 - Jamaican',
            '8 - Russian',
            '9 - Mozambican',
            '10 - Spanish',
            '11 - Malaysian/Singaporean',
            '12 - Czech',
            '13 - Hungarian Highlander',
            '14 - Argentinian',
            '15 - Thai',
            '16 - German',
            '17 - Turkish',
            '18 - Myanmar',
            '19 - Tanzanian',
            '20 - English',
            '21 - Italian',
            '22 - Gothic',
            '23 - Invent your own rules!!!']

    print('''
    *****************************************************************
    Welcome to the most complete python checkers game in the world!!!
    *****************************************************************
    ''')
    print(*mode, sep='\n')
    game = Game(input('Select mode:\n'))

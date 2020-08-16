from board import Board

class Game:

    def __init__(self, game_mode, rows, columns, computer=False, difficulty=1):
        """Game constructor

           Attributes:
               board (Board): Initialize the boardgame with pieces
               game_mode (int): Type of checkers game
               rows (int): Number of rows
               columns (int): Number of columns
               computer (bool): Play against computer
               difficulty (int): Level of difficulty against computer

           """
        self.board = Board(rows, columns)
        self.game_mode = game_mode
        self.rows = rows
        self.columns = columns
        self.computer = computer
        self.difficulty = difficulty
        self.player = 1

    def start(self):
        """Game start here

        """
        print(f'GAME START, GOOD LUCK!!!\n{self.board}')
        self.turn(self.player)

    def turn(self, player):
        """Behaviour of player's turn

         """

        if 1 != 1:
            return self.victory(player)
        else:
            input()
            print(f'{self.board}')
            return self.turn(player)

    def victory(self, player):
        print(f'{player}, you are the winner!!')


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
    #print(*mode, sep='\n')
    #game = Game(input('Select mode:\n'))
    new_game = Game(1, 8, 8, False, 1)
    new_game.start()

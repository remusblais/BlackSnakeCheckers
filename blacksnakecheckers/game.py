"""
This is the main module where all game logic between the player(s) and computer occur.

"""

__author__ = "Rémus Blais"
__version__ = "0.103"
__date__ = "2020-08-18"

from pyfiglet import Figlet
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
        print(Figlet(font='slant').renderText('Test'))
        self.turn(self.player)

    def turn(self, player):
        """Behaviour of player's turn

         """
        print(self.board)
        if 1 != 1:
            return self.victory(player)
        else:
            move_source = self.source()
            move_target = self.target()
            return self.turn(player)

    def source(self):
        """Ask the player which source

        """
        while True:
            pos_line = input("Source line : ")
            pos_col = input("Source column : ")
            '''if pos_line.isdecimal() and pos_col.isdecimal():
                source = Position(int(pos_line), int(pos_col))
                source_validation = (self.position_source_valide(source))
                if not source_validation[0]:
                    print(source_validation[1])
                else:
                    self.source_selected = source
                    break
            else:
                print(error)'''

        #return source
    
    def source_validation(self):
        pass
    
    def target(self):
        """Ask the player which target

        """
        while True:
            pos_line = input("Target line : ")
            pos_col = input("Target column : ")
            '''if pos_line.isdecimal() and pos_col.isdecimal():
                target = Position(int(pos_line), int(pos_col))
                target_validation = (self.position_cible_valide(target))
                if not target_validation[0]:
                    print(target_validation[1])
                else:
                    break
            else:
                print(error)'''
                
        #return target
    
    def target_validation(self):
        pass

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

    print(Figlet(font='slant').renderText('Black\nSnake\nCheckers') + __version__)
    #print(*mode, sep='\n')
    #game = Game(input('Select mode:\n'))
    new_game = Game(1, 8, 8, False, 1)
    new_game.start()
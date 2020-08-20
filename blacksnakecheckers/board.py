from position import Position as Pos

class Board:

    def __init__(self, rows, columns):
        self.x_spaces = columns
        self.y_spaces = rows

        self.spaces = {
            Pos(7, 0): 'o',
            Pos(7, 2): 'o',
            Pos(7, 4): 'o',
            Pos(7, 6): 'o',
            Pos(6, 1): 'o',
            Pos(6, 3): 'o',
            Pos(6, 5): 'o',
            Pos(6, 7): 'o',
            Pos(5, 0): 'o',
            Pos(5, 2): 'o',
            Pos(5, 4): 'o',
            Pos(5, 6): 'o',
            Pos(2, 1): 'x',
            Pos(2, 3): 'x',
            Pos(2, 5): 'x',
            Pos(2, 7): 'x',
            Pos(1, 0): 'x',
            Pos(1, 2): 'x',
            Pos(1, 4): 'x',
            Pos(1, 6): 'x',
            Pos(0, 1): 'x',
            Pos(0, 3): 'x',
            Pos(0, 5): 'x',
            Pos(0, 7): 'x',
        }

    def __repr__(self):
        """ Showcase the entire boardgame grid """

        hor_bar = '\u2500'  # ─
        ver_bar = '\u2502'  # │
        cross_bar = '\u253c'  # ┼

        boardgame = f' {cross_bar}'
        for num in range(self.x_spaces):
            boardgame += f'{hor_bar}{str(num)}{hor_bar}{cross_bar}'
        boardgame += '\n'

        for x in range(0, self.y_spaces):
            row_separator = f'{hor_bar * 3}{cross_bar}'
            boardgame += f'{str(x)}{ver_bar} '
            for y in range(0, self.x_spaces):
                if Pos(x, y) in self.spaces:
                    print(112)
                    boardgame += str(self.spaces[Pos(x, y)])+" | "
                else:
                    boardgame += f'  {ver_bar} '
            boardgame += f'\n {cross_bar}{row_separator * self.x_spaces}\n'

        return boardgame




if __name__ == '__main__':
    print(Pos(2, 2))
    print(repr(Board(8, 8)))


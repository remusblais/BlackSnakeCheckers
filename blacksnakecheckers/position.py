class Position:

    def __init__(self, row, column):
        """Position class construction, will define the position on the x axis (column) and y axis (row)

        Args:
            row (int): row position (y axis)
            column (int): column position (x axis)

        """
        self.row = int(row)
        self.column = int(column)

    def diagonal_move(self, step=1, direction='both', limit=True):
        """TBC

        Returns:
            list:

        """
        up = [Position(self.row - step, self.column - step), Position(self.row - step, self.column + step)]
        down =[Position(self.row + step, self.column - step), Position(self.row + step, self.column + step)]
        both = up + down

        if direction == 'up':
            return up
        elif direction == 'down':
            return down
        elif direction == 'both':
            return both

    def __repr__(self):
        """To print the position as a chain of characters

        """
        return f'({self.row}, {self.column})'

    def __hash__(self):
        """To allow position as key in a dictionary

        """
        return hash(str(self))

    def __eq__(self, other):
        """Compare actual position with original value

        """
        return self.row == other.row and self.column == other.column

test = Position(2, 2)
print(test.diagonal_move(4, 'down'))
class Position:

    def __init__(self, row, column):
        """Position class construction, will define the position on the x axis (column) and y axis (row)

        Args:
            row (int): row position (y axis)
            column (int): column position (x axis)

        """
        self.row = int(row)
        self.column = int(column)

    def diagonal_move(self, step=0, direction='all', limit=True):
        """TBC

        Returns:
            list:

        """
        result = []
        parameters = [['-', '-'], ['-', '+'], ['+', '-'], ['+', '+']]

        if direction == 'up':
            parameters = parameters[:2]

        if direction == 'down':
            parameters = parameters[2:4]


        x = 0
        for i in enumerate(parameters):
            result.extend(eval(f'[Position(self.row {parameters[x][0]} {step}, self.column {parameters[x][1]} {step})]'))
            x += 1

        return result

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
print(test.diagonal_move(2, 'all'))
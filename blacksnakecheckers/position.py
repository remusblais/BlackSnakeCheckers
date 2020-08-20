class Position:

    def __init__(self, row, column):
        """Position class construction, will define the position on the x axis (column) and y axis (row)

        Args:
            row (int): row position (y axis)
            column (int): column position (x axis)

        """
        self.row = int(row)
        self.column = int(column)

    def __hash__(self):
        """To allow position as key in a dictionary

        """
        return hash(str(self))

    def __repr__(self):
        """To print the position as a chain of characters

        """
        return f'({self.row}, {self.column})'

class Piece:
    """Constructor for every piece

    """
    def __init__(self, color_of_piece, type_of_piece):

        self.color = color_of_piece
        self.type = type_of_piece

    def pawn(self):
        """

        Returns:
            (bool) : True is piece is pawn

        """
        return self.type == "pawn"

    def king(self):
        """

        Returns:
            (bool) : True if piece is king

        """
        return self.type == "king"

    def white(self):
        """

        Returns:
            (bool) : True if piece white

        """
        return self.color == "white"

    def black(self):
        """

        Returns:
            (bool) : True if piece is black

        """
        return self.color == "black"

    def promotion(self):
        """Promote the current piece (eg. pawn to king)

        """
        self.type = "king"

    def __repr__(self):
        """Print the piece

        """
        if self.white() and self.pawn():
            return "o"

        if self.white() and self.king():
            return "O"

        if self.black() and self.pawn():
            return "x"

        if self.black() and self.king():
            return "x"

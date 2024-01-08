class Piece:
    # piece has pos and color
    def __init__(self, i, j, color):
        self.i = i
        self.j = j
        self.color = color

    def name(self):
        return self.color[0] + "P"

    # piece has valid moves
    def get_valid_moves(self, chess_board):
        return [(i, j) for i in range(8) for j in range(8)]
    
    # if the pieces were to have feelings, they should be aware of when they would be captured
    def can_be_captured(self, chess_board):
        return False


class King(Piece):
    def __init__(self, i, j, color):
        super().__init__(i, j, color)

    def name(self):
        return self.color[0] + "K"

    # the king can move 1 step in any directions, but must not move to be checked
    def get_valid_moves(self, chess_board):
        valid_moves = []
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if (di, dj) == (0, 0):
                    continue
                i = self.i + di
                j = self.j + dj
                valid_moves.append((i, j))
        return valid_moves


class Queen(Piece):
    def __init__(self, i, j, color):
        super().__init__(i, j, color)

    def name(self):
        return self.color[0] + "Q"

    # the queen can move in any directions
    def get_valid_moves(self, chess_board):
        valid_moves = []
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if (di, dj) == (0, 0):
                    continue
                i = self.i + di
                j = self.j + dj
                while 0 <= i <= 7 and 0 <= j <= 7:
                    valid_moves.append((i, j))
        return valid_moves

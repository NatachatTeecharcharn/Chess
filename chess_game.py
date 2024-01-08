# chess game has chess board, and is fun to play!
class ChessGame:
    def __init__(self, board):
        self.turn = 0  # 0 for white, 1 for black
        self.board = ChessBoard(board)

    # change turn
    def update_turn(self):
        self.turn = (self.turn + 1) % 2

    # game loop
    def play(self):  
        running = True
        while running:
            self.board.show()

            command = input()
            command = command.split()
            if command[0] == "quit":
                running = False
                print("GOODBYE")
            elif command[0] == "move":
                i1, j1, i2, j2 = command[1:5]
                self.board.move((i1, j1), (i2, j2))


# chess board has pieces
class ChessBoard:
    def __init__(self, board):
        self.board = self._parse_board(board)
    
    def _parse_board(self, board):
        new_board = [[None for j in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if piece != "  ":
                    new_board[i][j] = Queen(i, j, "white")
                else:
                    new_board[i][j] = None
        return new_board

    # move piece from one place to another
    def move(self, ij1, ij2):
        i1, j1 = ij1
        i2, j2 = ij2
        if board[i1][j1]:
            if not board[i2][j2]:
                board[i2][j2] = board[i1][j1].copy()
                board[i1][j1] = None

    # print board on terminal
    def show(self):
        output = [[".." for j in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                if self.board[i][j]:
                    output[i][j] = self.board[i][j].name()
        
        for row in output:
            print(" ".join(row))


class Piece:
    # piece has pos and color
    def __init__(self, i, j, color):
        self.i = i
        self.j = j
        self.color = color

    def name(self):
        return self.color[0] + "P"

    # piece has valid moves
    def get_valid_moves(self, board):
        return [(i, j) for i in range(8) for j in range(8)]


class Queen(Piece):
    def __init__(self, i, j, color):
        super().__init__(i, j, color)

    def name(self):
        return self.color[0] + "Q"

    # the queen can move in straight lines and diagonals
    def get_valid_moves(self, board):
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


if __name__ == "__main__":
    board = [
        ["  ", "  ", "  ", "  ", "bK", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "wQ", "wK", "  ", "  ", "  "]
    ]
    chess_game = ChessGame(board)
    chess_game.play()

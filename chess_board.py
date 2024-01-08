from chess_pieces import King, Queen


# chess board has pieces
class ChessBoard:
    def __init__(self, board):
        self.board = self._parse_board(board)
    
    def _parse_board(self, board):
        new_board = [[None for j in range(8)] for i in range(8)]
        pieces = {
            "K": lambda i, j, color: King(i, j, color),
            "Q": lambda i, j, color: Queen(i, j, color),
        }
        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if piece != "  ":
                    color = piece[0]
                    piece_type = piece[1]
                    new_board[i][j] = pieces[piece_type](i, j, color)
                else:
                    new_board[i][j] = None
        return new_board

    # move piece from one place to another, only if it is a valid move
    def move(self, ij1, ij2):
        i1, j1 = ij1
        i2, j2 = ij2
        piece = self.board[i1][j1]
        if piece:
            if (i2, j2) in piece.get_valid_moves(self):
                piece.move((i2, j2))
                self.board[i2][j2] = piece
                self.board[i1][j1] = None

    # print board on terminal
    def show(self):
        output = [[".." for j in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                if self.board[i][j]:
                    output[i][j] = self.board[i][j].name()
        
        for row in output:
            print(" ".join(row))

from chess_board import ChessBoard


# chess game has chess board, and is fun to play!
class ChessGame:
    def __init__(self, board):
        self.turn = 0  # 0 for white, 1 for black
        self.chess_board = ChessBoard(board)

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
                i1, j1, i2, j2 = map(int, command[1:5])
                self.board.move((i1, j1), (i2, j2))


if __name__ == "__main__":
    board = [
        ["  ", "  ", "  ", "  ", "  ", "  ", "bK", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "wK", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "wQ", "  ", "  ", "  "]
    ]
    chess_game = ChessGame(board)
    chess_game.play()

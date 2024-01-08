import pygame as pg
import sys

from settings import *
from utils import load_images, create_board_surf, draw_pieces, draw_square
from chess_game import ChessGame


class ChessInterface:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()

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
        self.chess_game = ChessGame(board)

        self.images = load_images()  # cache an image
        self.board_surf = create_board_surf()  # a background, should not be changed

        self.is_selecting = False
        self.selected_ij = (-1, -1)

    def run(self):
        while True:
            mouse_pos = pg.mouse.get_pos()
            mouse_pressed = pg.mouse.get_pressed()
            mouse_rel = pg.mouse.get_rel()
            
            left_pressed = mouse_pressed[0]
            mouse_ij = (mouse_pos[1] // SQUARE_SIZE, mouse_pos[0] // SQUARE_SIZE)

            self.screen.blit(self.board_surf, (0, 0))
            
            draw_square(self.screen, (250, 20, 20), (mouse_ij[1] * SQUARE_SIZE, mouse_ij[0] * SQUARE_SIZE))



            draw_pieces(self.images, self.screen, self.chess_game.chess_board)

            if self.is_selecting:
                piece = self.chess_game.chess_board.board[self.selected_ij[0]][self.selected_ij[1]]
                if piece:
                    piece.draw_valid_moves(self.screen, self.chess_game.chess_board)

                draw_square(self.screen, (250, 200, 50), (mouse_ij[1] * SQUARE_SIZE, mouse_ij[0] * SQUARE_SIZE))

                if not left_pressed:
                    self.chess_game.move(self.selected_ij, mouse_ij)

                    self.is_selecting = False
            else:
                if left_pressed:
                    self.selected_ij = mouse_ij
                    self.is_selecting = True
    

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == pg.BUTTON_RIGHT:
                        print(self.selected_ij)
                        self.chess_game.chess_board.show()
                        print()
            
            pg.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = ChessInterface()
    game.run()

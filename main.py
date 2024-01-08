import pygame as pg
import sys

from settings import *
from utils import load_images, create_board_surf, draw_pieces
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

    def run(self):
        while True:
            mouse_pos = pg.mouse.get_pos()
            mouse_pressed = pg.mouse.get_pressed()
            mouse_rel = pg.mouse.get_rel()

            self.screen.blit(self.board_surf, (0, 0))
            draw_pieces(self.images, self.screen, self.chess_game.chess_board)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
            pg.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = ChessInterface()
    game.run()

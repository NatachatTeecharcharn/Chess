import pygame as pg
import sys

from settings import *
from utils import load_images, create_board_surf, draw_pieces
from chess_game import ChessGame

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()

images = load_images()  # cache an image

board_surf = create_board_surf()  # a background, should not be changed

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

    while True:
        mouse_pos = pg.mouse.get_pos()
        mouse_pressed = pg.mouse.get_pressed()
        mouse_rel = pg.mouse.get_rel()

        screen.blit(board_surf, (0, 0))
        draw_pieces(images, screen, chess_game.chess_board)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
        pg.display.update()
        clock.tick(FPS)

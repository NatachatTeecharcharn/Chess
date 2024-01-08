import pygame as pg

from settings import *

# create board surface
def create_board_surf():
    board_surf = pg.Surface((BOARD_SIZE, BOARD_SIZE))
    for i in range(8):
        x = SQUARE_SIZE * i
        for j in range(8):
            y = SQUARE_SIZE * j
            if (i + j) % 2 == 0:
                color = LIGHT_SQUARE_COLOR
            else:
                color = DARK_SQUARE_COLOR
            pg.draw.rect(board_surf, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))
    return board_surf

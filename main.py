import pygame as pg
import sys

from settings import *
from pieces import Piece


pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()


# create board surface
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


# set up images
pieces_image = {}
for i, color in enumerate("bw"):
    for j, piece_type in enumerate("BKNpQR"):
        piece_name = color + piece_type 
        pieces_image[piece_name] = pg.image.load(f"images/{piece_name}.png").convert_alpha()


wK = Piece("w", 0, 0)


while True:
    mouse_pos = pg.mouse.get_pos()
    mouse_pressed = pg.mouse.get_pressed()
    mouse_rel = pg.mouse.get_rel()

    wK.update(mouse_pos, mouse_pressed, mouse_rel)

    screen.fill((0, 0, 0))
    screen.blit(board_surf, (0, 0))
    screen.blit(wK.image, wK.get_pos())

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    pg.display.update()
    clock.tick(FPS)

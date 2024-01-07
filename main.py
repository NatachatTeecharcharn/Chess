import pygame as pg
import sys

pg.init()
WIDTH = 600
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pg.time.Clock()

# create board surface
SQUARE_SIZE = 60
LIGHT_SQUARE_COLOR = (200, 200, 200)
DARK_SQUARE_COLOR = (50, 50, 50)
board_surf = pg.Surface((SQUARE_SIZE * 8, SQUARE_SIZE * 8))
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
PIECE_SIZE = 60
pieces_image = {}
for i in range(2):
    x = PIECE_SIZE * i
    for j in range(6):
        y = PIECE_SIZE * j

# test loading an image
black_queen_image = pg.image.load("ChessPiecesArray.png").convert()


while True:
    screen.fill((0, 0, 0))
    screen.blit(board_surf, (0, 0))

    screen.blit(black_queen_image, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    pg.display.update()
    clock.tick(FPS)

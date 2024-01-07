import pygame as pg
import sys

pg.init()
WIDTH = 600
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pg.time.Clock()

# create board surface
SQUARE_WIDTH = 60
LIGHT_SQUARE_COLOR = (200, 200, 200)
DARK_SQUARE_COLOR = (50, 50, 50)
board_surf = pg.Surface((SQUARE_WIDTH * 8, SQUARE_WIDTH * 8))
for i in range(8):
    x = SQUARE_WIDTH * i
    for j in range(8):
        y = SQUARE_WIDTH * j
        if (i + j) % 2 == 0:
            color = LIGHT_SQUARE_COLOR
        else:
            color = DARK_SQUARE_COLOR
        pg.draw.rect(board_surf, color, (x, y, SQUARE_WIDTH, SQUARE_WIDTH))

while True:
    screen.fill((0, 0, 0))
    screen.blit(board_surf, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    pg.display.update()
    clock.tick(FPS)

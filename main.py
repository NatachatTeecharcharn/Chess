import pygame as pg
import sys

from settings import *
from utils import create_board_surf

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()

board_surf = create_board_surf()

if __name__ == "__main__":

    while True:
        mouse_pos = pg.mouse.get_pos()
        mouse_pressed = pg.mouse.get_pressed()
        mouse_rel = pg.mouse.get_rel()

        screen.fill((0, 0, 0))
        screen.blit(board_surf, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
        pg.display.update()
        clock.tick(FPS)

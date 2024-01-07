import pygame as pg
import sys

pg.init()
WIDTH = 500
HEIGHT = 500
screen = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    clock.tick(FPS)

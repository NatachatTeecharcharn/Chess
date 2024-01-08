import pygame as pg
import sys

from settings import *


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()


# set up images
pieces_image = {}
for i, color in enumerate("bw"):
    for j, piece_type in enumerate("BKNpQR"):
        piece_name = color + piece_type 
        pieces_image[piece_name] = pg.image.load(f"images/{piece_name}.png").convert_alpha()


# drag-and-drop-able Piece Class
class Piece(pg.sprite.Sprite):
    def __init__(self, color, i, j) -> None:
        super().__init__()

        self.image = pieces_image["wK"]

        self.color = color

        self.i = i
        self.j = j

        x = i * SQUARE_SIZE
        y = j * SQUARE_SIZE
        self.rect = pg.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)

        self.is_focus = False

    def is_selecting(self, mouse_pos, mouse_pressed):  # True if is being left-clicked on, until dropping
        is_mouse_hovering = self.rect.collidepoint(mouse_pos)
        is_mouse_left_click = mouse_pressed[0]
        if is_mouse_hovering and is_mouse_left_click:
            self.is_focus = True
        elif not is_mouse_left_click:
            self.is_focus = False

        return self.is_focus

    def update(self, mouse_pos, mouse_pressed, mouse_rel):
        if self.is_selecting(mouse_pos, mouse_pressed):
            self.rect.x += mouse_rel[0]
            self.rect.y += mouse_rel[1]
        else:
            self.rect.x = ((self.rect.x + 30) // SQUARE_SIZE) * SQUARE_SIZE
            self.rect.y = ((self.rect.y + 30) // SQUARE_SIZE) * SQUARE_SIZE

            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > BOARD_SIZE - SQUARE_SIZE:
                self.rect.x = BOARD_SIZE - SQUARE_SIZE
            
            if self.rect.y < 0:
                self.rect.y = 0
            elif self.rect.y > BOARD_SIZE - SQUARE_SIZE:
                self.rect.y = BOARD_SIZE - SQUARE_SIZE

    def get_pos(self): # return x, y coordinate (top left)
        return self.rect.x, self.rect.y


class Board:
    def __init__(self):
        # create board surface
        self.surf = pg.Surface((BOARD_SIZE, BOARD_SIZE))
        for i in range(8):
            x = SQUARE_SIZE * i
            for j in range(8):
                y = SQUARE_SIZE * j
                if (i + j) % 2 == 0:
                    color = LIGHT_SQUARE_COLOR
                else:
                    color = DARK_SQUARE_COLOR
                pg.draw.rect(self.surf, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

    def render(self, screen):
        screen.blit(board.surf, (0, 0))

        for i in range(8):
            row = self.board[i]
            for j in range(8):
                piece = row[j]
                if piece != "  ":
                    screen.blit(pieces_image[piece], (j * SQUARE_SIZE, i * SQUARE_SIZE))

board = Board()


# game loop
while True:
    mouse_pos = pg.mouse.get_pos()
    mouse_pressed = pg.mouse.get_pressed()
    mouse_rel = pg.mouse.get_rel()

    screen.fill((0, 0, 0))
    board.render(screen)


    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    pg.display.update()
    clock.tick(FPS)

import pygame as pg

from settings import *


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
        else:  # 
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

            self.i = self.rect.y // SQUARE_SIZE
            self.j = self.rect.x // SQUARE_SIZE

    def get_pixel_pos(self): # return x, y coordinate (top left)
        return self.rect.x, self.rect.y
    
    def get_board_pos(self):
        return self.i, self.j

    def get_valid_moves(self):
        return [(i, j) for i in range(8) for j in range(8)]


class Queen(Piece):
    def __init__(self, color, i, j):
        super().__init__(color, i, j)
    
    def get_valid_moves(self):
        valid_moves = []

        return valid_moves
    
import pygame as pg
import sys


pg.init()
WIDTH = 600
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 30
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

    def is_selecting(self, mouse_pos, mouse_pressed):  # True if is being left-clicked on
        is_mouse_hovering = self.rect.collidepoint(mouse_pos)
        is_mouse_left_click = mouse_pressed[0]
        if is_mouse_hovering and is_mouse_left_click:
            return True
        else:
            return False

    def update(self, mouse_pos, mouse_pressed, mouse_rel):
        if self.is_selecting(mouse_pos, mouse_pressed):
            self.rect.x += mouse_rel[0]
            self.rect.y += mouse_rel[1]

    def get_pos(self): # return x, y coordinate (top left)
        return self.rect.x, self.rect.y


wK = Piece("w", 0, 0)


while True:
    mouse_pos = pg.mouse.get_pos()
    mouse_pressed = pg.mouse.get_pressed()
    mouse_rel = pg.mouse.get_rel()
    print(mouse_rel)

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

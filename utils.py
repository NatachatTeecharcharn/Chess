import pygame as pg

from settings import *

def load_images():
    images = {}
    for color in "bw":
        for piece_type in "BKNpQ":
            piece_name = color + piece_type
            images[piece_name] = pg.image.load(f"pieces_image/{piece_name}.png").convert_alpha()
    return images

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

# draw pieces on surf
def draw_pieces(images, surf, chess_board):
    for i in range(8):
        for j in range(8):
            piece = chess_board.board[i][j]
            if piece:
                image = images[piece.name()]
                x = j * SQUARE_SIZE
                y = i * SQUARE_SIZE
                surf.blit(image, (x, y))

# draw hollow square
def draw_square(surf, color, xy):
    x, y = xy
    pg.draw.rect(surf, color, (x, y, SQUARE_SIZE, SQUARE_SIZE), 3)

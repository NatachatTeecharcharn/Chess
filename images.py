import pygame as pg

def load_images(): # set up images
    pieces_image = {}
    for i, color in enumerate("bw"):
        for j, piece_type in enumerate("BKNpQR"):
            piece_name = color + piece_type 
            pieces_image[piece_name] = pg.image.load(f"pieces_image/{piece_name}.png").convert_alpha()
    return pieces_image

import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, x, filename):
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))
    def move_left(self):
        self.rect.x -= 1
    def move_right(self):
        self.rect.x += 1
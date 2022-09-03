import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, x, filename):
        self.image = pg.image.load(filename)
        self.rect = self.image.get_rect(center=(x, 200))
        self.image.set_colorkey((255, 255, 255))
    def move_left(self):
        pg.transform.flip(self.image, True, False)
        self.rect.x -= 1
    def move_right(self):
        pg.transform.flip(self.image, True, False)
        self.rect.x += 1
    def kill(self):
        self.kill()
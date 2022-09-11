import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, x, filename):
        self.filename = filename
        self.image = pg.image.load(self.filename)
        self.rect = self.image.get_rect(center=(x, 200))
        self.image.set_colorkey((255, 255, 255))
    def move_left(self):
        self.image = pg.image.load(f'{self.filename[0:len(self.filename) - 4]}_left.png')
        pg.transform.flip(self.image, True, False)
        self.rect.x -= 1
    def move_right(self):
        self.image = pg.image.load(f'{self.filename[0:len(self.filename) - 4]}_right.png')
        pg.transform.flip(self.image, True, False)
        self.rect.x += 1
    def default_pos(self):
        self.image = pg.image.load(self.filename)
        pg.transform.flip(self.image, True, False)
    def kill(self):
        self.kill()
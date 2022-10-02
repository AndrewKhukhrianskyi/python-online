import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, x, filename):
        self.hp = 3
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
    def get_hit(self):
        self.hp -= 1
    def check_player_hp(self):
        if self.hp == 2:
            hp_icon = pg.image.load('heart_2hp.png')
        elif self.hp == 1:
            hp_icon = pg.image.load('heart_1hp.png')
        else:
            hp_icon = pg.image.load('heart.png')
        return hp_icon
    def kill(self):
        self.kill()
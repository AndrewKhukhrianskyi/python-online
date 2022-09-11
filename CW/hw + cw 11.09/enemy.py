from time import sleep
import pygame as pg

from random import randint

class Enemy(pg.sprite.Sprite):
    def __init__(self, filename, group):
        pg.sprite.Sprite.__init__(self)
        self.filename = filename
        self.image = pg.image.load(self.filename)
        self.rect = self.image.get_rect(center=(randint(1, 500), 0))
        self.add(group)

    def random_speed(self):
        return randint(1,3)

    def update(self):
        if self.rect.y >= 500:
            self.kill() # "Убивает" объект (удаляет объект) 
        else:
            self.rect.y += self.random_speed()

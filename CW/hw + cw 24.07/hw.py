import pygame as pg

from time import sleep
from random import choice, randint

import button # Custom Method
WHITE = (255,255,255)
RED = (255, 0, 0)
BLACK = (0,0,0)

color_list = [WHITE, RED, BLACK]

class Screen:
    def __init__(self, x : int, y : int, lst = color_list):
        self.x = x
        self.y = y
        self.FPS = 60
        self.screen = pg.display.set_mode((self.x, self.y))
        self.screen.fill(WHITE)
        self.lst = lst
        self.button_var = button.Button()

    def button_create(self):
        self.button_var.create_button(surface=self.screen,
                                 color = self.lst[1], # RED
                                 x = self.x // 2,
                                 y = self.y // 2,
                                 length = 100,
                                 height = 100,
                                 width = 100,
                                 text = 'BUTTON',
                                 text_color=self.lst[2]) # BLACK
        
    

    def run(self):
        is_run = True
        self.button_create()
        while is_run:
            press = pg.key.get_pressed()
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    is_run = False
                if i.type == pg.MOUSEBUTTONDOWN:
                    self.button_var.pressed(mouse=pg.mouse.get_pos(),
                                            text_list = ['Тык', "Снова тык.", "Поздравляю. Ты тыкнул на меня.",
                                            "Ух ты. Это снова тык.", "Произошел нервный ТЫК. Обожаю каламбур!", "Не устал еще?"])
            
            pg.display.update()
            pg.time.Clock().tick(self.FPS)

screen = Screen(600, 400)

if __name__ == '__main__':
    screen.run()
        

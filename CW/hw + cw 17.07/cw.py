from time import sleep
import pygame as pg

from random import choice

class Screen:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
        self.list_name = ['Марио', "Крестики-Нолики", "Сапер", 
                           "Пасъянс", "Косынка", "Паук", "Brawl Stars",
                           "Minecraft", "Бобер"]

    def draw_screen(self):
        pg.display.set_mode((self.x, self.y))
    
    def rename_game(self):
        pg.init()
        pg.display.set_caption(choice(self.list_name))

    def run(self):
        is_run = True
        while is_run:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    is_run = False
                elif i.type == pg.
            self.rename_game()

screen = Screen(600, 400)
screen.draw_screen()
if __name__ == '__main__':
    screen.run()




        

from time import sleep
import pygame as pg

from random import choice

class Screen:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
        self.list_name = [str(elem) for elem in range(5)] # '0', '1', '2' ...
        self.FPS = 60

    def draw_screen(self):
        pg.display.set_mode((self.x, self.y))
    
    def rename_game(self):
        pg.init()
        pg.display.set_caption(choice(self.list_name))
    
    def fixed_rename(self, move):
        try:
            if move == '+':
                finder = self.list_name.index(pg.display.get_caption()[0])
                finder += 1
                pg.display.set_caption(self.list_name[finder])
            elif move == '-':
                finder = self.list_name.index(pg.display.get_caption()[0])
                finder -= 1
                pg.display.set_caption(self.list_name[finder])
            else:
                print('Некорректное назначение передвижения!')
            print(f"CURRENT INDEX IS: {finder}")
        except IndexError:
            print('Вышли за пределы списка имен!')

    def run(self):
        is_run = True
        name = choice(self.list_name)
        pg.display.set_caption(name)
        

        while is_run:
            press = pg.key.get_pressed()
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    is_run = False
            
            if press[pg.K_RIGHT]:
                self.fixed_rename('+')
            elif press[pg.K_LEFT]:
                self.fixed_rename('-')
            
            pg.display.update()
            pg.time.Clock().tick(self.FPS)

screen = Screen(600, 400)
screen.draw_screen()
if __name__ == '__main__':
    screen.run()




        

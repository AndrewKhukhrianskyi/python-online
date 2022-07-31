from time import sleep
import pygame as pg

from random import choice, randint
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

color_list = [WHITE, RED, GREEN, BLUE]

class Screen:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
        self.list_name = [str(elem) for elem in range(5)] # '0', '1', '2' ...
        self.FPS = 60
        self.screen = pg.display.set_mode((self.x, self.y))
        self.screen.fill(WHITE)
        
    
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
    
    def random_color_screen(self):
        random_color = (randint(0, 255), randint(0, 255), randint(0,255))
        print(random_color)
        self.screen.fill(random_color)
    
    def draw_random_line(self):
        print('LINE')
        pg.draw.aaline(self.screen, 
                    color = (randint(0, 255), randint(0, 255), randint(0, 255)), 
                    start_pos = [randint(0, self.x - 100), randint(0, self.x - 100)], 
                    end_pos =[randint(0, self.x - 100), randint(0, self.x - 100)])

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
            elif press[pg.K_1]:
                sleep(2)
                self.draw_random_line()
            elif press[pg.K_2]:
                sleep(2)
                self.random_color_screen()
            
            pg.display.update()
            pg.time.Clock().tick(self.FPS)

screen = Screen(600, 400)

if __name__ == '__main__':
    screen.run()
        

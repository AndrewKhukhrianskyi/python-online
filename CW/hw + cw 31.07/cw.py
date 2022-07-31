import pygame as pg

from time import sleep
from random import choice, randint

WHITE = (255,255,255)

class Screen:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
        self.FPS = 60
        self.screen = pg.display.set_mode((self.x, self.y))
    
    def change_random_color(self, object_color = False):
        if not object_color:
            self.screen.fill((randint(0, 255), randint(0,255), randint(0,255)))
        else:
            return (randint(0, 255), randint(0,255), randint(0,255))
    
    def get_random_coords(self):
        return randint(self.x // 4, self.x // 2), randint(self.y // 4, self.y // 2)
    
    def draw_random_circle(self):
        pg.draw.circle(self.screen,
                        color = self.change_random_color(object_color=True),
                        center=self.get_random_coords(),
                        radius=float(randint(10, 50))) # 10.0 (Example)
    
    def circle_rain(self, amount = randint(5, 50)):
        for draw in range(amount):
            sleep(1)
            self.draw_random_circle()
    

    def run(self):
        is_run = True
        while is_run:
            press = pg.key.get_pressed()
            mouse_press = pg.mouse.get_pressed(num_buttons=3)
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    is_run = False
                    
            
            if press[pg.K_1]:
                sleep(2)
                self.change_random_color()
            
            elif press[pg.K_2]:
                sleep(2)
                self.draw_random_circle()
            
            elif press[pg.K_3]:
                self.circle_rain()
            
            elif mouse_press:
                pg.mouse.get_pos()
          
            pg.display.update()
            pg.time.Clock().tick(self.FPS)

screen = Screen(600, 400)

if __name__ == '__main__':
    screen.run()
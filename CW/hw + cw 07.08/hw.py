import pygame as pg

from random import randint, choice
from time import sleep
'''
def fill_color(surface):
    surface.fill(randint(0,255), randint(0,255), randint(0,255),)

def draw_object(surface, object_type = None):
    object_types = ('rect', 'circle', 'triangle')
    if object_type is None:
        object_type = choice(object_types)

    if object_type in object_types:
        if object_type == 'rect':
            rect = pg.Rect(randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50))
            pg.draw.rect(surface, RED, rect)
        elif object_type == 'circle':
            coordinate = (randint(0, 50), randint(0, 50))
            radius = randint(2, 10)
            pg.draw.circle(surface, GREEN, coordinate, radius)
        elif object_type == 'triangle':
            points = [(randint(5, 50), randint(5, 50)),
                      (randint(5, 50), randint(5, 50)),
                      (randint(5, 50), randint(5, 50))]
            pg.draw.polygon(surface, BLUE, points)
    else:
        print(f'Error: {object_type} is invalid!')

# NO OOP
# Constant variables (Константы)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Основная логика
x, y = 400, 400 # Размер экрана
screen = pg.display.set_mode((x, y)) # Отрисовка экрана
FPS = 60 # Кадры
is_run = True # Запуск игры

surf = pg.Surface(size=(300, 300)) # Поверхность (холст) для отрисовки.
surf.fill(WHITE)
while is_run:
    pg.display.update()
    press = pg.key.get_pressed()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_run = False
    screen.blit(source = surf,
                dest = (x // 2, y // 2))
    
    if press[pg.K_1]:
        draw_object(surf, 'rect')
    elif press[pg.K_2]:
        draw_object(surf, 'circle')
    elif press[pg.K_3]:
        draw_object(surf, 'triangle')
    elif press[pg.K_4]:
        draw_object(surf)
    elif press[pg.K_5]:
        surf.fill(WHITE)

    pg.time.Clock().tick(FPS)
'''
# OOP
# Constant variables (Константы)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 60
class Screen:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.screen = pg.display.set_mode((self.x, self.y)) 
        self.surface = pg.Surface(size=(300, 300))
        self.surface.fill(WHITE)

    def fill_color(self):
        self.surface.fill(randint(0,255), randint(0,255), randint(0,255),)

    def draw_object(self, object_type = None):
        object_types = ('rect', 'circle', 'triangle')
        if object_type is None:
            object_type = choice(object_types)

        if object_type in object_types:
            if object_type == 'rect':
                rect = pg.Rect(randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50))
                pg.draw.rect(self.surface, RED, rect)
            elif object_type == 'circle':
                coordinate = (randint(0, 50), randint(0, 50))
                radius = randint(2, 10)
                pg.draw.circle(self.surface, GREEN, coordinate, radius)
            elif object_type == 'triangle':
                points = [(randint(5, 50), randint(5, 50)),
                        (randint(5, 50), randint(5, 50)),
                        (randint(5, 50), randint(5, 50))]
                pg.draw.polygon(self.surface, BLUE, points)
        else:
            print(f'Error: {object_type} is invalid!')

    def run(self):
        is_run = True 
        while is_run:
            pg.display.update()
            press = pg.key.get_pressed()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    is_run = False
            self.screen.blit(source = self.surface,
                            dest = (self.x // 2, self.y // 2))
            
            if press[pg.K_1]:
                sleep(1)
                self.draw_object('rect')
            elif press[pg.K_2]:
                sleep(1)
                self.draw_object('circle')
            elif press[pg.K_3]:
                sleep(1)
                self.draw_object('triangle')
            elif press[pg.K_4]:
                sleep(1)
                self.draw_object()
            elif press[pg.K_5]:
                self.surface.fill(WHITE)

            pg.time.Clock().tick(FPS)


screen = Screen(400, 400)
screen.run()


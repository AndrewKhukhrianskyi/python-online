# Without OOP (Решение без ООП для понимания)
import pygame as pg

from random import randint

# Constant variables (Константы)
BLACK = (0,0,0)
# Основная логика
x, y = 400, 400 # Размер экрана
screen = pg.display.set_mode((x, y)) # Отрисовка экрана
FPS = 60 # Кадры
is_run = True # Запуск игры
x1, y1, x2, y2 = 10, 10, 20, 20 # Координаты объекта

square = pg.Rect(x1, y1, x2, y2) # Сущность объекта (задаем координаты нашего квадрата)

def get_rnd_color():
    return randint(0, 255), randint(0, 255), randint(0,255)

while is_run:
    pg.display.update()
    press = pg.key.get_pressed()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_run = False
    screen.fill(BLACK)
    
    if press[pg.K_LEFT]:
        square.move_ip(-5, 0)
    elif press[pg.K_RIGHT]:
        square.move_ip(5, 0)
    elif press[pg.K_UP]:
        square.move_ip(0, -5)
    elif press[pg.K_DOWN]:
        square.move_ip(0, 5)


    pg.draw.rect(screen, get_rnd_color(), square, 0)
               
    pg.time.Clock().tick(FPS)

# ООП
class Screen:
    def __init__(self, width, height, coords):
        self.width = width
        self.height = height
        self.rect = pg.Rect(coords)
        self.FPS = 60
        self.color = randint(0, 255), randint(0, 255), randint(0,255)
        self.BLACK = (0, 0, 0)

    def run(self):
        is_run = True
        screen = pg.display.set_mode((self.width, self.height))

        while is_run:
            pg.display.update()
            press = pg.key.get_pressed()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    is_run = False
                    
            if press[pg.K_LEFT]:
                self.rect.move_ip(-5, 0)
            elif press[pg.K_RIGHT]:
                self.rect.move_ip(5, 0)
            elif press[pg.K_UP]:
                self.rect.move_ip(0, -5)
            elif press[pg.K_DOWN]:
                self.rect.move_ip(0, 5)

            screen.fill(self.BLACK)
            pg.draw.rect(screen, self.color, self.rect, 0)
            pg.time.Clock().tick(self.FPS)

game = Screen(500, 500, (25, 25, 50, 50))
game.run()

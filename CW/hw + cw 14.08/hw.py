import pygame as pg

from random import randint
"""
def get_rnd_color():
    return randint(0, 255), randint(0, 255), randint(0,255)

# Constant variables (Константы)
BLACK = (0,0,0)
RED = (255, 0, 0) 
BLUE = (0, 0, 255)
# Основная логика
x, y = 400, 400 # Размер экрана
screen = pg.display.set_mode((x, y)) # Отрисовка экрана
FPS = 60 # Кадры
is_run = True # Запуск игры

x1, y1, x2, y2 = 10, 10, 20, 20 # Координаты объекта
rect_1 = pg.Rect(x1, y1, x2, y2)
rect_2 = pg.Rect(x1 + 50, y1 + 50, x2 + 50, y2 + 50)

is_run = True
turn = False # 0 & 1
players = [rect_1, rect_2]
while is_run:
    pg.display.update()
    for event in pg.event.get():
       press = pg.key.get_pressed()
       if event.type == pg.QUIT:
            is_run = False

    screen.fill(BLACK)  
    pg.draw.rect(screen, RED, rect_1)
    pg.draw.rect(screen, BLUE, rect_2)

    if press[pg.K_RIGHT]:
        players[int(turn)].move_ip(5, 0)
    elif press[pg.K_LEFT]:
        players[int(turn)].move_ip(-5, 0)
    elif press[pg.K_UP]:
        players[int(turn)].move_ip(0, -5)
    elif press[pg.K_DOWN]:
        players[int(turn)].move_ip(0, 5)
    elif press[pg.K_0]:
        turn = False
    elif press[pg.K_1]:
        turn = True
    
    if rect_1.colliderect(rect_2):
        print("Квадраты пересекаются!")
        pg.draw.rect(screen, get_rnd_color(), rect_1)
        pg.draw.rect(screen, get_rnd_color(), rect_2)

    pg.time.Clock().tick(FPS)
"""

# Constant variables (Константы)
BLACK = (0,0,0)
RED = (255, 0, 0) 
BLUE = (0, 0, 255)
FPS = 60

class Screen:
    def __init__(self, width, height):
        x1, y1, x2, y2 = 10, 10, 20, 20
        self.width = width
        self.height = height
        self.clock = pg.time.Clock()
        self.rect_1 = pg.Rect(x1, y1, x2, y2)
        self.rect_2 = pg.Rect(x1 + 50, y1 + 50, x2 + 50, y2 + 50)

    def get_rnd_color(self):
        return randint(0, 255), randint(0, 255), randint(0,255)

    def run(self):
        is_run = True
        turn = False
        screen = pg.display.set_mode((self.width, self.height))
        players = [self.rect_1, self.rect_2]
        while is_run:
            pg.display.update()
            press = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                        is_run = False

            screen.fill(BLACK)  
            pg.draw.rect(screen, RED, self.rect_1)
            pg.draw.rect(screen, BLUE, self.rect_2)

            if press[pg.K_RIGHT]:
                players[int(turn)].move_ip(5, 0)
            elif press[pg.K_LEFT]:
                players[int(turn)].move_ip(-5, 0)
            elif press[pg.K_UP]:
                players[int(turn)].move_ip(0, -5)
            elif press[pg.K_DOWN]:
                players[int(turn)].move_ip(0, 5)
            elif press[pg.K_0]:
                turn = False
            elif press[pg.K_1]:
                turn = True
            
            if self.rect_1.colliderect(self.rect_2):
                print("Квадраты пересекаются!")
                pg.draw.rect(screen, self.get_rnd_color(), self.rect_1)
                pg.draw.rect(screen, self.get_rnd_color(), self.rect_2)

            self.clock.tick(FPS)

game = Screen(400, 400)
game.run()      

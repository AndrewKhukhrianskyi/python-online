import pygame as pg

from random import randint, choice
from time import sleep

from label import Label


BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
TREES_LIST = ['tree.png', 'small_tree.png', 'big_tree.png']
FPS = 60
'''
pg.font.init() # Инициализируем работу со шрифтами
screen = pg.display.set_mode((500, 500))
sys_font = pg.font.Font(None, 20) # Шрифт по умолчанию
font = pg.font.Font('C:/Users/Андрей/Desktop/Код/python-online/CW/hw + cw 21.08/pricedown bl.otf', 50) 

health_icon = pg.image.load('heart.png')
health_icon.set_colorkey(WHITE)
background = pg.image.load('background.jpg')

def draw_trees(background):
    # Задача 1 - Рисовать случайные деревья
    image = pg.image.load(choice(TREES_LIST))
    image.set_colorkey(WHITE)
    background.blit(image, (randint(0, 400), -250)) # Если подымаем объект - указываем отрицательное значение
    

score_value = 0
is_run = True
set_score = True
screen.fill(BLACK)
while is_run:
    score_value += 1
    pg.display.update()
    health_amount = sys_font.render('x3', True, WHITE)
    
    # Добавление значения
    score_text = sys_font.render(str(score_value), True, WHITE)
    

    # Подгрузка изображений
    background.blit(health_icon, (5, 7))
    background.blit(score_text, (300, 10))
    background.blit(health_amount, (30, 10))
    screen.blit(background, (0, 0))
    
    
    for event in pg.event.get():
        press = pg.key.get_pressed()
        if event.type == pg.QUIT:
            is_run = False
    
    if press[pg.K_0]:
        screen.fill(BLACK)
    
    elif press[pg.K_1]:
        sys_font_text = sys_font.render('Это текст с применением системного шрифта', 
                                        True, RED) # render - переоводит Font в Surface
        screen.blit(sys_font_text, (100, 100))

    elif press[pg.K_2]:
        font_text = font.render('RESPECT +', True,  WHITE)
        screen.blit(font_text, (100, 300))
    
    elif press[pg.K_3]:
        font_text = font.render('Game Over', True,  RED)
        screen.blit(font_text, (100, 300))
    
    elif press[pg.K_4]:
        sleep(7)
        draw_trees(background)
'''

# OOP
class Screen:
    def __init__(self, x, y):
        pg.font.init()
        self.x = x
        self.y = y
        self.heart = Label('x3')
        self.background = pg.image.load('background.jpg')
        self.health_icon = pg.image.load('heart.png')


    def draw_trees(self):
        # Задача 1 - Рисовать случайные деревья
        image = pg.image.load(choice(TREES_LIST))
        image.set_colorkey(WHITE)
        self.background.blit(image, (randint(0, 400), -250))

    def run(self):
        screen = pg.display.set_mode((self.x, self.y))
        score_value = 0
        is_run = True
        screen.fill(BLACK)
        
        while is_run:
            score = Label()
            pg.display.update()
            health_amount = self.heart.font.render('x3', True, WHITE)
            self.health_icon.set_colorkey(WHITE)
            result = score.add_score(score_value)
            score_text = score.font.render(result, True, WHITE)
            score_value += 1
            
            

            # Подгрузка изображений
            self.background.blit(self.health_icon, (5, 7))
            self.background.blit(score_text, (300, 10))
            self.background.blit(health_amount, (30, 10))
            screen.blit(self.background, (0, 0))
            
            
            for event in pg.event.get():
                press = pg.key.get_pressed()
                if event.type == pg.QUIT:
                    is_run = False
            
            if press[pg.K_0]:
                screen.fill(BLACK)
                      
            elif press[pg.K_1]:
                sleep(3)
                self.draw_trees()

game = Screen(500, 500)
game.run()


            
            



        




    
    
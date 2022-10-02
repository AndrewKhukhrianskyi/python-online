from cmath import rect
from tkinter import Label
import pygame as pg

from random import randint, choice
from time import sleep

from label import Label
from player import Player
from enemy import Enemy

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
TREES_LIST = ['tree.png', 'small_tree.png', 'big_tree.png']
FPS = 60

class Screen:
    def __init__(self, x, y):
        pg.font.init()
        self.x = x
        self.y = y
        self.heart = Label('x3')
        self.background = pg.image.load('background.jpg')
        self.health_icon = pg.image.load('heart.png')
        self.enemy_list = ['enemy_1.png', 'enemy_2.png', 'enemy_3.png']

    def draw_trees(self):
        # Задача 1 - Рисовать случайные деревья
        image = pg.image.load(choice(TREES_LIST))
        image.set_colorkey(WHITE)
        self.background.blit(image, (randint(0, 400), -250))

    def run(self):
        pg.init()
        pg.time.set_timer(pg.USEREVENT, 500)
        screen = pg.display.set_mode((self.x, self.y))
        score_value = 0
        is_run = True
        enemy_group = pg.sprite.Group()
        player = Player(20, 'player.png')
        screen.fill(BLACK)
        
        while is_run:
            self.health_icon = player.check_player_hp()
            score = Label()
            pg.display.update()
            health_amount = self.heart.font.render('x3', True, WHITE)
            self.health_icon.set_colorkey(WHITE)
            
            result = score.add_score(score_value)
            score_text = score.font.render(result, True, WHITE)
            score_value += 1

            for event in pg.event.get():
                press = pg.key.get_pressed()
                if event.type == pg.QUIT:
                    is_run = False
                elif event.type == pg.USEREVENT:
                   enemy = Enemy(choice(self.enemy_list), enemy_group)
                   if player.rect.colliderect(enemy.rect):
                        player.get_hit()
            
            # Подгрузка изображений
            self.background.blit(self.health_icon, (5, 7))
            self.background.blit(score_text, (300, 10))
            self.background.blit(health_amount, (30, 10))
            self.background.blit(player.image, player.rect)
            screen.blit(self.background, (0, 0))
            
            if press[pg.K_0]:
                screen.fill(BLACK)
                      
            elif press[pg.K_1]:
                sleep(3)
                self.draw_trees()
            
            elif press[pg.K_2]:
                player.get_hit()

            elif press[pg.K_LEFT]:
                player.move_left()

            elif press[pg.K_RIGHT]:
                player.move_right()
            
            else:
                player.default_pos()
            
            
            if player.hp <= 0:
                game_over = pg.image.load('game_over.png')
                screen.blit(game_over, game_over.get_rect())
            player.update()
            enemy_group.update() # обновляет состояние группы объектов (.update())
            enemy_group.draw(self.background) # Отрисовываем группу объектов на поверхности (.draw())

game = Screen(500, 500)
game.run()
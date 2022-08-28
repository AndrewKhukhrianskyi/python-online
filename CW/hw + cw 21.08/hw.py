import pygame as pg


BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
pg.font.init() # Инициализируем работу со шрифтами
screen = pg.display.set_mode((500, 500))
sys_font = pg.font.Font(None, 20) # Шрифт по умолчанию
font = pg.font.Font('C:/Users/Андрей/Desktop/Код/python-online/CW/hw + cw 21.08/pricedown bl.otf', 50) # Example: 'C:/filename_1/filename_2/.../filename_N/font.hf
                      
is_run = True
screen.fill(BLACK)
while is_run:
    pg.display.update()
    health_amount = sys_font.render('x3', True, WHITE)
    screen.blit(health_amount, (30, 10))
    score_text = sys_font.render('000000', True, WHITE)
    screen.blit(score_text, (450, 10))
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


# OOP
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

class Screen:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pg.font.init() # Инициализируем работу со шрифтами
        self.sys_font = pg.font.Font(None, 20)
        self.font = pg.font.Font('C:/Users/Андрей/Desktop/Код/python-online/CW/hw + cw 21.08/pricedown bl.otf', 50)

    def run(self):
        screen = pg.display.set_mode((self.x, self.y))
        is_run = True

        screen.fill(BLACK)
        while is_run:
            pg.display.update()
            health_amount = self.sys_font.render('x3', True, WHITE)
            screen.blit(health_amount, (30, 10))
            score_text = self.sys_font.render('000000', True, WHITE)
            screen.blit(score_text, (450, 10))
            for event in pg.event.get():
                press = pg.key.get_pressed()
                if event.type == pg.QUIT:
                    is_run = False
            
            if press[pg.K_0]:
                screen.fill(BLACK)
            
            elif press[pg.K_1]:
                sys_font_text =self.sys_font.render('Это текст с применением системного шрифта', 
                                                True, RED) # render - переоводит Font в Surface
                screen.blit(sys_font_text, (100, 100))

            elif press[pg.K_2]:
                font_text = self.font.render('RESPECT +', True,  WHITE)
                screen.blit(font_text, (100, 300))
            
            elif press[pg.K_3]:
                font_text = self.font.render('Game Over', True,  RED)
                screen.blit(font_text, (100, 300))


game = Screen(500, 500)
game.run()
    
        


    
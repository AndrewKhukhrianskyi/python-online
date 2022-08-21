import pygame as pg

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen = pg.display.set_mode((500, 500))
sys_font = pg.font.Font(None, 14) # Шрифт по умолчанию
font = pg.font.Font('C:\Windows\Fonts\Pricedown', 14) # Example: 'C:/filename_1/filename_2/.../filename_N/font.hf
                       
is_run = True

while is_run:
    pg.display.update()
    screen.fill(BLACK)
    for event in pg.event.get():
        press = pg.key.get_pressed()
        if event.type == pg.QUIT:
            is_run = False
    
    if press[pg.K_0]:
        screen.fill(BLACK)
    
    elif press[pg.K_1]:
        sys_font_text = sys_font.render(text = 'Это текст с применением системного шрифта',
                                        color = RED) # render - переоводит Font в Surface
        screen.blit(sys_font_text, (100, 100))
    elif press[pg.K_2]:
        font_text = font.render(text = 'Respect +',
                                color = WHITE)
        screen.blit(font_text, (300, 300))
        


    
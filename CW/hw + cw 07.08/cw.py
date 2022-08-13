from random import randint
import pygame as pg

def create_surface(sub_screen):
    object = pg.Surface(size = (25, 25))
    object.fill((randint(0,255),(randint(0,255)),(randint(0,255))))
    
    return object

WHITE = (255,255,255)
FPS = 60

width, height = 300, 300
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
is_run = True

sub_screen = pg.Surface(size = (100, 100))
sub_screen.fill(WHITE)

pg.display.update()
while is_run:
    press = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_run = False

    if press[pg.K_1]:
        object = create_surface(sub_screen)
        sub_screen.blit(object,
                    (randint(0, 150),
                     randint(0, 150)))
        screen.blit(source = sub_screen,
            dest = (width // 2, height // 2))
    
    clock.tick(FPS)
    pg.display.update()
    

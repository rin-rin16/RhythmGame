import pygame as pg
from source_code.Engine import mouse_mode as M_Eng
import os

black = (0, 0, 0)
pink = (255, 150, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 6)
white = (255, 255, 255)
blue = (0, 0, 255)
orange = (255, 180, 0)
dark_grey = (50, 50, 50)
light_grey = (90, 90, 90)

clock = pg.time.Clock()

colors = [red, yellow, green]



def countdown(number):
    if number == 4:
        clock.tick(1)
        M_Eng.screen.fill((0, 0, 0))
        myfont = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 100)
        text = myfont.render('Get Ready', 1, pink)
        M_Eng.screen.blit(text, (450, 300))
        pg.display.update()
        clock.tick(1)
    elif number == 0:
        M_Eng.screen.fill((0, 0, 0))
        myfont = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 100)
        text = myfont.render('GO!', 1, (255, 255, 255))
        M_Eng.screen.blit(text, (550, 300))
        pg.display.update()
        clock.tick(1)
    else:
        M_Eng.screen.fill((0, 0, 0))
        myfont = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 100)
        text = myfont.render(f'{number}', 1, colors[number-1])
        M_Eng.screen.blit(text, (600, 300))
        pg.display.update()
        clock.tick(1)

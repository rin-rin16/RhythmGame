import pygame as pg
from source_code.Engine import Mouse_Mode as M_Eng

clock = pg.time.Clock()



def countdown(number):
    if number == 4:
        clock.tick(1)
        M_Eng.screen.fill((0, 0, 0))
        myfont = pg.font.SysFont("monospace", 30)
        text = myfont.render('Get Ready', 1, (255, 255, 255))
        M_Eng.screen.blit(text, (500, 300))
        pg.display.update()
        clock.tick(1)
    elif number == 0:
        M_Eng.screen.fill((0, 0, 0))
        myfont = pg.font.SysFont("monospace", 30)
        text = myfont.render('GO!', 1, (255, 255, 255))
        M_Eng.screen.blit(text, (500, 300))
        pg.display.update()
        clock.tick(1)
    else:
        M_Eng.screen.fill((0, 0, 0))
        myfont = pg.font.SysFont("monospace", 30)
        text = myfont.render(f'{number}', 1, (255, 255, 255))
        M_Eng.screen.blit(text, (500, 300))
        pg.display.update()
        clock.tick(1)

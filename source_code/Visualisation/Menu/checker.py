import pygame as pg
from source_code.Visualisation.Background import Background as bg

import Vis_Choose_a_song_Menu as csm
import Vis_Start_Menu as sm
import Vis_Pause_Menu as pm

pg.init()

screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()

finished = False

cs_menu = csm.VisualisationInChooseSongMenu(screen)

start_menu = sm.DrawAMenuButton(screen)

pause_menu = pm.DrawAMenuButton(screen)

while not finished:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            screen.fill((0, 0, 0))
            pause_menu.all_menu_drawer_pressed()
            pg.display.update()
            clock.tick(0.5)
            screen.fill((0, 0, 0))
            pause_menu.all_menu_drawer_unpressed()
            pg.display.update()
        else:
            screen.fill((0, 0, 0))
            pause_menu.all_menu_drawer_unpressed()
            pg.display.update()



    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()

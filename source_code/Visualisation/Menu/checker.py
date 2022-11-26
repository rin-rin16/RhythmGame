import pygame as pg
import pygame.key

import Vis_Choose_a_song_Menu as csm
import Vis_Start_Menu as sm
import Vis_Pause_Meny as pm

pg.init()

screen = pg.display.set_mode((1280, 720))

finished = False

cs_menu = csm.VisualisationInChooseSongMenu(screen)

start_menu = sm.DrawAMenuButton(screen)

pause_menu = pm.DrawAMenuButton(screen)

while not finished:
    for event in pg.event.get():
        if pg.key.get_pressed()[pg.K_SPACE]:
            pause_menu.all_menu_drawer_pressed()
            pg.display.update()
        else:
            pause_menu.all_menu_drawer_unpressed()
            pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

print(pg.font.get_fonts())
pg.quit()

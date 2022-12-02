import pygame as pg
from source_code.Visualisation.Background import Background as bg

from source_code.Visualisation.Menu import Vis_Choose_a_song_Menu as csm
from source_code.Visualisation.Menu import Vis_Pause_Menu as pm
from source_code.Visualisation.Menu import Vis_Start_Menu as sm

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
            pause_menu.all_menu_drawer_unpressed()
            pg.display.update()
        else:
            pause_menu.all_menu_drawer_unpressed()
            pg.display.update()



    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()

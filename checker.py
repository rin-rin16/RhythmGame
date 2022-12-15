import pygame as pg
from source_code.Visualisation.Background import Background as bg

from source_code.Visualisation.Menu import Vis_Choose_a_song_Menu as csm
from source_code.Visualisation.Menu import Vis_Pause_Menu as pm
from source_code.Visualisation.Menu import Vis_Start_Menu as sm
from source_code.Visualisation.Game import Vis_Mouse_Mode as vmm
from source_code.Visualisation.Menu import Vis_Choose_mode_menu as vcm

pg.init()

screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()

finished = False

cs_menu = csm.VisualisationInChooseSongMenu(screen)

start_menu = sm.DrawAMenuButton(screen)

pause_menu = pm.DrawAMenuButton(screen)

chm_menu = vcm.DrawAMenuButton(screen)

while not finished:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            screen.fill((0, 0, 0))
            chm_menu.all_menu_drawer_pressed('none')
            pg.display.update()
        else:
            screen.fill((0, 0, 0))
            chm_menu.all_menu_drawer_pressed('none')
            pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True


pg.quit()

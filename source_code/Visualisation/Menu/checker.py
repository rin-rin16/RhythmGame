import pygame as pg
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
    start_menu.all_menu_drawer()
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

print(pg.font.get_fonts())
pg.quit()

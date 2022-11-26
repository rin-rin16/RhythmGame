import pygame as pg
import Vis_Choose_a_song_Menu as csm
import Vis_Start_Menu as sm

pg.init()

screen = pg.display.set_mode((1280, 720))

finished = False

csmenu = csm.VisualisationInChooseSongMenu(screen)

startmenu = sm.DrawAMenuButton(screen)

while not finished:
    csmenu.all_drawer()
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

print(pg.font.get_fonts())
pg.quit()

import pygame as pg
from source_code.Visualisation.Background import background as bg

from source_code.Visualisation.Menu import vis_choose_a_song_menu as csm
from source_code.Visualisation.Menu import vis_pause_menu as pm
from source_code.Visualisation.Menu import vis_start_menu as sm
from source_code.Visualisation.Game import vis_mouse_mode as vmm
from source_code.Visualisation.Menu import vis_choose_mode_menu as vcm
from source_code.Visualisation.Menu import vis_end_menu as vem

pg.init()

screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()

finished = False

cs_menu = csm.VisualisationInChooseSongMenu(screen)

start_menu = sm.DrawAMenuButton(screen)

pause_menu = pm.DrawAMenuButton(screen)

chm_menu = vcm.DrawAMenuButton(screen)

end_menu = vem.DrawAMenuButton(screen, 220)

while not finished:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            screen.fill((0, 0, 0))
            end_menu.all_menu_drawer_pressed('quit')
            pg.display.update()
        else:
            screen.fill((0, 0, 0))
            end_menu.all_menu_drawer_pressed('quit')
            pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            finished = True


pg.quit()

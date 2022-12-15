import pygame as pg
import Vis_Keyboard_Mode as vkm
import Vis_score as VS
import source_code.Engine.score as score


pg.init()

screen = pg.display.set_mode((1280, 720))

finished = False

target = vkm.DrawableRightTarget(screen, 400, 400, 10, 'normal')
score_draw = VS.DrawCounter(screen)

while not finished:

    screen.fill((0, 0, 0))
    target.draw_right_arrow()
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True


pg.quit()

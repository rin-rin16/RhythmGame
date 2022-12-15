import pygame as pg
import Vis_Keyboard_Mode as vkm
import Vis_score as VS
import source_code.Engine.score as score


pg.init()

screen = pg.display.set_mode((1280, 720))

finished = False

arrow = vkm.DrawableArrowRight(screen, 400, 400, 10, 'normal')
score_draw = VS.DrawCounter(screen)

while not finished:

    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            score.up(score.counter)
            screen.fill((0,0,0))
            score_draw.draw_counter(score.counter.getter())
    pg.display.update()


pg.quit()

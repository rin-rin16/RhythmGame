import pygame as pg
import Vis_Keyboard_Mode as vkm

pg.init()

screen = pg.display.set_mode((1280, 720))

finished = False

arrow = vkm.DrawableArrowLeft(screen, 400, 400, 10, 'normal')

while not finished:
    arrow.draw_left_arrow()
    pg.display.update()



    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True


pg.quit()

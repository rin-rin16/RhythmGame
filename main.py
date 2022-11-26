import pygame as pg
import time as time
import pandas as pd
from source_code.Sound_Rhytm import Sound_Rhytm as SR
from source_code.Engine import Mouse_Mode as M_Eng

#width, height = 1280, 720       # Screen's width and height        # Took this into engine file
#background_color = (0, 0, 0)

#pg.display.init()

#screen = pg.display.set_mode((width, height))
#screen.fill(background_color)
#pg.display.flip()

SR.start_time.setter(time.time())



running = True

[balls, draw_balls] = M_Eng.ball_initializer()

while running:
    pg.display.update()
    SR.TimerBull.timer()
    M_Eng.Drawer(draw_balls)
    print(draw_balls.getter()[0].coord_getter())
    print(balls.getter()[0].coord_getter())
    pg.draw.circle(M_Eng.screen, "green", (500, 500), 10)
    for event in pg.event.get():
        M_Eng.Event_Holder(event, balls, draw_balls, SR.TimerBull)
        if event.type == pg.QUIT:
            running = False
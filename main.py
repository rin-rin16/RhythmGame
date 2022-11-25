import pygame as pg
import time as time
import pandas as pd
from source_code.Sound_Rhytm import Sound_Rhytm as SR

width, height = 1280, 720       # Screen's width and height
background_color = (0, 0, 0)

pg.display.init()

screen = pg.display.set_mode((width, height))
screen.fill(background_color)
pg.display.flip()

SR.start_time.setter(time.time())

running = True
while running:
    pg.display.update()
    SR.TimerBull.timer()
    if SR.TimerBull.getter():
        screen.fill((255, 255, 255))
    if not SR.TimerBull.getter():
        screen.fill(background_color)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
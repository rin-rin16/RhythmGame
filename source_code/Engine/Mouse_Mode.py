import pygame as pg
import numpy as np
from source_code.Visualisation.Game import Vis_Mouse_Mode as Mouse
from source_code.Sound_Rhytm import Sound_Rhytm as SR

class Ball:
    """Class, responding to calculations with balls"""
    def __init__(self):     # Creates initial balls coordinates
        self._r = 10
        self._x = np.random.randint(10, 1270)
        self._y = np.random.randint(10, 710)

    def pos_setter(self, pos):      # Sets ball's position in the balls list
        self._pos = pos

    def pos_getter(self):
        return self._pos

    def click_check(self, event):       # Checks, if click hits the only clickable ball, which is the first one in the balls list
        if (self.x - event.pos[0]) ** 2 + (self.y - event.pos[1]) ** 2 <= self.r ** 2:
            return True
        else: return False

    def bit_check(self, TimerBull):     # Checks, if click hits the bit
        if TimerBull.timer():
            return True
        else:
            return False



for event in pg.event.get():
    if event.type == pg.MOUSEBUTTONDOWN:
        ba
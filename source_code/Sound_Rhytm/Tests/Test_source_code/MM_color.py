import time

import pygame as pg
import numpy as np
from source_code.Visualisation.Game import Vis_Mouse_Mode as Ms_Vis
from source_code.Sound_Rhytm import Sound_Rhytm as SR

class Ball:
    """Class, responding to calculations with balls"""
    def __init__(self, color, surface):     # Creates initial balls coordinates
        self.surface = surface
        self._r = 500
        self._x = 640
        self._y = 330
        self._pos = 2
        self.color = color

    def draw_a_ball(self):
        pg.draw.circle(self.surface, self.color, (self._x, self._y), self._r)
        pg.draw.circle(self.surface, "white", (self._x, self._y), self._r, width=4)

    def color_getter(self):
        return self.color

class ListVariables():
    """Class of list variables, used in this program"""
    def __init__(self):
        self.list = []

    def setter(self, arg):
        self.list = arg

    def getter(self):
        return self.list


width, height = 1280, 720       # Screen's width and height
background_color = (0, 0, 0)

pg.display.init()

screen = pg.display.set_mode((width, height))
screen.fill(background_color)
pg.display.flip()

balls = ListVariables()         # Creating lists of balls
draw_balls = ListVariables()

def ball_initializer():
    """
    Creates initial balls
    :return: ListVariables of balls and drawable balls
    """

    ball_1 = Ball("red", screen)     # Creating initial balls
    ball_3 = Ball("green", screen)

    balls.setter([ball_1, ball_3])

    return balls

def Event_Holder(event, balls, TimerBull):
    """
    Checks if the click hits the beat and the ball, and if so, gives user score
    :param event: event
    :param balls: list of balls
    :param draw_balls: list of drawable balls
    :param TimerBull: timer, which checks for the beat
    :return: nothing
    """
    #if event.type == pg.MOUSEBUTTONDOWN:            # Commented stuff is here for testing reasons
        #if balls.getter()[0].bit_check(TimerBull) and balls.getter()[0].click_check(event):
        #if balls.getter()[0].bit_check(TimerBull):
    if TimerBull.getter():
        balls.setter([balls.getter()[1], balls.getter()[0]])
        time.sleep(0.3)




def Drawer(balls):
    """
    Draws balls from the list
    :param draw_balls: list of balls to draw
    :return: nothing
    """
    balls.getter()[0].draw_a_ball()
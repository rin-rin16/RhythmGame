import pygame as pg
import numpy as np
from source_code.Visualisation.Game import vis_mouse_mode as Ms_Vis


class Ball:
    """Class, responding to calculations with balls"""
    def __init__(self):     # Creates initial balls coordinates
        self._r = 30
        self._x = np.random.randint(30, 1250)
        self._y = np.random.randint(30, 690)
        self._pos = 2

    def pos_setter(self, pos):      # Sets ball's position in the balls list
        self._pos = pos

    def pos_getter(self):
        return self._pos

    def click_check(self, event):       # Checks, if click hits the only clickable ball, which is the first one in the balls list
        if (self._x - event.pos[0]) ** 2 + (self._y - event.pos[1]) ** 2 <= self._r ** 2:
            return True
        else: return False

    def bit_check(self, TimerBull):     # Checks, if click hits the bit
        if TimerBull.getter():
            return True
        else:
            return False

    def coord_getter(self):
        return [self._x, self._y]


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

    ball_1 = Ball()     # Creating initial balls
    ball_1.pos_setter(0)
    ball_2 = Ball()
    ball_2.pos_setter(1)
    ball_3 = Ball()
    ball_3.pos_setter(2)

    balls.setter([ball_1, ball_2, ball_3])

    draw_ball_1 = Ms_Vis.DrawableBall(ball_1.coord_getter()[0], ball_1.coord_getter()[1], screen, ball_1.pos_getter())
    draw_ball_2 = Ms_Vis.DrawableBall(ball_2.coord_getter()[0], ball_2.coord_getter()[1], screen, ball_2.pos_getter())
    draw_ball_3 = Ms_Vis.DrawableBall(ball_3.coord_getter()[0], ball_3.coord_getter()[1], screen, ball_3.pos_getter())

    draw_balls.setter([draw_ball_1, draw_ball_2, draw_ball_3])

    return balls, draw_balls

def Event_Holder(event, balls, draw_balls, TimerBull):
    """
    Checks if the click hits the beat and the ball, and if so, gives user score
    :param event: event
    :param balls: list of balls
    :param draw_balls: list of drawable balls
    :param TimerBull: timer, which checks for the beat
    :return: nothing
    """
    #if event.type == pg.MOUSEBUTTONDOWN or event.type == pg.KEYDOWN:            # Commented stuff is here for testing reasons
        #if balls.getter()[0].bit_check(TimerBull) and balls.getter()[0].click_check(event):
    if balls.getter()[0].bit_check(TimerBull):
    #if TimerBull.getter():
        balls.setter([balls.getter()[1], balls.getter()[2], Ball()])

        draw_ball_1 = draw_balls.getter()[1]
        draw_ball_1.color_setter("green")
        draw_ball_2 = draw_balls.getter()[2]
        draw_ball_2.color_setter("yellow")
        draw_ball_3 = Ms_Vis.DrawableBall(balls.getter()[2].coord_getter()[0], balls.getter()[2].coord_getter()[1],
                                              screen, balls.getter()[2].pos_getter()
                                             )
        draw_balls.setter([draw_ball_1, draw_ball_2, draw_ball_3])
            #time.sleep(0.3)


def Drawer(draw_balls):
    """
    Draws balls from the list
    :param draw_balls: list of balls to draw
    :return: nothing
    """
    for ball in draw_balls.getter():
        ball.draw_a_ball()

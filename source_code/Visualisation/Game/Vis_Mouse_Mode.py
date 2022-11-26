import pygame as pg
import numpy as np

red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
orange = (255, 180, 0)


class DrawableBall:
    '''
    draws a ball in direct place
    '''
    def __init__(self, x, y, surface, pos):
        self.surface = surface
        self.x = x
        self.y = y
        self.r = 10
        self.pos = pos
        if self.pos == 0:
            self.color = green
        if self.pos == 1:
            self.color = yellow
        if self.pos == 2:
            self.color = red

    def color_setter(self, color):
        """

        :param color -- color of the ball
        :return: sets color according to ball's position in list of balls
        """
        self.color = color

    def draw_a_ball(self):
        '''
        :return: draws a ball if ball is alive
        '''

        pg.draw.circle(self.surface, self.color, (self.x, self.y), self.r)
        pg.draw.circle(self.surface, white, (self.x, self.y), self.r, width=2)

    def color_getter(self):
        return self.color

pg.font.init()

class DisplayText:
    '''
    requires x, y and screen
    '''

    COOL_WORDS = [('Wow!', 1, yellow, black), ('Shock!', 1, blue, black), ('Stunning!', 1, red, black),
                  ('Insane', 1, white, black), ('OMG', 1, orange, black)]
    words_number = len(COOL_WORDS)
    font = pg.font.SysFont('comicsansms', 32)

    def __init__(self, x, y, surface):
        self.x = x
        self.y = y
        self.screen = surface
        self.lives = 100


    def writer_of_cool_word(self):
        '''
        writes a cool word in dot (self.x, self.y)
        cool word is randomly choosen

        '''
        if self.lives >= 0:
            self.screen.blit(self.font.render(self.COOL_WORDS[np.random.randint(self.words_number)]), (self.x, self.y))

    def live_down(self):
        self.lives -= 1


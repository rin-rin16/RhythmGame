import pygame as pg

red = [255, 0, 0]
green = [0, 255, 0]
yellow = [255, 255, 0]
class Drawable_ball:
    '''
    draws a ball in direct place
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 10
        self.color = green
        self.is_alive = True
    def click(self):
        '''

        :return: changes ball's color, or kills the ball
        '''
        if self.color == green:
            self.color = yellow
        if self.color == yellow:
            self.color = red
        if self.color == red:
            self.is_alive = False
    def draw_a_ball(self):
        '''

        :return: draws a ball if ball is alive
        '''
        if self.is_alive == True:
            pg.draw.ball(self.r, (self.x, self.y), self.color)


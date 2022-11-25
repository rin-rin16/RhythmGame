import pygame as pg

black = (0, 0, 0)
pink = (255, 150, 255)

class DrawAMenuButton:
    '''
    draws a beautiful button in some place
    '''

    def __init__(self, surface):
        self.surface = surface
        self.x = 580
        self.y = 300

    def draw_a_start_button(self):
        font = pg.font.SysFont('comicsansms', 32)
        start = font.render('Start', 1, black, pink)
        self.surface.blit(start, (self.x, self.y))


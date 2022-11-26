import pygame as pg

black = (0, 0, 0)
pink = (255, 150, 255)
yellow = (255, 193, 6)

class DrawAMenuButton:
    '''
    draws a beautiful button in some place
    '''

    def __init__(self, surface):
        self.surface = surface


    def draw_start_button(self):
        font = pg.font.SysFont('comicsansms', 32)
        start = font.render('Start', 1, black, pink)
        self.surface.blit(start, (580, 300))

    def draw_Menu_word(self):
        font = pg.font.SysFont('comicsansms', 32)
        menu = font.render('Menu', 1, yellow, black)
        self.surface.blit(menu, (580, 100))

    def all_menu_drawer(self):
        self.draw_Menu_word()
        self.draw_start_button()

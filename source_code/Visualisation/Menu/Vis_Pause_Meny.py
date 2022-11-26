import pygame as pg

black = (0, 0, 0)
pink = (255, 150, 255)
yellow = (255, 220, 6)


class DrawAMenuButton:
    '''
    draws a beautiful button in some place
    '''

    def __init__(self, surface):
        self.surface = surface

    def draw_continue_button(self):
        font = pg.font.SysFont('sunsetclubfreetrial', 160)
        start = font.render('Continue', 1, pink)
        self.surface.blit(start, (410, 300))

    def draw_pause_word(self):
        font = pg.font.SysFont('sunsetclubfreetrial', 50)
        menu = font.render('Pause', 1, yellow, black)
        self.surface.blit(menu, (580, 100))

    def all_menu_drawer(self):
        self.draw_pause_word()
        self.draw_continue_button()
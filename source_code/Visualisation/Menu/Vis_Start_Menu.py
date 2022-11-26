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

    def draw_start_button(self):
        font = pg.font.Font('Sunset Club Free Trial.ttf', 160)
        start = font.render('Start', 1, pink)
        self.surface.blit(start, (480, 300))

    def draw_menu_word(self):
        font = pg.font.Font('Sunset Club Free Trial.ttf', 50)
        menu = font.render('Menu', 1, yellow, black)
        self.surface.blit(menu, (580, 100))

    def all_menu_drawer(self):
        self.draw_menu_word()
        self.draw_start_button()

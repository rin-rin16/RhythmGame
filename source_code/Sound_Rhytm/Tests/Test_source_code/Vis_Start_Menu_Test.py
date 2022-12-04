import os
import pygame as pg

black = (0, 0, 0)
pink = (255, 150, 255)
yellow = (255, 220, 6)
dark_grey = (50, 50, 50)
light_grey = (90, 90, 90)


class DrawAMenuButton:
    '''
    draws a beautiful button in some place

    Varning!!! use only all_menu_drawer_unpressed or all_menu_drawer_pressed functions

    they draw all menu
    '''

    def __init__(self, surface):
        self.surface = surface

    def draw_start_button_unpressed(self):
        pg.draw.rect(self.surface, color=dark_grey, rect=(470, 190, 320, 185))
        font = pg.font.Font(os.path.join("C:\\Users\\danik\\PycharmProjects\\RhythmGame", "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 160)
        start = font.render('Start', 1, pink, light_grey)
        self.surface.blit(start, (480, 200))

    def draw_start_button_pressed(self):
        font = pg.font.Font(os.path.join("C:\\Users\\danik\\PycharmProjects\\RhythmGame", "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 160)
        start = font.render('Start', 1, pink, dark_grey)
        self.surface.blit(start, (470, 190))

    def draw_quit_button_unpressed(self):
        pg.draw.rect(self.surface, color=dark_grey, rect=(545, 440, 200, 138))
        font = pg.font.Font(os.path.join("C:\\Users\\danik\\PycharmProjects\\RhythmGame", "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 120)
        start = font.render('Quit', 1, pink, light_grey)
        self.surface.blit(start, (555, 450))

    def draw_quit_button_pressed(self):
        font = pg.font.Font(os.path.join("C:\\Users\\danik\\PycharmProjects\\RhythmGame", "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 120)
        start = font.render('Quit', 1, pink, dark_grey)
        self.surface.blit(start, (545, 440))

    def draw_menu_word(self):
        font = pg.font.Font(os.path.join("C:\\Users\\danik\\PycharmProjects\\RhythmGame", "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 60)
        menu = font.render('Menu', 1, yellow, black)
        self.surface.blit(menu, (580, 100))

    def all_menu_drawer_pressed(self, button: str):
        """

        :param button: which button is pressed ['none', 'start', 'quit']
        :return: draws given button pressed, other unpressed
        """
        self.draw_menu_word()
        if button == 'none':
            self.draw_quit_button_unpressed()
            self.draw_start_button_unpressed()
        if button == 'start':
            self.draw_quit_button_unpressed()
            self.draw_start_button_pressed()
        if button == 'quit':
            self.draw_quit_button_pressed()
            self.draw_start_button_unpressed()
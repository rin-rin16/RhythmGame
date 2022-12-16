import pygame as pg
import os

black = (0, 0, 0)
pink = (255, 150, 255)
yellow = (255, 220, 6)
dark_grey = (50, 50, 50)
light_grey = (90, 90, 90)
orange = (255, 150, 0)
purple = (121, 50, 169)


class DrawAMenuButton:
    """
    draws a beautiful button in some place

    Varning!!! use only all_menu_drawer_unpressed or all_menu_drawer_pressed functions

    they draw all menu
    """

    def __init__(self, surface, score):
        self.surface = surface
        self.score = score

    def draw_to_menu_button_unpressed(self):
        pg.draw.rect(self.surface, color=dark_grey, rect=(380, 230, 550, 180))
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 160)
        continue_word = font.render('Continue', True, pink, light_grey)
        self.surface.blit(continue_word, (390, 240))

    def draw_to_menu_button_pressed(self):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 160)
        continue_word = font.render('Continue', True, pink, dark_grey)
        self.surface.blit(continue_word, (380, 230))

    def draw_quuit_button_unpressed(self):
        pg.draw.rect(self.surface, color=dark_grey, rect=(520, 470, 265, 138))
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 120)
        start = font.render('Menu', True, pink, light_grey)
        self.surface.blit(start, (530, 480))

    def draw_quit_button_pressed(self):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 120)
        start = font.render('Menu', True, pink, dark_grey)
        self.surface.blit(start, (520, 470))

    def draw_score(self):
        pass

    def draw_congratulations_word(self):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 60)
        menu = font.render('Pause', True, yellow, black)
        self.surface.blit(menu, (580, 100))

    def all_menu_drawer_pressed(self, button: str):
        """

        :param button: which button is pressed ['none', 'continue', 'menu']
        :return: draws given button pressed, other unpressed
        """
        self.draw_congratulations_word()
        self.draw_score()
        if button == 'none':
            self.draw_menu_button_unpressed()
            self.draw_continue_button_unpressed()
        if button == 'to menu':
            self.draw_menu_button_unpressed()
            self.draw_continue_button_pressed()
        if button == 'quit':
            self.draw_menu_button_pressed()
            self.draw_continue_button_unpressed()

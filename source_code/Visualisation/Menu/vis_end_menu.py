import pygame as pg
import os

black = (0, 0, 0)
pink = (255, 150, 255)
yellow = (255, 220, 6)
dark_grey = (50, 50, 50)
light_grey = (90, 90, 90)
orange = (255, 165, 0)
purple = (121, 50, 169)
white = (255, 255, 255)


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
        pg.draw.rect(self.surface, color=white, rect=(370, 380, 550, 130), width=7)
        pg.draw.rect(self.surface, color=black, rect=(380-5, 390-5, 550, 130))
        pg.draw.rect(self.surface, color=white, rect=(380, 390, 550, 130), width=7)
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu",
                                         'Sunset Club Free Trial.ttf'), 120)
        to_menu = font.render('Go to menu', True, purple)
        self.surface.blit(to_menu, (390, 400))

    def draw_to_menu_button_pressed(self):
        pg.draw.rect(self.surface, color=white, rect=(370, 380, 550, 130), width=7)
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu",
                                         'Sunset Club Free Trial.ttf'), 120)
        to_menu = font.render('Go to menu', True, purple)
        self.surface.blit(to_menu, (380, 390))

    def draw_quit_button_unpressed(self):
        pg.draw.rect(self.surface, color=white, rect=(370, 550, 550, 130), width=7)
        pg.draw.rect(self.surface, color=black, rect=(380 - 5, 560 - 5, 550, 130))
        pg.draw.rect(self.surface, color=white, rect=(380, 560, 550, 130), width=7)
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu",
                                         'Sunset Club Free Trial.ttf'), 120)
        exit_game = font.render('Quit', True, purple)
        self.surface.blit(exit_game, (530, 570))

    def draw_quit_button_pressed(self):
        pg.draw.rect(self.surface, color=white, rect=(370, 550, 550, 130), width=7)
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu",
                                         'Sunset Club Free Trial.ttf'), 120)
        to_menu = font.render('Quit', True, purple)
        self.surface.blit(to_menu, (520, 570))

    def draw_score(self):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu",
                                         'Sunset Club Free Trial.ttf'), 100)
        font_double_dot = pg.font.SysFont('marion', 80)
        font_number = pg.font.SysFont('geneva', 100)
        score = font.render('Your score', True, orange)
        double_dot = font_double_dot.render(':', True, orange)
        number = font_number.render(f'{self.score}', True, orange)
        self.surface.blit(score, (50, 260))
        self.surface.blit(double_dot, (445, 275))
        self.surface.blit(number, (500, 240))

    def draw_congratulations_word(self):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu",
                                         'Sunset Club Free Trial.ttf'), 180)
        menu = font.render('Congratulations!', True, white, black)
        self.surface.blit(menu, (50, 50))

    def all_menu_drawer_pressed(self, button: str):
        """

        :param button: which button is pressed ['none', 'continue', 'menu']
        :return: draws given button pressed, other unpressed
        """
        self.draw_congratulations_word()
        self.draw_score()
        if button == 'none':
            self.draw_quit_button_unpressed()
            self.draw_to_menu_button_unpressed()
        if button == 'to_menu':
            self.draw_quit_button_unpressed()
            self.draw_to_menu_button_pressed()
        if button == 'quit':
            self.draw_quit_button_pressed()
            self.draw_to_menu_button_unpressed()

import os
import pygame as pg

black = (0, 0, 0)
pink = (255, 150, 255)
yellow = (255, 220, 6)
dark_grey = (50, 50, 50)
light_grey = (90, 90, 90)
cyan = (0,255,255)

class DrawAMenuButton:
    """
    draws a beautiful button in some place

    Varning!!! use only all_menu_drawer_unpressed or all_menu_drawer_pressed functions

    they draw all menu
    """

    def __init__(self, surface):
        self.surface = surface

    def draw_mouse_button_unpressed(self):
        pg.draw.rect(self.surface, color=dark_grey, rect=(485, 210, 284, 135))
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 120)
        start = font.render('Mouse', True, pink, light_grey)
        self.surface.blit(start, (495, 220))

    def draw_mouse_button_pressed(self):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 120)
        start = font.render('Mouse', True, pink, dark_grey)
        self.surface.blit(start, (485, 210))

    def draw_keyboard_button_unpressed(self):
        pg.draw.rect(self.surface, color=dark_grey, rect=(420-10, 440, 440, 134))
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 120)
        start = font.render('Keyboard', True, pink, light_grey)
        self.surface.blit(start, (420, 450))

    def draw_keyboard_button_pressed(self):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 120)
        start = font.render('Keyboard', True, pink, dark_grey)
        self.surface.blit(start, (400-10, 440))

    def draw_back_button_unpressed(self):
        pg.draw.rect(self.surface, color=dark_grey, rect=(950 - 10, 550-10, 170, 95))
        font = pg.font.Font(
            os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 80)
        start = font.render('Back', True, cyan, light_grey)
        self.surface.blit(start, (950, 550))

    def draw_choose_mode_word(self):
        bad_font = pg.font.SysFont('marion', 50)
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 60)
        choose_mode = font.render('Choose game mode', True, yellow, black)
        double_dot = bad_font.render(':', True, yellow)
        self.surface.blit(choose_mode, (400, 100))
        self.surface.blit(double_dot, (850, 110))

    def all_menu_drawer_pressed(self, button: str):
        """

        :param button: which button is pressed ['none', 'mouse', 'keyboard']
        :return: draws given button pressed, other unpressed
        """
        self.draw_choose_mode_word()
        if button == 'none':
            self.draw_mouse_button_unpressed()
            self.draw_keyboard_button_unpressed()
            self.draw_back_button_unpressed()
        if button == 'mouse':
            self.draw_keyboard_button_unpressed()
            self.draw_mouse_button_pressed()
        if button == 'keyboard':
            self.draw_keyboard_button_pressed()
            self.draw_mouse_button_unpressed()




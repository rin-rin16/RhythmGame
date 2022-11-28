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

    def draw_continue_button_unpressed(self):
        pg.draw.rect(self.surface, color=dark_grey, rect=(400, 290, 550, 180))
        font = pg.font.Font('Sunset Club Free Trial.ttf', 160)
        Continue = font.render('Continue', 1, pink, light_grey)
        self.surface.blit(Continue, (410, 300))

    def draw_continue_button_pressed(self):
        font = pg.font.Font('Sunset Club Free Trial.ttf', 160)
        Continue = font.render('Continue', 1, pink, light_grey)
        self.surface.blit(Continue, (400, 290))

    def draw_pause_word(self):
        font = pg.font.Font('Sunset Club Free Trial.ttf', 50)
        menu = font.render('Pause', 1, yellow, black)
        self.surface.blit(menu, (580, 100))

    def all_menu_drawer_unpressed(self):
        """

        :return: draws menu in state when continue button unpressed
        """
        self.draw_pause_word()
        self.draw_continue_button_unpressed()

    def all_menu_drawer_pressed(self):
        """

        :return: draws menu in state when continue button pressed
        """
        self.draw_pause_word()
        self.draw_continue_button_pressed()

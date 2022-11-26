import pygame as pg

black = (0, 0, 0)
pink = (255, 150, 255)
yellow = (255, 220, 6)
dark_grey = (50, 50, 50)
light_grey = (90, 90, 90)


class DrawAMenuButton:
    '''
    draws a beautiful button in some place
    '''

    def __init__(self, surface):
        self.surface = surface

    def draw_start_button_unpressed(self):
        pg.draw.rect(self.surface, color=dark_grey, rect=(470, 290, 320, 185))
        font = pg.font.Font('Sunset Club Free Trial.ttf', 160)
        start = font.render('Start', 1, pink, light_grey)
        self.surface.blit(start, (480, 300))

    def draw_start_button_pressed(self):
        font = pg.font.Font('Sunset Club Free Trial.ttf', 160)
        start = font.render('Start', 1, pink, dark_grey)
        self.surface.blit(start, (470, 290))

    def draw_menu_word(self):
        font = pg.font.Font('Sunset Club Free Trial.ttf', 50)
        menu = font.render('Menu', 1, yellow, black)
        self.surface.blit(menu, (580, 100))

    def all_menu_drawer_unpressed(self):
        self.draw_menu_word()
        self.draw_start_button_unpressed()

    def all_menu_drawer_pressed(self):
        self.draw_menu_word()
        self.draw_start_button_pressed()

import pygame as pg
import os

black = (0, 0, 0)
pink = (255, 150, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 6)
white = (255, 255, 255)
blue = (0, 0, 255)
orange = (255, 180, 0)
dark_grey = (50, 50, 50)
light_grey = (90, 90, 90)
cyan = (0,255,255)


x = 20

class VisualisationInChooseSongMenu:
    """
    draws beautiful buttons in some place

    Varning! use to draw only function all_menu_drawer!!!!
    """

    def __init__(self, surface):
        self.surface = surface

    def draw_back_button_unpressed(self):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 70)
        easy = font.render('Back', 1, cyan, light_grey)
        pg.draw.rect(self.surface, color=dark_grey, rect=(1100-7, 600-7, 150, 78))
        self.surface.blit(easy, (1100, 600))

    def draw_back_button_pressed(self):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 70)
        easy = font.render('Back', 1, cyan, dark_grey)
        self.surface.blit(easy, (1100-7, 600-7))

    def draw_easy_button(self):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 40)
        easy = font.render('easy', 1, green)
        self.surface.blit(easy, (570, 60))

    def draw_medium_button(self):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 40)
        medium = font.render('medium', 1, yellow)
        self.surface.blit(medium, (535, 260))

    def draw_hard_button(self):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 40)
        hard = font.render('hard', 1, red)
        self.surface.blit(hard, (560, 460))

    def draw_a_song_name_unpressed(self, x, y, name, length_name, height_name):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 40)
        song_name = font.render(name, 1, white, light_grey)
        pg.draw.rect(self.surface, color=dark_grey, rect=(x-7, y-7, length_name, height_name))
        self.surface.blit(song_name, (x, y))

    def draw_a_song_name_pressed(self, x, y, name, length_name, height_name):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 40)
        song_name = font.render(name, 1, white, dark_grey)
        self.surface.blit(song_name, (x-7, y-7))

    def all_menu_drawer_pressed(self, pos):
        """

        :param pos: number which shows position of song in song_tuple or back, if it is button back
        :return: draws a screen with drawn button pos pressed
        """
        song_tuple = [(343, 145, 'Keraunos killer',  235, 48, 0),
                      (638, 145, 'Live another day', 268, 48, 1),
                      (378, 345, 'Delta alpha',      198, 48, 4),
                      (638, 345, 'Phonky town',      202, 48, 2),
                      (540, 540, 'Why not.',         130, 48, 3)]

        '''for i in range(3):
            for song in song_matrix[i]:
                if (i, song[5]) != pos:
                    self.draw_a_song_name_unpressed(song[0], song[1], song[2], song[3], song[4])'''
        for i in range(5):
            if pos != song_tuple[i][5]:
               self.draw_a_song_name_unpressed(song_tuple[i][0], song_tuple[i][1], song_tuple[i][2], song_tuple[i][3], song_tuple[i][4])
            else:
                self.draw_a_song_name_pressed(song_tuple[i][0], song_tuple[i][1], song_tuple[i][2], song_tuple[i][3], song_tuple[i][4])

        if pos == 'back':
            self.draw_back_button_pressed()
        else:
            self.draw_back_button_unpressed()
        self.draw_easy_button()
        self.draw_medium_button()
        self.draw_hard_button()


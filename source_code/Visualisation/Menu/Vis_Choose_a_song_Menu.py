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

x = 20

class VisualisationInChooseSongMenu:
    """
    draws beautiful buttons in some place

    Varning! use to draw only function all_menu_drawer!!!!
    """

    def __init__(self, surface):
        self.surface = surface

    def draw_easy_button(self):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 120)
        easy = font.render('easy', 1, green)
        self.surface.blit(easy, (580, 100))

    def draw_medium_button(self):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 120)
        medium = font.render('medium', 1, yellow)
        self.surface.blit(medium, (580-20, 300))

    def draw_hard_button(self):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 120)
        hard = font.render('hard', 1, red)
        self.surface.blit(hard, (580, 500))

    def draw_a_song_name_unpressed(self, x, y, name, length_name, height_name):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 120)
        song_name = font.render(name, 1, white, light_grey)
        pg.draw.rect(self.surface, color=dark_grey, rect=(x-7, y-7, length_name, height_name))
        self.surface.blit(song_name, (x, y))

    def draw_a_song_name_pressed(self, x, y, name, length_name, height_name):
        font = pg.font.Font(os.path.join(os.getcwd(), "source_code", "Visualisation", "Menu", 'Sunset Club Free Trial.ttf'), 120)
        song_name = font.render(name, 1, white, dark_grey)
        self.surface.blit(song_name, (x-7, y-7))

    def all_menu_drawer_unpressed(self):
        self.draw_easy_button()
        self.draw_medium_button()
        self.draw_hard_button()
        self.draw_a_song_name_unpressed(267, 200, 'Keraunos killer', 235, 48)
        self.draw_a_song_name_unpressed(540, 200, 'Why not', 128, 48)
        self.draw_a_song_name_unpressed(720, 200, 'Live another day', 268, 48)
        self.draw_a_song_name_unpressed(247, 400, 'North memphis', 232, 48)
        self.draw_a_song_name_unpressed(510, 400, 'Delta alpha', 198, 48)
        self.draw_a_song_name_unpressed(740, 400, 'Phonky town', 202, 48)
        self.draw_a_song_name_unpressed(347, 600, 'name1', 107, 48)
        self.draw_a_song_name_unpressed(560, 600, 'name2', 117, 48)
        self.draw_a_song_name_unpressed(773, 600, 'name3', 115, 48)

    def all_menu_drawer_pressed(self, pos):
        """

        :param pos: tuple 1x2, which gives position of a song which should be pressed, returns position in matrix 3x3
        :return: draws a screen with drawn button pos pressed
        """
        song_matrix = [[(267, 200, 'Keraunos killer', 235, 48),
                                        (540, 200, 'Why not', 128, 48),
                                        (720, 200, 'Live another day', 268, 48)],
                                       [(247, 400, 'North memphis', 232, 48),
                                        (510, 400, 'Delta alpha', 198, 48),
                                        (740, 400, 'Phonky town', 202, 48)],
                                       [(347, 600, 'name1', 107, 48),
                                        (560, 600, 'name2', 117, 48),
                                        (773, 600, 'name3', 115, 48)]]

        for i in range(3):
            for j in range(3):
                if (i, j) != pos:
                    self.draw_a_song_name_unpressed(song_matrix[i][j][0], song_matrix[i][j][1], song_matrix[i][j][2], song_matrix[i][j][3], song_matrix[i][j][4])
        for i in range(3):
            for j in range(3):
                if (i, j) == pos:
                    self.draw_a_song_name_pressed(song_matrix[i][j][0], song_matrix[i][j][1], song_matrix[i][j][2], song_matrix[i][j][3], song_matrix[i][j][4])

        self.draw_easy_button()
        self.draw_medium_button()
        self.draw_hard_button()




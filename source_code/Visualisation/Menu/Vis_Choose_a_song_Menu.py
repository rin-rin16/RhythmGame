import pygame as pg

black = (0, 0, 0)
pink = (255, 150, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 6)
white = (255, 255, 255)
blue = (0, 0, 255)
orange = (255, 180, 0)

x = 20

class VisualisationInChooseSongMenu:
    """
    draws beautiful buttons in some place

    Varning! use to draw only function all_drawer!!!!
    """

    def __init__(self, surface):
        self.surface = surface

    def draw_easy_button(self):
        font = pg.font.SysFont('sunsetclubfreetrial', 32)
        easy = font.render('easy', 1, green, black)
        self.surface.blit(easy, (580, 100))

    def draw_medium_button(self):
        font = pg.font.SysFont('sunsetclubfreetrial', 32)
        medium = font.render('medium', 1, yellow, black)
        self.surface.blit(medium, (580-20, 300))

    def draw_hard_button(self):
        font = pg.font.SysFont('sunsetclubfreetrial', 32)
        hard = font.render('hard', 1, red, black)
        self.surface.blit(hard, (580, 500))

    def draw_easy_song_names(self):
        # FIXME: add song names
        font = pg.font.SysFont('sunsetclubfreetrial', 32)
        first_easy_song = font.render('name1', 1, white, black)
        self.surface.blit(first_easy_song, (367-x, 200))
        second_easy_song = font.render('name2', 1, white, black)
        self.surface.blit(second_easy_song, (580-x, 200))
        third_easy_song = font.render('name3', 1, white, black)
        self.surface.blit(third_easy_song, (793-x, 200))

    def draw_medium_song_names(self):
        # FIXME: add song names
        font = pg.font.SysFont('sunsetclubfreetrial', 32)
        first_medium_song = font.render('name1', 1, white, black)
        self.surface.blit(first_medium_song, (367-x, 400))
        second_medium_song = font.render('name2', 1, white, black)
        self.surface.blit(second_medium_song, (580-x, 400))
        third_medium_song = font.render('name3', 1, white, black)
        self.surface.blit(third_medium_song, (793-x, 400))

    def draw_hard_song_names(self):
        # FIXME: add song names
        font = pg.font.SysFont('sunsetclubfreetrial', 32)
        first_hard_song = font.render('name1', 1, white, black)
        self.surface.blit(first_hard_song, (367-x, 600))
        second_hard_song = font.render('name2', 1, white, black)
        self.surface.blit(second_hard_song, (580-x, 600))
        third_hard_song = font.render('name3', 1, white, black)
        self.surface.blit(third_hard_song, (793-x, 600))

    def all_drawer(self):
        self.draw_easy_button()
        self.draw_medium_button()
        self.draw_hard_button()
        self.draw_easy_song_names()
        self.draw_medium_song_names()
        self.draw_hard_song_names()

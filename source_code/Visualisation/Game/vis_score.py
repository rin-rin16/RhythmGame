import pygame as pg
from source_code.Visualisation.Game import vis_mouse_mode as VSM
import os


class DrawCounter:
    """ drawing score counter on the screen"""
    font = pg.font.SysFont('geneva', 70)

    def __init__(self, surface):
        self.surface = surface

    def draw_counter(self, count):
        self.surface.blit(self.font.render(f'Score: {count}', 1, VSM.white), (20, 20))

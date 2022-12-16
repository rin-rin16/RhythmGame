import pygame as pg
from source_code.Visualisation.Game import Vis_Mouse_Mode as vsm


class DrawCounter:
    """ drawing score counter on the screen"""
    font = pg.font.SysFont('geneva', 70)

    def __init__(self, surface):
        self.surface = surface

    def draw_counter(self, count):
        self.surface.blit(self.font.render(f'Score: {count}', True, vsm.white), (20, 20))

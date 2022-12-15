import pygame as pg
import Vis_Mouse_Mode as VSM

class DrawCounter:
    """ drawing score counter on the screen"""
    font = pg.font.SysFont('geneva', 80)

    def __init__(self, surface):
        self.surface = surface

    def draw_counter(self, count):
        self.surface.blit(self.font.render(f'Score:{count}', 1, VSM.white), (20, 20))

import pygame as pg
from source_code.Sound_Rhytm.sound_rhytm_source_code import sound_rhytm_mouse as sr
import Menu as start_m
import numpy as np

choosing_song = sr.BullVariables(True)

choosed_song = [None, None]

list_of_song_size = [[[267, 200, 502-267, 48], [540, 200, 668-540, 48], [720, 200, 988-720, 48]],
                     [[247, 400, 479-247, 48], [510, 400, 942-510, 48], [740, 400, 942-740, 48]],
                     [[347, 600, 454-347, 48], [560, 600, 677-560, 48], [773, 600, 888-773, 48]]]

class ChoosingButton(start_m.Button):
    def __init__(self, *args, pos):
        super().__init__(*args)
        self.pos = pos
        self.is_clicked = False


    def pos_getter(self):
        return self.pos

songs = np.array([[ChoosingButton(list_of_song_size[i][0]),
          ChoosingButton(list_of_song_size[i][1]),
          ChoosingButton(list_of_song_size[i][2]),
          ChoosingButton(list_of_song_size[i][3]), '', (i//3, i % 3)] for i in range(9)])

songs.reshape(3, 3)

was_hit = sr.BullVariables(False)

def getter_position_of_a_clicked_button():
    """

    :return: position of a clicked button position in format tuple 1x2, position in songs
    """
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            for i in range(3):
                for j in range(3):
                    if songs[i][j].is_click(event):
                        was_hit.changer()
                        return songs[i][j].pos_getter()





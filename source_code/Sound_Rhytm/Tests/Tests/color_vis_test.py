import pygame as pg
import time as time
import pandas as pd
from source_code.Sound_Rhytm.songs_bpm import songs_bpm as sb
from source_code.Sound_Rhytm.Tests.Test_source_code import SR_color as SR
from source_code.Sound_Rhytm.Tests.Test_source_code import MM_color as M_Eng
from source_code.Visualisation.Game import vis_mouse_mode as Ms_Vis
from source_code.Sound_Rhytm.Tests.Test_source_code import Test_St_M as start_menu
from source_code.Visualisation.Game import text_before_game as TBG

# width, height = 1280, 720       # Screen's width and height        # Took this into engine file
# background_color = (0, 0, 0)

# pg.display.init()

# screen = pg.display.set_mode((width, height))
# screen.fill(background_color)
# pg.display.flip()

running = SR.BullVariables()
clock = pg.time.Clock()
balls = M_Eng.ball_initializer()

while running.getter():
    menu_running = True
    if menu_running:
        start_menu.draw_menu_buttons()
    start_menu.logic_of_menu_buttons(start_menu.play_button, start_menu.quit_button, running, start_menu.trek_choice,
                                     clock)

    SR.start_time.setter(time.time())
    SR.Trak_1_Player.music_player(SR.start_time, 60 / sb.K_K[0], sb.K_K[1], 0.002, 0.002, balls, running,
                                  start_menu.trek_number.getter())
    SR.Track_2_Player.music_player(SR.start_time, 60 / sb.L_A_D[0], sb.L_A_D[1], 0.002, 0.002, balls, running,
                                   start_menu.trek_number.getter())
    SR.Track_3_Player.music_player(SR.start_time, 60 / sb.P_T[0], sb.P_T[1], 0.002, 0.002, balls, running,
                                   start_menu.trek_number.getter())
    SR.Track_4_Player.music_player(SR.start_time, 60 / sb.Y_N[0], sb.Y_N[1], 0.002, 0.002, balls, running,
                                   start_menu.trek_number.getter())
    SR.Track_5_Player.music_player(SR.start_time, 60 / sb.D_A[0], sb.D_A[1], 0.002, 0.002, balls, running,
                                   start_menu.trek_number.getter())

pg.mixer.music.stop()
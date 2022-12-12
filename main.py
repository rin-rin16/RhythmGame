import pygame as pg
import time as time
import pandas as pd
from source_code.Sound_Rhytm.songs_bpm import songs_bpm as sb
from source_code.Classes import Classes as CL
from source_code.Sound_Rhytm import Sound_Rhytm as SR
from source_code.Engine import Mouse_Mode as M_Eng
from source_code.Visualisation.Game import Vis_Mouse_Mode as Ms_Vis
from source_code.Engine.menu import start_menu as start_menu
from source_code.Visualisation.Game import Text_Before_Game as TBG


running = CL.BullVariables()
pressing_start = CL.BullVariables(False)
pressing_quit = CL.BullVariables(False)
pressing_song_name = CL.NumVariables(0)
clock = pg.time.Clock()
[balls, draw_balls] = M_Eng.ball_initializer()
mode_type = CL.NumVariables()
while running.getter():
    menu_running = True
    start_menu.logic_of_menu_buttons(running, start_menu.trek_choice, clock, pressing_start, pressing_quit,mode_type)

    mode_tracker = 1

    CL.start_time.setter(time.time())

    if mode_tracker == 1:
        SR.Track_1_Player.music_player(CL.start_time, 60 / sb.K_K[0], sb.K_K[1], 0.1, 0.15, draw_balls, balls, running,
                                      start_menu.trek_number.getter())
        SR.Track_2_Player.music_player(CL.start_time, 60 / sb.L_A_D[0], sb.L_A_D[1], 0.1, 0.15, draw_balls, balls, running,
                                       start_menu.trek_number.getter())
        SR.Track_3_Player.music_player(CL.start_time, 60 / sb.P_T[0], sb.P_T[1], 0.1, 0.15, draw_balls, balls, running,
                                       start_menu.trek_number.getter())
        SR.Track_4_Player.music_player(CL.start_time, 60 / sb.Y_N[0], sb.Y_N[1], 0.1, 0.15, draw_balls, balls, running,
                                       start_menu.trek_number.getter())
        SR.Track_5_Player.music_player(CL.start_time, 60 / sb.D_A[0], sb.D_A[1], 0.1, 0.15, draw_balls, balls, running,
                                       start_menu.trek_number.getter())

pg.mixer.music.stop()

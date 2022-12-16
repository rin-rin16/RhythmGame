import pygame as pg
import time as time
import pandas as pd
from source_code.Sound_Rhytm.songs_bpm import songs_bpm as sb
from source_code.Classes import Classes as CL
from source_code.Sound_Rhytm import Sound_Rhytm_Mouse as SR
from source_code.Engine import Mouse_Mode as M_Eng
from source_code.Engine import Keyboard_Mode as K_Eng
from source_code.Visualisation.Game import Vis_Mouse_Mode as Ms_Vis
from source_code.Engine.menu import Menu as start_menu
from source_code.Visualisation.Game import Text_Before_Game as TBG
from source_code.Classes import timer_creator as tcr
from source_code.Sound_Rhytm import Sound_Rhytm_Keyboard as KR
from source_code.Visualisation.Game import Vis_score as VS

pg.display.set_caption('RhytmGame')

running = CL.BullVariables()
pressing_start = CL.BullVariables(False)
pressing_quit = CL.BullVariables(False)
pressing_song_name = CL.NumVariables(0)
pressing = CL.NumVariables('none')
clock = pg.time.Clock()
[balls, draw_balls] = M_Eng.ball_initializer()
ker_arr_list, lad_arr_list, pht_arr_list, wyn_arr_list, daa_arr_list = K_Eng.arrow_initializer(K_Eng.rand_generator(tcr.l_K_K), tcr.l_K_K),        \
                                                                        K_Eng.arrow_initializer(K_Eng.rand_generator(tcr.l_L_A_D), tcr.l_L_A_D),     \
                                                                        K_Eng.arrow_initializer(K_Eng.rand_generator(tcr.l_P_T), tcr.l_P_T),       \
                                                                        K_Eng.arrow_initializer(K_Eng.rand_generator(tcr.l_W_N), tcr.l_W_N),       \
                                                                        K_Eng.arrow_initializer(K_Eng.rand_generator(tcr.l_D_A), tcr.l_D_A)
mode_type = CL.NumVariables()
mode_choice = CL.BullVariables(False)
play_quit_menu = CL.BullVariables(True)
ending = CL.NumVariables(True)
trek_choice = CL.NumVariables(0)
while running.getter():
    menu_running = True
    playing = True
    start_menu.logic_of_menu_buttons(running, trek_choice, clock, mode_type, mode_choice, ending, play_quit_menu,pressing)
    CL.start_time.setter(time.time())

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

    KR.Track_6_Player.music_player(CL.start_time, 60 / sb.K_K[0], sb.K_K[1], 0.1, 0.15, ker_arr_list, running,
                                   start_menu.trek_number.getter(), tcr.l_K_K)
    KR.Track_7_Player.music_player(CL.start_time, 60 / sb.L_A_D[0], sb.L_A_D[1], 0.1, 0.15, lad_arr_list, running,
                                   start_menu.trek_number.getter(), tcr.l_L_A_D)
    KR.Track_8_Player.music_player(CL.start_time, 60 / sb.P_T[0], sb.P_T[1], 0.1, 0.15, pht_arr_list, running,
                                   start_menu.trek_number.getter(), tcr.l_P_T)
    KR.Track_9_Player.music_player(CL.start_time, 60 / sb.Y_N[0], sb.Y_N[1], 0.1, 0.15, wyn_arr_list, running,
                                   start_menu.trek_number.getter(), tcr.l_W_N)
    KR.Track_10_Player.music_player(CL.start_time, 60 / sb.D_A[0], sb.D_A[1], 0.1, 0.15, daa_arr_list, running,
                                   start_menu.trek_number.getter(), tcr.l_D_A)

pg.mixer.music.stop()

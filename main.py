import pygame as pg
import time as time
from source_code.Sound_Rhytm.songs_bpm import songs_bpm as sb
from source_code.Classes import Classes as Cl
from source_code.Sound_Rhytm import Sound_Rhytm_Mouse as Sr
from source_code.Engine import Mouse_Mode as M_Eng
from source_code.Engine import Keyboard_Mode as K_Eng
from source_code.Engine.menu import Menu as Start_menu
from source_code.Classes import timer_creator as tcr
from source_code.Sound_Rhytm import Sound_Rhytm_Keyboard as Kr
from source_code.Engine import Final
pg.display.set_caption('RhytmGame')

running = Cl.BullVariables()
pressing_start = Cl.BullVariables(False)
pressing_quit = Cl.BullVariables(False)
pressing_song_name = Cl.NumVariables(0)
pressing = Cl.NumVariables('none')
clock = pg.time.Clock()
[balls, draw_balls] = M_Eng.ball_initializer()
ker_arr_list, lad_arr_list, pht_arr_list, wyn_arr_list, daa_arr_list = K_Eng.arrow_initializer(K_Eng.rand_generator(tcr.l_K_K), tcr.l_K_K),        \
                                                                        K_Eng.arrow_initializer(K_Eng.rand_generator(tcr.l_L_A_D), tcr.l_L_A_D),     \
                                                                        K_Eng.arrow_initializer(K_Eng.rand_generator(tcr.l_P_T), tcr.l_P_T),       \
                                                                        K_Eng.arrow_initializer(K_Eng.rand_generator(tcr.l_W_N), tcr.l_W_N),       \
                                                                        K_Eng.arrow_initializer(K_Eng.rand_generator(tcr.l_D_A), tcr.l_D_A)
mode_type = Cl.NumVariables()
mode_choice = Cl.BullVariables(False)
play_quit_menu = Cl.BullVariables(True)
ending = Cl.NumVariables(True)
trek_choice = Cl.NumVariables(0)
final_running = Cl.BullVariables(False)
while running.getter():
    menu_running = True
    Start_menu.logic_of_menu_buttons(running, trek_choice, clock, mode_type, mode_choice, play_quit_menu, pressing)
    Cl.start_time.setter(time.time())

    Sr.Track_1_Player.music_player(Cl.start_time, 60 / sb.K_K[0], sb.K_K[1], 0.1, 0.15, draw_balls, balls, running,
                                   Start_menu.trek_number.getter(), final_running)
    Sr.Track_2_Player.music_player(Cl.start_time, 60 / sb.L_A_D[0], sb.L_A_D[1], 0.1, 0.15, draw_balls, balls, running,
                                   Start_menu.trek_number.getter(), final_running)
    Sr.Track_3_Player.music_player(Cl.start_time, 60 / sb.P_T[0], sb.P_T[1], 0.1, 0.15, draw_balls, balls, running,
                                   Start_menu.trek_number.getter(), final_running)
    Sr.Track_4_Player.music_player(Cl.start_time, 60 / sb.Y_N[0], sb.Y_N[1], 0.1, 0.15, draw_balls, balls, running,
                                   Start_menu.trek_number.getter(), final_running)
    Sr.Track_5_Player.music_player(Cl.start_time, 60 / sb.D_A[0], sb.D_A[1], 0.1, 0.15, draw_balls, balls, running,
                                   Start_menu.trek_number.getter(), final_running)

    Kr.Track_6_Player.music_player(Cl.start_time, 60 / sb.K_K[0], sb.K_K[1], 0.1, 0.15, ker_arr_list, running,
                                   Start_menu.trek_number.getter(), tcr.l_K_K)
    Kr.Track_7_Player.music_player(Cl.start_time, 60 / sb.L_A_D[0], sb.L_A_D[1], 0.1, 0.15, lad_arr_list, running,
                                   Start_menu.trek_number.getter(), tcr.l_L_A_D)
    Kr.Track_8_Player.music_player(Cl.start_time, 60 / sb.P_T[0], sb.P_T[1], 0.1, 0.15, pht_arr_list, running,
                                   Start_menu.trek_number.getter(), tcr.l_P_T)
    Kr.Track_9_Player.music_player(Cl.start_time, 60 / sb.Y_N[0], sb.Y_N[1], 0.1, 0.15, wyn_arr_list, running,
                                   Start_menu.trek_number.getter(), tcr.l_W_N)
    Kr.Track_10_Player.music_player(Cl.start_time, 60 / sb.D_A[0], sb.D_A[1], 0.1, 0.15, daa_arr_list, running,
                                    Start_menu.trek_number.getter(), tcr.l_D_A)

    Final.logic(final_running.getter(), running, pressing, M_Eng.screen, mode_type, mode_choice, trek_choice, play_quit_menu)

pg.mixer.music.stop()

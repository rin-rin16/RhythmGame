import pygame as pg
import time as time
import pandas as pd
from source_code.Sound_Rhytm.songs_bpm import songs_bpm as sb
from source_code.Sound_Rhytm.Tests.Test_source_code import SR_Vis_Test as SR
from source_code.Sound_Rhytm.Tests.Test_source_code import MM_Vis_Test as M_Eng
from source_code.Visualisation.Game import Vis_Mouse_Mode as Ms_Vis
from source_code.Engine.menu import start_menu as start_menu
from source_code.Visualisation.Game import Text_Before_Game as TBG

# width, height = 1280, 720       # Screen's width and height        # Took this into engine file
# background_color = (0, 0, 0)

# pg.display.init()

# screen = pg.display.set_mode((width, height))
# screen.fill(background_color)
# pg.display.flip()

running = SR.BullVariables()
clock = pg.time.Clock()
[balls, draw_balls] = M_Eng.ball_initializer()

while running.getter():
    menu_running = True
    if menu_running:
        start_menu.make_the_buttons_great_again(running)
    if start_menu.trek_choice:
        choice_running = True
        while choice_running:
            M_Eng.screen.fill((0, 0, 0))

            amount_of_buttons = 5
            trek_button = [0] * amount_of_buttons
            for i in range(amount_of_buttons):
                trek_button[i] = start_menu.TrekButton(100, i * 100 + 100, 50, 50, f'trek_button_{i + 1}',
                                                       trek_number=i + 1)
                trek_button[i].write_text_on_button(M_Eng.screen)
            back_to_menu = start_menu.Button(500, 100, 50, 50, 'Back')
            back_to_menu.write_text_on_button(M_Eng.screen)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    for i in range(amount_of_buttons):
                        if trek_button[i].is_click(event):
                            clock.tick(1)
                            #for j in range(0, 5):
                                #TBG.countdown(j)
                            start_menu.trek_number = i + 1
                            choice_running = False
                    if back_to_menu.is_click(event):
                        menu_running = True
                        choice_running = False
                        start_menu.trek_choice = False
                elif event.type == pg.QUIT:
                    choice_running = False
                    running.setter(False)

    SR.start_time.setter(time.time())
    SR.Trak_1_Player.music_player(SR.start_time, 60 / sb.K_K[0], sb.K_K[1], 0.1, 0.15, draw_balls, balls, running,     # FIXME: подобрать нормальный бит и фазу
                                  start_menu.trek_number)
    SR.Track_2_Player.music_player(SR.start_time, 60 / sb.L_A_D[0], sb.L_A_D[1], 0.1, 0.15, draw_balls, balls, running,    # FIXME: подобрать нормальный бит и фазу
                                   start_menu.trek_number)

pg.mixer.music.stop()

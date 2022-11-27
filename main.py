import pygame as pg
import time as time
import pandas as pd
from source_code.Sound_Rhytm import Sound_Rhytm as SR
from source_code.Engine import Mouse_Mode as M_Eng
from source_code.Visualisation.Game import Vis_Mouse_Mode as Ms_Vis
from source_code.Engine.menu import start_menu as start_menu

#width, height = 1280, 720       # Screen's width and height        # Took this into engine file
#background_color = (0, 0, 0)

#pg.display.init()

#screen = pg.display.set_mode((width, height))
#screen.fill(background_color)
#pg.display.flip()

SR.start_time.setter(time.time())

running = SR.BullVariables()

[balls, draw_balls] = M_Eng.ball_initializer()

while running.getter():
    menu_running = True
    if menu_running:
        M_Eng.screen.fill((0, 0, 0))
        play_button = start_menu.PlayButton(100, 100, 50, 50, 'play_button')
        quit_button = start_menu.Button(100, 200, 50, 50, 'quit_button')
        play_button.write_text_on_button(M_Eng.screen)
        quit_button.write_text_on_button(M_Eng.screen)
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if play_button.is_click(event):
                    play_button.start_game()
                    menu_running = False
                if quit_button.is_click(event):
                    running.setter(False)
            elif event.type == pg.QUIT:
                running.setter(False)

    if start_menu.trek_choice:
        choice_running = True
        while choice_running:
            M_Eng.screen.fill((0, 0, 0))

            amount_of_buttons = 5
            trek_button = [0]*amount_of_buttons
            for i in range(amount_of_buttons):
                trek_button[i] = start_menu.TrekButton(100, i*100+100, 50, 50, f'trek_button_{i+1}', trek_number=i+1)
                trek_button[i].write_text_on_button(M_Eng.screen)
            back_to_menu = start_menu.Button(500,100,50,50,'Back')
            back_to_menu.write_text_on_button(M_Eng.screen)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    for i in range(amount_of_buttons):
                        if trek_button[i].is_click(event):
                            start_menu.trek_number = i+1
                            choice_running = False
                    if back_to_menu.is_click(event):
                        menu_running = True
                        choice_running = False
                        start_menu.trek_choice = False
                elif event.type == pg.QUIT:
                    choice_running = False
                    running.setter(False)

    SR.Trak_1_Player.music_player(SR.start_time, 60/137, 0.6, 0.1, 0.15, draw_balls, balls, running,
                                  start_menu.trek_number)
    SR.Track_2_Player.music_player(SR.start_time, 60 / 137, 0.6, 0.1, 0.15, draw_balls, balls, running,
                                  start_menu.trek_number)



pg.mixer.music.stop()
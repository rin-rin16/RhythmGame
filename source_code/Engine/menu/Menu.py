import pygame as pg
from source_code.Engine import Mouse_Mode as M_Eng
from source_code.Visualisation.Game import Text_Before_Game as TBG
from source_code.Visualisation.Menu import Vis_Start_Menu as VSM
from source_code.Classes import Classes as CL
from source_code.Visualisation.Menu import Vis_Choose_a_song_Menu as VCSM
from source_code.Visualisation.Menu import Vis_Choose_mode_menu as VCMM




surf = M_Eng.screen
menu_screen = VSM.DrawAMenuButton(surf)
choose_song_menu = VCSM.VisualisationInChooseSongMenu(surf)
choose_mode_menu = VCMM.DrawAMenuButton(surf)
menu = True
trek_choice = CL.NumVariables(0)
trek_number = CL.NumVariables()


def logic_of_menu_buttons(running, trek_choice, clock, pressing_start, pressing_quit, mode_type, mode_choice,
                          play_quit_menu, pressing):
    """ describes the logic of menu buttons """

    if play_quit_menu.getter():
        if pressing.getter() == 'none':
            menu_screen.all_menu_drawer_pressed('none')
            pg.display.update()
        M_Eng.screen.fill((0, 0, 0))
        play_button = CL.PlayButton(480, 200, 320, 180, 'play_button')
        quit_button = CL.Button(540, 450, 200, 138, 'quit_button')

        for event in pg.event.get():
            if pressing.getter() == 'none':
                if event.type == pg.MOUSEBUTTONDOWN:
                    if play_button.is_click(event):  # PLAY/QUIT menu
                        M_Eng.screen.fill((0, 0, 0))
                        menu_screen.all_menu_drawer_pressed('start')
                        pg.display.update()
                        pressing.setter('start')
                    if quit_button.is_click(event):
                        M_Eng.screen.fill((0, 0, 0))
                        menu_screen.all_menu_drawer_pressed('quit')
                        pg.display.update()
                        pressing.setter('quit')
                elif event.type == pg.QUIT:
                    running.setter(False)

            elif event.type == pg.MOUSEBUTTONUP:
                if pressing.getter() == 'start':
                    mode_choice.setter(True)
                    play_quit_menu.setter(False)
                    trek_choice.setter(0)
                    pressing.setter('none')
                else:
                    running.setter(False)
                    pressing.setter('none')
                pressing.setter('none')

    if mode_choice.getter():  # MM/KM menu
        M_Eng.screen.fill((0, 0, 0))
        mm_button = CL.Button(495, 210, 284, 135, '')
        km_button = CL.Button(420, 440, 440, 134, '')
        back_to_menu = CL.Button(1070, 600, 170, 95, '')
        choose_mode_menu.all_menu_drawer_pressed('none')
        pg.display.update()
        while mode_choice.getter():
            for event in pg.event.get():
                if pressing.getter() == 'none':
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if mm_button.is_click(event):
                            M_Eng.screen.fill((0,0,0))
                            choose_mode_menu.all_menu_drawer_pressed('mouse')
                            pg.display.update()
                            pressing.setter('mouse')
                        if km_button.is_click(event):
                            M_Eng.screen.fill((0,0,0))
                            choose_mode_menu.all_menu_drawer_pressed('keyboard')
                            pg.display.update()
                            pressing.setter('keyboard')
                        if back_to_menu.is_click(event):
                            M_Eng.screen.fill((0,0,0))
                            choose_mode_menu.all_menu_drawer_pressed('back')
                            pg.display.update()
                            pressing.setter('back')
                    elif event.type == pg.QUIT:
                        mode_choice.setter(False)
                        running.setter(False)
                elif event.type == pg.MOUSEBUTTONUP:
                    if pressing.getter() == 'mouse':
                        mode_type.setter(1)
                        mode_choice.setter(False)
                        play_quit_menu.setter(False)
                        trek_choice.setter(1)
                        pressing.setter('none')
                    elif pressing.getter() == 'keyboard':
                        mode_type.setter(2)
                        mode_choice.setter(False)
                        play_quit_menu.setter(False)
                        trek_choice.setter(2)
                        pressing.setter('none')
                    elif pressing.getter() == 'back':
                        mode_type.setter(0)
                        mode_choice.setter(False)
                        trek_choice.setter(0)
                        play_quit_menu.setter(True)
                        pressing.setter('none')
                    pressing.setter('none')

    if trek_choice.getter() == 1:  # MM Trek Choicing menu
        choice_running = True
        while choice_running:
            amount_of_buttons = 5
            trek_button = [0] * amount_of_buttons
            trek_button[0] = CL.TrekButton(343, 145, 235, 48, '')
            trek_button[1] = CL.TrekButton(638, 145, 268, 48, '')
            trek_button[2] = CL.TrekButton(638, 345, 202, 48, '')
            trek_button[3] = CL.TrekButton(540, 600, 130, 48, '')
            trek_button[4] = CL.TrekButton(378, 345, 130, 48, '')
            if pressing.getter() == 'none':
                M_Eng.screen.fill((0, 0, 0))
                choose_song_menu.all_menu_drawer_pressed('none')
                pg.display.update()
            back_to_menu = CL.Button(1100 - 7, 600 - 7, 150, 78, '')
            pg.display.update()
            for event in pg.event.get():
                if pressing.getter() == 'none':
                    if event.type == pg.MOUSEBUTTONDOWN:
                        for i in range(amount_of_buttons):
                            if trek_button[i].is_click(event):
                                M_Eng.screen.fill((0, 0, 0))
                                choose_song_menu.all_menu_drawer_pressed(i)
                                pg.display.update()
                                pressing.setter(i)
                        if back_to_menu.is_click(event):
                            M_Eng.screen.fill((0, 0, 0))
                            choose_song_menu.all_menu_drawer_pressed('back')
                            pg.display.update()
                            pressing.setter('back')
                    elif event.type == pg.QUIT:
                        choice_running = False
                        running.setter(False)
                elif event.type == pg.MOUSEBUTTONUP:
                    for i in range(amount_of_buttons):
                        if pressing.getter() == i:
                            clock.tick(1)
                            for j in [4, 3, 2, 1, 0]:
                                TBG.countdown(j)
                            trek_number.setter(i + 1)
                            choice_running = False
                            mode_choice.setter(False)
                            pressing.setter('none')
                    if pressing.getter() == 'back':
                        mode_choice.setter(True)
                        choice_running = False
                        trek_choice.setter(0)
                        pressing.setter('none')
                    pressing.setter('none')

    if trek_choice.getter() == 2:  # KM Trek Choicing menu
        choice_running = True
        while choice_running:
            amount_of_buttons = 5
            trek_button = [0] * amount_of_buttons
            trek_button[0] = CL.TrekButton(343, 145, 235, 48, '')
            trek_button[1] = CL.TrekButton(638, 145, 268, 48, '')
            trek_button[2] = CL.TrekButton(638, 345, 202, 48, '')
            trek_button[3] = CL.TrekButton(540, 600, 130, 48, '')
            trek_button[4] = CL.TrekButton(378, 345, 130, 48, '')
            if pressing.getter() == 'none':
                M_Eng.screen.fill((0, 0, 0))
                choose_song_menu.all_menu_drawer_pressed('none')
                pg.display.update()
            back_to_menu = CL.Button(1100 - 7, 600 - 7, 150, 78, '')
            pg.display.update()
            for event in pg.event.get():
                if pressing.getter() == 'none':
                    if event.type == pg.MOUSEBUTTONDOWN:
                        for i in range(amount_of_buttons):
                            if trek_button[i].is_click(event):
                                M_Eng.screen.fill((0, 0, 0))
                                choose_song_menu.all_menu_drawer_pressed(i)
                                pg.display.update()
                                pressing.setter(i)
                        if back_to_menu.is_click(event):
                            M_Eng.screen.fill((0, 0, 0))
                            choose_song_menu.all_menu_drawer_pressed('back')
                            pg.display.update()
                            pressing.setter('back')
                    elif event.type == pg.QUIT:
                        choice_running = False
                        running.setter(False)
                elif event.type == pg.MOUSEBUTTONUP:
                    for i in range(amount_of_buttons):
                        if pressing.getter() == i:
                            clock.tick(1)
                            for j in [4, 3, 2, 1, 0]:
                                TBG.countdown(j)
                            trek_number.setter(i + 6)
                            choice_running = False
                            mode_choice.setter(False)
                            pressing.setter('none')
                    if pressing.getter() == 'back':
                        mode_choice.setter(True)
                        choice_running = False
                        trek_choice.setter(0)
                        pressing.setter('none')
                    pressing.setter('none')

def pause(event, clock, running):
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
            run_pause = True
            while run_pause:
                M_Eng.screen.fill((0, 0, 0))
                resume = CL.Button(390, 240, 550, 180, '')
                resume.write_text_on_button(M_Eng.screen)
                to_menu = CL.Button(530, 480, 265, 138, '')
                to_menu.write_text_on_button(M_Eng.screen)
                pg.display.update()
                clock.tick(100)
                for action in pg.event.get():
                    if action.type == pg.QUIT:
                        running.setter(False)
                        # FIXME не закрывается при нажатии на крестик :(
                    elif action.type == pg.MOUSEBUTTONDOWN:
                        if resume.is_click(action):
                            run_pause = False
                            # FIXME должна продолжаться игра ( по идее если сунуть эту функцию туда куда надо,
                            # то все должно быть окей: меню паузы закроется и продолжится игра,
                            # но как это будет на практике хз если честно)

                        if to_menu.is_click(action):
                            run_pause = False
                            # FIXME должно открываться меню выбора трека (возможно стоит заново вызывать функцию отображения меню выбора,
                            # либо как-то выходить из этого цикла и запуска меню выбора, путем деланья trek_choice трушным

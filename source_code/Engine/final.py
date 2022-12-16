from source_code.Classes import classes as CL
import pygame as pg
from source_code.Visualisation.Menu import vis_end_menu as vem
from source_code.Engine import mouse_mode as M_Eng

surf = M_Eng.screen
score = 0
final_screen = vem.DrawAMenuButton(surf, score)


def logic(final_running, running, pressing, screen, mode_type, mode_choice, trek_choice, play_quit_menu, trek_number):
    if final_running.getter():
        screen.fill((0, 0, 0))
        go_to_menu = CL.Button(380, 390, 550, 130, 'Go_to_menu')
        quit_from_game = CL.Button(380, 560, 550, 130, 'Quit')
        go_to_menu.write_text_on_button(screen)
        quit_from_game.write_text_on_button(screen)
        pg.display.update()

        while final_running.getter():
            if pressing.getter() == 'none':
                final_screen.all_menu_drawer_pressed('none')
                pg.display.update()
            for event in pg.event.get():
                if pressing.getter() == 'none':
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if quit_from_game.is_click(event):
                            M_Eng.screen.fill((0, 0, 0))
                            final_screen.all_menu_drawer_pressed('quit')
                            pg.display.update()
                            pressing.setter('quit')
                        elif go_to_menu.is_click(event):
                            M_Eng.screen.fill((0, 0, 0))
                            final_screen.all_menu_drawer_pressed('to_menu')
                            pg.display.update()
                            pressing.setter('to_menu')
                    elif event.type == pg.QUIT:
                        running.setter(False)
                        final_running.setter(False)

                elif event.type == pg.MOUSEBUTTONUP:
                    if pressing.getter() == 'quit':
                        final_running.setter(False)
                        running.setter(False)
                        pressing.setter('none')
                    elif pressing.getter() == 'to_menu':
                        mode_type.setter(0)
                        mode_choice.setter(True)
                        trek_choice.setter(0)
                        pressing.setter('none')
                        play_quit_menu.setter(True)
                        final_running.setter(False)
                        trek_number.setter(0)
                        pressing.setter('none')
                    pressing.setter('none')

from source_code.Classes import classes as CL
import pygame as pg


def logic(final_running,running,pressing,screen,mode_type,mode_choice,trek_choice,play_quit_menu):
    if final_running.getter():
        screen.fill((0, 0, 0))
        go_to_menu = CL.Button(480, 200, 320, 180, 'Go_to_menu')
        quit = CL.Button(540, 450, 200, 138, 'Quit')
        go_to_menu.write_text_on_button(screen)
        quit.write_text_on_button(screen)
        pg.display.update()

        while final_running.getter():
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if quit.is_click(event):
                        final_running = False
                        running.setter(False)
                    elif go_to_menu.is_click(event):
                        mode_type.setter(0)
                        mode_choice.setter(False)
                        trek_choice.setter(0)
                        play_quit_menu.setter(True)
                        final_running.setter(False)
                elif event.type == pg.QUIT:
                    running.setter(False)
                    final_running = False


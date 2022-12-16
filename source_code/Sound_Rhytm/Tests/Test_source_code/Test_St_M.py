import pygame as pg
from source_code.Engine import mouse_mode as M_Eng
from source_code.Visualisation.Game import text_before_game as TBG
from source_code.Sound_Rhytm.Tests.Test_source_code import Vis_Start_Menu_Test as VSM
from source_code.Classes import classes as CL

class Button:

    def __init__(self, x, y, xsize, ysize, text):
        """ constructor of class "Button" """
        self.x = x
        self.y = y
        self.text = text
        self.xsize = xsize
        self.ysize = ysize

    def is_click(self, event):
        """ return True if you click on the Button """
        if self.x < event.pos[0] < self.x + self.xsize and self.y < event.pos[1] < self.y + self.ysize:
            return True

    def write_text_on_button(self, screen):
        """ writing text on the element of class "Button" """
        myfont = pg.font.SysFont("monospace", 30)
        text = myfont.render(str(self.text), 1, (255, 255, 255))
        screen.blit(text, (self.x, self.y))



menu = True
trek_choice = CL.BullVariables(False)
trek_number = CL.NumVariables()


class PlayButton(Button):
    def __init__(self, *args):
        """ constructor of class "PlayButton" which the subclass of class "Button" """
        super().__init__(*args)

    def start_game(self):
        """ Using for run game if player click on the element of PlayButton """
        trek_choice.setter(True)


class TrekButton(Button):
    def __init__(self, *args, trek_number):
        """ constructor of class "TrekButton" which the subclass of class "Button" """
        super().__init__(*args)
        self.trek_number = trek_number

    def get_trek_number(self):
        """ Return number of trek for which the element of TrekButton is responsible"""
        return self.trek_number

surf = M_Eng.screen
menu_screen = VSM.DrawAMenuButton(surf)

def draw_menu_buttons():
    """ the function responsible for drawing the "play" and "exit" buttons """
    global play_button
    global quit_button
    M_Eng.screen.fill((0, 0, 0))
    play_button = PlayButton(480, 200, 320, 180, 'play_button')
    quit_button = Button(540, 450, 200, 138, 'quit_button')
    menu_screen.all_menu_drawer_pressed('none')
    pg.display.update()


def logic_of_menu_buttons(play_button, quit_button, running, trek_choice, clock):
    """ describes the logic of menu buttons """
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if play_button.is_click(event):
                M_Eng.screen.fill((0, 0, 0))
                menu_screen.all_menu_drawer_pressed('start')
                pg.display.update()
                clock.tick(0.99)
                play_button.start_game()
                menu_running = False
            if quit_button.is_click(event):
                M_Eng.screen.fill((0, 0, 0))
                menu_screen.all_menu_drawer_pressed('quit')
                pg.display.update()
                clock.tick(0.99)
                running.setter(False)
        elif event.type == pg.QUIT:
            running.setter(False)
    if trek_choice.getter():
        choice_running = True
        while choice_running:
            M_Eng.screen.fill((0, 0, 0))
            amount_of_buttons = 9
            trek_button = [0] * amount_of_buttons
            for i in range(amount_of_buttons):
                trek_button[i] = TrekButton(100, i * 70 + 70, 50, 50, f'trek_button_{i + 1}',
                                            trek_number=i + 1)
                trek_button[i].write_text_on_button(M_Eng.screen)
            back_to_menu = Button(500, 100, 50, 50, 'Back')
            back_to_menu.write_text_on_button(M_Eng.screen)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    for i in range(amount_of_buttons):
                        if trek_button[i].is_click(event):
                            clock.tick(1)
                            #for j in [4,3,2,1,0]:
                            #    TBG.countdown(j)
                            trek_number.setter(i + 1)
                            choice_running = False
                    if back_to_menu.is_click(event):
                        menu_running = True
                        choice_running = False
                        trek_choice.setter(False)
                elif event.type == pg.QUIT:
                    choice_running = False
                    running.setter(False)

import pygame as pg
from source_code.Engine import Mouse_Mode as M_Eng
from source_code.Visualisation.Game import Text_Before_Game as TBG


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


# start = 0
menu = True
trek_choice = False
trek_number = 0


class PlayButton(Button):
    def __init__(self, *args):
        """ constructor of class "PlayButton" which the subclass of class "Button" """
        super().__init__(*args)

    def start_game(self):
        """ Using for run game if player click on the element of PlayButton """
        global trek_choice
        trek_choice = True


class TrekButton(Button):
    def __init__(self, *args, trek_number):
        """ constructor of class "TrekButton" which the subclass of class "Button" """
        super().__init__(*args)
        self.trek_number = trek_number

    def get_trek_number(self):
        """ Return number of trek for which the element of TrekButton is responsible"""
        return self.trek_number


def draw_menu_buttons():
    """ the function responsible for drawing the "play" and "exit" buttons """
    global play_button
    global quit_button
    M_Eng.screen.fill((0, 0, 0))
    play_button = PlayButton(100, 100, 50, 50, 'play_button')
    quit_button = Button(100, 200, 50, 50, 'quit_button')
    play_button.write_text_on_button(M_Eng.screen)
    quit_button.write_text_on_button(M_Eng.screen)
    pg.display.update()


def logic_of_menu_buttons(play_button, quit_button, running, trek_choice, clock):
    global trek_number
    """ describes the logic of menu buttons """
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if play_button.is_click(event):
                play_button.start_game()
                menu_running = False
            if quit_button.is_click(event):
                running.setter(False)
        elif event.type == pg.QUIT:
            running.setter(False)

    if trek_choice:
        choice_running = True
        while choice_running:
            M_Eng.screen.fill((0, 0, 0))
            amount_of_buttons = 5
            trek_button = [0] * amount_of_buttons
            for i in range(amount_of_buttons):
                trek_button[i] = TrekButton(100, i * 100 + 100, 50, 50, f'trek_button_{i + 1}',
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
                                #TBG.countdown(j)
                            trek_number = i + 1
                            choice_running = False
                    if back_to_menu.is_click(event):
                        menu_running = True
                        choice_running = False
                        trek_choice = False
                elif event.type == pg.QUIT:
                    choice_running = False
                    running.setter(False)
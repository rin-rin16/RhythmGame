import pygame as pg
from source_code.Engine import Mouse_Mode as M_Eng

class Button:

    def __init__(self, x, y, xsize, ysize, text):
        self.x = x
        self.y = y
        self.text = text
        self.xsize = xsize
        self.ysize = ysize

    def is_click(self, event):
        if self.x < event.pos[0] < self.x + self.xsize and self.y < event.pos[1] < self.y + self.ysize:
            return True

    def write_text_on_button(self,screen):
        myfont = pg.font.SysFont("monospace", 30)
        text = myfont.render(str(self.text), 1, (255, 255, 255))
        screen.blit(text, (self.x, self.y))


# start = 0
menu = True
trek_choice = False
trek_number = 0


class PlayButton(Button):
    def __init__(self, *args):
        super().__init__(*args)

    def start_game(self):
        global trek_choice
        trek_choice = True


class TrekButton(Button):
    def __init__(self, *args, trek_number):
        super().__init__(*args)
        self.trek_number = trek_number

    def get_trek_number(self):
        return self.trek_number

def make_the_buttons_great_again(running):
    M_Eng.screen.fill((0, 0, 0))
    play_button = PlayButton(100, 100, 50, 50, 'play_button')
    quit_button = Button(100, 200, 50, 50, 'quit_button')
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

import pygame as pg


class Button:

    def __init__(self, x, y, xsize, ysize, text):
        self.x = x
        self.y = y
        self.text = text
        self.xsize = xsize
        self.ysize = ysize

    def is_click(self, event):
        if abs(self.x - event.pos[0]) < self.xsize and abs(self.y - event.pos[1]) < self.ysize:
            return True

    def write_text_on_button(self):
        myfont = pg.font.SysFont("monospace", 10)
        text = myfont.render(str(self.text), 1, (0, 0, 0))
        pg.draw.screen.blit(text, (self.x - self.xsize, self.y - self.ysize))


# start = 0
trek_choice = False
trek_value = 0


class PlayButton(Button):
    def __init__(self, *args):
        super().__init__(*args)

    def start_game(self):
        global trek_choice
        trek_choice = True


class TrekButton(Button):
    def __init__(self, *args, trek_number):
        super().__init__(*args, trek_number)
        self.trek_number = trek_number

    def get_trek_number(self):
        return self.trek_number


class QuitButton(Button):
    def __init__(self, *args):
        super().__init__(*args)

    def quit(self):
        pg.QUIT


class QuitButton(Button):
    def __init__(self, *args):
        super().__init__(*args)

    def quit(self):
        pg.QUIT

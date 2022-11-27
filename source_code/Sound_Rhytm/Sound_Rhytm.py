import time as time
import pygame as pg
from source_code.Engine.menu import start_menu as start_menu
from source_code.Sound_Rhytm import Sound_Rhytm as SR
from source_code.Engine import Mouse_Mode as M_Eng

class NumVariables:
    """Class of numeric variables"""
    def __init__(self, num = 0):
        self._num = num

    def adder(self, arg):
        self._num += arg

    def setter(self, arg):
        self._num = arg

    def timer_setter(self):         # Sets value to current time
        self._num = time.time()

    def getter(self):
        return self._num

class BullVariables:
    """Class of Bullian variables"""
    def __init__(self, init_bul = True):
        self._bul = init_bul

    def setter(self, arg):
        self._bul = arg

    def timer(self, start_time, bpm, fase, lower_bound, upper_bound):            # Returns True or False depending on current time
        if (((time.time() - start_time.getter() + fase) % (bpm) <= upper_bound) or      #0.15
            ((time.time() - start_time.getter() + fase) % (bpm) >= bpm - lower_bound)):
            self._bul = True
        else:
            self._bul = False

    def changer(self):
        if self._bul:
            self._bul = False
        else:
            self._bul = True

    def getter(self):
        return self._bul


start_time = NumVariables()
TimerBull = BullVariables()

def music_player(trek_number, start_time, bpm, fase, lower_bound, upper_bound, draw_balls, balls):
    pg.mixer.init()  # Initializing audio player
    pg.mixer.music.set_volume(0.5)
    if trek_number == 1:
        pg.mixer.music.load("Soundtracks/Phonk/4WHEEL_-_KERAUNOS_KILLER_Speed_Up_73991451.mp3")
        pg.mixer.music.play()
        game_running = True
        while game_running:
            M_Eng.screen.fill((0, 0, 0))
            SR.TimerBull.timer(start_time, bpm, fase, lower_bound, upper_bound)
            M_Eng.Drawer(draw_balls)
            pg.display.update()
            for event in pg.event.get():
                M_Eng.Event_Holder(event, balls, draw_balls, SR.TimerBull)
                if event.type == pg.QUIT:
                    running = False
                    game_running = False





import time as time
import pygame as pg

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

    def timer(self, start_time):            # Returns True or False depending on current time
        if (((time.time() - start_time.getter() + 0.6) % (60/137) <= 0.15) or      #0.15
            ((time.time() - start_time.getter() + 0.6) % (60/137) >= 60/137 - 0.1)):
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

pg.mixer.init()     # Initializing audio player
pg.mixer.music.load("Soundtracks/Phonk/4WHEEL_-_KERAUNOS_KILLER_Speed_Up_73991451.mp3")
pg.mixer.music.set_volume(0.5)

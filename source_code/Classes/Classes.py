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

class Ker_Kill(BullVariables):
    def timer(self, start_time, bpm, fase, lower_bound, upper_bound):
        if (
                ((((time.time() - start_time.getter() + fase) % (bpm) <= upper_bound) or
                ((time.time() - start_time.getter() + fase) % (bpm) >= bpm - lower_bound))) and
                (((((time.time() - start_time.getter() + fase) / (bpm)) % 8 <= 0.5)) or
                ((((time.time() - start_time.getter() + fase) / (bpm)) % 8 >= 8 - 0.5)) or
                (((((time.time() - start_time.getter() + fase) / (bpm)) % 8 <= 2 + 0.5)) and
                ((((time.time() - start_time.getter() + fase) / (bpm)) % 8 >= 2 - 0.5))) or
                (((((time.time() - start_time.getter() + fase) / (bpm)) % 8 <= 4 + 0.5)) and
                ((((time.time() - start_time.getter() + fase) / (bpm)) % 8 >= 4 - 0.5))) or
                (((((time.time() - start_time.getter() + fase) / (bpm)) % 8 <= 6 + 0.5)) and
                ((((time.time() - start_time.getter() + fase) / (bpm)) % 8 >= 6 - 0.5))) or
                (((((time.time() - start_time.getter() + fase) / (bpm)) % 8 <= 1 + 0.5)) and
                ((((time.time() - start_time.getter() + fase) / (bpm)) % 8 >= 1 - 0.5)))
                )
            ):
            self._bul = True
        else:
            self._bul = False


start_time = NumVariables()
TimerBull = BullVariables()
Ker_Kill_Timer = Ker_Kill()
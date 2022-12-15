import time as time
import pygame as pg
from source_code.Engine.menu import start_menu as start_menu
from source_code.Sound_Rhytm import Sound_Rhytm_Mouse as SR
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

class Mouse_Mode_Track_1:
    """Class of functions, which executes mouse mode gameplay for different tracks, corresponding to track number"""
    def __init__(self, track_name):
        """Defines the name of the track which will be played"""
        self.track_name = track_name

    def number_checker(self, trek_number):
        """
        Activates music_player function only for corresponding track number
        :param trek_number: track number
        :return: True, if the number fits the track
        """
        if trek_number == 1:
            return True

    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, draw_balls, balls, running, trek_number):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                M_Eng.screen.fill((0, 0, 0))
                SR.TimerBull.timer(start_time, bpm, fase, lower_bound, upper_bound)
                M_Eng.Drawer(draw_balls)
                pg.display.update()
                #M_Eng.Event_Holder("q", balls, draw_balls, SR.TimerBull)        # Commented stuff is here for testing
                for event in pg.event.get():
                    M_Eng.Event_Holder(event, balls, draw_balls, SR.TimerBull)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class Mouse_Mode_Track_2(Mouse_Mode_Track_1):
    def number_checker(self, trek_number):
        if trek_number == 2:
            return True


start_time = NumVariables()
TimerBull = BullVariables()

Trak_1_Player = Mouse_Mode_Track_1("../../../../Soundtracks/Phonk/4WHEEL_-_KERAUNOS_KILLER_Speed_Up_73991451.mp3")
Track_2_Player = Mouse_Mode_Track_2("../../../../Soundtracks/Phonk/KORDHELL_-_Live_Another_Day_73349846.mp3")

import time as time
import pygame as pg
from source_code.Engine.menu import Menu as start_menu
from source_code.Classes import Classes as CL
from source_code.Sound_Rhytm import Sound_Rhytm_Mouse as SR
from source_code.Engine import Mouse_Mode as M_Eng
from source_code.Visualisation.Game import Vis_score as VSS


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
                CL.TimerBull.timer(start_time, bpm, fase, lower_bound, upper_bound)
                M_Eng.Drawer(draw_balls)
                drawable_counter.draw_counter(M_Eng.counter.getter())
                pg.display.update()
                #M_Eng.Event_Holder("q", balls, draw_balls, SR.TimerBull)        # Commented stuff is here for testing
                for event in pg.event.get():
                    M_Eng.Event_Holder(event, balls, draw_balls, CL.TimerBull)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class Mouse_Mode_Track_2(Mouse_Mode_Track_1):
    def number_checker(self, trek_number):
        if trek_number == 2:
            return True


class Mouse_Mode_Track_3(Mouse_Mode_Track_1):
    def number_checker(self, trek_number):
        if trek_number == 3:
            return True


class Mouse_Mode_Track_4(Mouse_Mode_Track_1):
    def number_checker(self, trek_number):
        if trek_number == 4:
            return True


class Mouse_Mode_Track_5(Mouse_Mode_Track_1):
    def number_checker(self, trek_number):
        if trek_number == 5:
            return True


class Ker_Kill_Player(Mouse_Mode_Track_1):
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
                CL.Ker_Kill_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                M_Eng.Drawer(draw_balls)
                drawable_counter.draw_counter(M_Eng.counter.getter())
                pg.display.update()
                if CL.timer.time_getter(start_time) >= 79:
                    game_running = False
                for event in pg.event.get():
                    M_Eng.Event_Holder(event, balls, draw_balls, CL.Ker_Kill_Timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class Live_Another_Day_Player(Mouse_Mode_Track_2):
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
                CL.Live_An_Day_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                drawable_counter.draw_counter(M_Eng.counter.getter())
                M_Eng.Drawer(draw_balls)
                drawable_counter.draw_counter(M_Eng.counter.getter())
                pg.display.update()
                if CL.timer.time_getter(start_time) >= 134:
                    game_running = False
                for event in pg.event.get():
                    M_Eng.Event_Holder(event, balls, draw_balls, CL.Live_An_Day_Timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class Phonk_Town_Player(Mouse_Mode_Track_3):
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
                CL.Phonky_Town_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                drawable_counter.draw_counter(M_Eng.counter.getter())
                M_Eng.Drawer(draw_balls)
                drawable_counter.draw_counter(M_Eng.counter.getter())
                pg.display.update()
                if CL.timer.time_getter(start_time) >= 143:
                    game_running = False
                for event in pg.event.get():
                    M_Eng.Event_Holder(event, balls, draw_balls, CL.Phonky_Town_Timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False ##


class Why_Not_Player(Mouse_Mode_Track_4):
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
                CL.Why_Not_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                M_Eng.Drawer(draw_balls)
                drawable_counter.draw_counter(M_Eng.counter.getter())
                pg.display.update()
                if CL.timer.time_getter(start_time) >= 165:
                    game_running = False
                for event in pg.event.get():
                    M_Eng.Event_Holder(event, balls, draw_balls, CL.Why_Not_Timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class DeltaAlphaPlayer(Mouse_Mode_Track_5):
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
                CL.Delta_Alpha_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                M_Eng.Drawer(draw_balls)
                drawable_counter.draw_counter(M_Eng.counter.getter())
                pg.display.update()
                if CL.timer.time_getter(start_time) >= 31.5:
                    game_running = False
                for event in pg.event.get():
                    M_Eng.Event_Holder(event, balls, draw_balls, CL.Delta_Alpha_Timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False



drawable_counter = VSS.DrawCounter(M_Eng.screen)

Track_1_Player = Ker_Kill_Player("Soundtracks/Phonk/4WHEEL_-_KERAUNOS_KILLER_Speed_Up_73991451.mp3")
Track_2_Player = Live_Another_Day_Player("Soundtracks/Phonk/KORDHELL_-_Live_Another_Day_73349846.mp3")
Track_3_Player = Phonk_Town_Player("Soundtracks/Phonk/PlayaPhonk_-_Phonky_Town_72969550.mp3")
Track_4_Player = Why_Not_Player("Soundtracks/Phonk/GHOSTFACE_PLAYA_-_Why_Not_74017956.mp3")
Track_5_Player = Mouse_Mode_Track_5("Soundtracks/DeltaAlpha/Delta_Alpha.mp3")





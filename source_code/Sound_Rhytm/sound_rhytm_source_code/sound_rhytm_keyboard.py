import pygame as pg
from source_code.Classes import classes as cl
from source_code.Engine import keyboard_mode as k_eng
from source_code.Visualisation.Game import vis_score as vss


class KeyboardModeTrack1:
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
        if trek_number == 6:
            return True

    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, arrow_list, running, trek_number, time_list, final_running):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                k_eng.screen.fill((0, 0, 0))
                cl.TimerBull.timer(start_time, bpm, fase, lower_bound, upper_bound)
                drawable_counter.draw_counter(k_eng.counter.getter())
                k_eng.Targ_Drawer(k_eng.Target_List)
                k_eng.Arr_Drawer(arrow_list)
                k_eng.arrow_mover(arrow_list, cl.timer)
                pg.display.update()
                # M_Eng.Event_Holder("q", balls, draw_balls, SR.TimerBull)        # Commented stuff is here for testing
                for event in pg.event.get():
                    k_eng.Event_Holder(event, arrow_list, k_eng.bit_checker, time_list, fase, cl.timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class KeyboardModeTrack2(KeyboardModeTrack1):
    def number_checker(self, trek_number):
        if trek_number == 7:
            return True


class KeyboardModeTrack3(KeyboardModeTrack1):
    def number_checker(self, trek_number):
        if trek_number == 8:
            return True


class KeyboardModeTrack4(KeyboardModeTrack1):
    def number_checker(self, trek_number):
        if trek_number == 9:
            return True


class KeyboardModeTrack5(KeyboardModeTrack1):
    def number_checker(self, trek_number):
        if trek_number == 10:
            return True


class KerKillPlayer(KeyboardModeTrack1):
    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, arrow_list, running, trek_number, time_list, final_running):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                k_eng.screen.fill((0, 0, 0))
                cl.Ker_Kill_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                drawable_counter.draw_counter(k_eng.counter.getter())
                k_eng.Targ_Drawer(k_eng.Target_List)
                k_eng.Arr_Drawer(arrow_list)
                k_eng.arrow_mover(arrow_list, cl.timer)
                pg.display.update()
                if cl.timer.time_getter(start_time) >= 79:
                    game_running = False
                    final_running.setter(True)
                for event in pg.event.get():
                    k_eng.Event_Holder(event, arrow_list, k_eng.bit_checker, time_list, fase, cl.timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class LiveAnotherDayPlayer(KeyboardModeTrack2):
    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, arrow_list, running, trek_number, time_list, final_running):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                k_eng.screen.fill((0, 0, 0))
                cl.Live_An_Day_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                drawable_counter.draw_counter(k_eng.counter.getter())
                k_eng.Targ_Drawer(k_eng.Target_List)
                k_eng.Arr_Drawer(arrow_list)
                k_eng.arrow_mover(arrow_list, cl.timer)
                pg.display.update()
                if cl.timer.time_getter(start_time) >= 134:
                    game_running = False
                    final_running.setter(True)
                for event in pg.event.get():
                    k_eng.Event_Holder(event, arrow_list, k_eng.bit_checker, time_list, fase, cl.timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class PhonkTownPlayer(KeyboardModeTrack3):
    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, arrow_list, running, trek_number, time_list, final_running):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                k_eng.screen.fill((0, 0, 0))
                cl.Phonky_Town_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                drawable_counter.draw_counter(k_eng.counter.getter())
                k_eng.Targ_Drawer(k_eng.Target_List)
                k_eng.Arr_Drawer(arrow_list)
                k_eng.arrow_mover(arrow_list, cl.timer)
                pg.display.update()
                if cl.timer.time_getter(start_time) >= 143:
                    game_running = False
                    final_running.setter(True)
                for event in pg.event.get():
                    k_eng.Event_Holder(event, arrow_list, k_eng.bit_checker, time_list, fase, cl.timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class WhyNotPlayer(KeyboardModeTrack4):
    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, arrow_list, running, trek_number, time_list, final_running):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                k_eng.screen.fill((0, 0, 0))
                cl.Why_Not_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                drawable_counter.draw_counter(k_eng.counter.getter())
                k_eng.Targ_Drawer(k_eng.Target_List)
                k_eng.Arr_Drawer(arrow_list)
                k_eng.arrow_mover(arrow_list, cl.timer)
                pg.display.update()
                if cl.timer.time_getter(start_time) >= 165:
                    game_running = False
                    final_running.setter(True)
                for event in pg.event.get():
                    k_eng.Event_Holder(event, arrow_list, k_eng.bit_checker, time_list, fase, cl.timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class DeltaAlphaPlayer(KeyboardModeTrack5):
    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, arrow_list, running, trek_number,
                     time_list, final_running):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                k_eng.screen.fill((0, 0, 0))
                cl.Why_Not_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                drawable_counter.draw_counter(k_eng.counter.getter())
                k_eng.Targ_Drawer(k_eng.Target_List)
                k_eng.Arr_Drawer(arrow_list)
                k_eng.arrow_mover(arrow_list, cl.timer)
                pg.display.update()
                if cl.timer.time_getter(start_time) >= 31.5:
                    game_running = False
                    final_running.setter(True)
                for event in pg.event.get():
                    k_eng.Event_Holder(event, arrow_list, k_eng.bit_checker, time_list, fase, cl.timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


drawable_counter = vss.DrawCounter(k_eng.screen)

Track_6_Player = KerKillPlayer("Soundtracks/Phonk/4WHEEL_-_KERAUNOS_KILLER_Speed_Up_73991451.mp3")
Track_7_Player = LiveAnotherDayPlayer("Soundtracks/Phonk/KORDHELL_-_Live_Another_Day_73349846.mp3")
Track_8_Player = PhonkTownPlayer("Soundtracks/Phonk/PlayaPhonk_-_Phonky_Town_72969550.mp3")
Track_9_Player = WhyNotPlayer("Soundtracks/Phonk/GHOSTFACE_PLAYA_-_Why_Not_74017956.mp3")
Track_10_Player = DeltaAlphaPlayer("Soundtracks/DeltaAlpha/Delta_Alpha.mp3")

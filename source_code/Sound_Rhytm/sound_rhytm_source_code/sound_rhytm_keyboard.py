import pygame as pg
from source_code.Classes import classes as CL
from source_code.Engine import keyboard_mode as K_Eng
from source_code.Visualisation.Game import vis_score as VSS


class Keyboard_Mode_Track_1:
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

    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, arrow_list, running, trek_number, time_list):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                K_Eng.screen.fill((0, 0, 0))
                CL.TimerBull.timer(start_time, bpm, fase, lower_bound, upper_bound)
                drawable_counter.draw_counter(CL.counter.getter())
                K_Eng.Targ_Drawer(K_Eng.Target_List)
                K_Eng.Arr_Drawer(arrow_list)
                K_Eng.arrow_mover(arrow_list, CL.timer)
                pg.display.update()
                #M_Eng.Event_Holder("q", balls, draw_balls, SR.TimerBull)        # Commented stuff is here for testing
                for event in pg.event.get():
                    K_Eng.Event_Holder(event, arrow_list, K_Eng.bit_checker, time_list, fase, CL.timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class Keyboard_Mode_Track_2(Keyboard_Mode_Track_1):
    def number_checker(self, trek_number):
        if trek_number == 7:
            return True


class Keyboard_Mode_Track_3(Keyboard_Mode_Track_1):
    def number_checker(self, trek_number):
        if trek_number == 8:
            return True


class Keyboard_Mode_Track_4(Keyboard_Mode_Track_1):
    def number_checker(self, trek_number):
        if trek_number == 9:
            return True


class Keyboard_Mode_Track_5(Keyboard_Mode_Track_1):
    def number_checker(self, trek_number):
        if trek_number == 10:
            return True


class Ker_Kill_Player(Keyboard_Mode_Track_1):
    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, arrow_list, running, trek_number, time_list, final_running):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                K_Eng.screen.fill((0, 0, 0))
                CL.Ker_Kill_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                drawable_counter.draw_counter(CL.counter.getter())
                K_Eng.Targ_Drawer(K_Eng.Target_List)
                K_Eng.Arr_Drawer(arrow_list)
                K_Eng.arrow_mover(arrow_list, CL.timer)
                drawable_counter.draw_counter(CL.counter.getter())
                pg.display.update()
                if CL.timer.time_getter(start_time) >= 79:
                    game_running = False
                    final_running.setter(True)
                for event in pg.event.get():
                    K_Eng.Event_Holder(event, arrow_list, K_Eng.bit_checker, time_list, fase, CL.timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class Live_Another_Day_Player(Keyboard_Mode_Track_2):
    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, arrow_list, running, trek_number, time_list, final_running):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                K_Eng.screen.fill((0, 0, 0))
                CL.Live_An_Day_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                drawable_counter.draw_counter(CL.counter.getter())
                K_Eng.Targ_Drawer(K_Eng.Target_List)
                K_Eng.Arr_Drawer(arrow_list)
                K_Eng.arrow_mover(arrow_list, CL.timer)
                drawable_counter.draw_counter(CL.counter.getter())
                pg.display.update()
                if CL.timer.time_getter(start_time) >= 134:
                    game_running = False
                    final_running.setter(True)
                for event in pg.event.get():
                    K_Eng.Event_Holder(event, arrow_list, K_Eng.bit_checker, time_list, fase, CL.timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class Phonk_Town_Player(Keyboard_Mode_Track_3):
    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, arrow_list, running, trek_number, time_list, final_running):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                K_Eng.screen.fill((0, 0, 0))
                CL.Phonky_Town_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                drawable_counter.draw_counter(CL.counter.getter())
                K_Eng.Targ_Drawer(K_Eng.Target_List)
                K_Eng.Arr_Drawer(arrow_list)
                K_Eng.arrow_mover(arrow_list, CL.timer)
                drawable_counter.draw_counter(CL.counter.getter())
                pg.display.update()
                if CL.timer.time_getter(start_time) >= 143:
                    game_running = False
                    final_running.setter(True)
                for event in pg.event.get():
                    K_Eng.Event_Holder(event, arrow_list, K_Eng.bit_checker, time_list, fase, CL.timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class Why_Not_Player(Keyboard_Mode_Track_4):
    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, arrow_list, running, trek_number, time_list, final_running):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                K_Eng.screen.fill((0, 0, 0))
                CL.Why_Not_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                K_Eng.Targ_Drawer(K_Eng.Target_List)
                K_Eng.Arr_Drawer(arrow_list)
                K_Eng.arrow_mover(arrow_list, CL.timer)
                drawable_counter.draw_counter(CL.counter.getter())
                pg.display.update()
                if CL.timer.time_getter(start_time) >= 165:
                    game_running = False
                    final_running.setter(True)
                for event in pg.event.get():
                    K_Eng.Event_Holder(event, arrow_list, K_Eng.bit_checker, time_list, fase, CL.timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class DeltaAlphaPlayer(Keyboard_Mode_Track_5):
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
                K_Eng.screen.fill((0, 0, 0))
                CL.Why_Not_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                drawable_counter.draw_counter(CL.counter.getter())
                K_Eng.Targ_Drawer(K_Eng.Target_List)
                K_Eng.Arr_Drawer(arrow_list)
                K_Eng.arrow_mover(arrow_list, CL.timer)
                drawable_counter.draw_counter(CL.counter.getter())
                pg.display.update()
                if CL.timer.time_getter(start_time) >= 31.5:
                    game_running = False
                    final_running.setter(True)
                for event in pg.event.get():
                    K_Eng.Event_Holder(event, arrow_list, K_Eng.bit_checker, time_list, fase, CL.timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False

drawable_counter = VSS.DrawCounter(K_Eng.screen)

Track_6_Player = Ker_Kill_Player("Soundtracks/Phonk/4WHEEL_-_KERAUNOS_KILLER_Speed_Up_73991451.mp3")
Track_7_Player = Live_Another_Day_Player("Soundtracks/Phonk/KORDHELL_-_Live_Another_Day_73349846.mp3")
Track_8_Player = Phonk_Town_Player("Soundtracks/Phonk/PlayaPhonk_-_Phonky_Town_72969550.mp3")
Track_9_Player = Why_Not_Player("Soundtracks/Phonk/GHOSTFACE_PLAYA_-_Why_Not_74017956.mp3")
Track_10_Player = DeltaAlphaPlayer("Soundtracks/DeltaAlpha/Delta_Alpha.mp3")
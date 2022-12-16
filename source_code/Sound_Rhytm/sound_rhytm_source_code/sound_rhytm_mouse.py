import pygame as pg
from source_code.Classes import classes as cl
from source_code.Engine import mouse_mode as m_eng
from source_code.Visualisation.Game import vis_score as vss


class MouseModeTrack1:
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

    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, draw_balls, balls, running, trek_number, final_running):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                m_eng.screen.fill((0, 0, 0))
                cl.TimerBull.timer(start_time, bpm, fase, lower_bound, upper_bound)
                m_eng.Drawer(draw_balls)
                drawable_counter.draw_counter(m_eng.counter.getter())
                pg.display.update()
                # m_eng.Event_Holder("q", balls, draw_balls, SR.TimerBull)        # Commented stuff is here for testing
                for event in pg.event.get():
                    m_eng.Event_Holder(event, balls, draw_balls, cl.TimerBull)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class MouseModeTrack2(MouseModeTrack1):
    def number_checker(self, trek_number):
        if trek_number == 2:
            return True


class MouseModeTrack3(MouseModeTrack1):
    def number_checker(self, trek_number):
        if trek_number == 3:
            return True


class MouseModeTrack4(MouseModeTrack1):
    def number_checker(self, trek_number):
        if trek_number == 4:
            return True


class MouseModeTrack5(MouseModeTrack1):
    def number_checker(self, trek_number):
        if trek_number == 5:
            return True


class KerKillPlayer(MouseModeTrack1):
    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, draw_balls, balls, running, trek_number, final_running):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                m_eng.screen.fill((0, 0, 0))
                cl.Ker_Kill_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                m_eng.Drawer(draw_balls)
                drawable_counter.draw_counter(m_eng.counter.getter())
                pg.display.update()
                if cl.timer.time_getter(start_time) >= 79:
                    game_running = False
                    final_running.setter(True)
                for event in pg.event.get():
                    m_eng.Event_Holder(event, balls, draw_balls, cl.Ker_Kill_Timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class LiveAnotherDayPlayer(MouseModeTrack2):
    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, draw_balls, balls, running, trek_number, final_running):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                m_eng.screen.fill((0, 0, 0))
                cl.Live_An_Day_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                drawable_counter.draw_counter(m_eng.counter.getter())
                m_eng.Drawer(draw_balls)
                drawable_counter.draw_counter(m_eng.counter.getter())
                pg.display.update()
                if cl.timer.time_getter(start_time) >= 134:
                    game_running = False
                    final_running.setter(True)
                for event in pg.event.get():
                    m_eng.Event_Holder(event, balls, draw_balls, cl.Live_An_Day_Timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class PhonkTownPlayer(MouseModeTrack3):
    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, draw_balls, balls, running, trek_number, final_running):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                m_eng.screen.fill((0, 0, 0))
                cl.Phonky_Town_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                drawable_counter.draw_counter(m_eng.counter.getter())
                m_eng.Drawer(draw_balls)
                drawable_counter.draw_counter(m_eng.counter.getter())
                pg.display.update()
                if cl.timer.time_getter(start_time) >= 143:
                    game_running = False
                    final_running.setter(True)
                for event in pg.event.get():
                    m_eng.Event_Holder(event, balls, draw_balls, cl.Phonky_Town_Timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class WhyNotPlayer(MouseModeTrack4):
    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, draw_balls, balls, running, trek_number, final_running):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                m_eng.screen.fill((0, 0, 0))
                cl.Why_Not_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                m_eng.Drawer(draw_balls)
                drawable_counter.draw_counter(m_eng.counter.getter())
                pg.display.update()
                if cl.timer.time_getter(start_time) >= 165:
                    game_running = False
                    final_running.setter(True)
                for event in pg.event.get():
                    m_eng.Event_Holder(event, balls, draw_balls, cl.Why_Not_Timer)
                    if event.type == pg.QUIT:
                        running.setter(False)
                        game_running = False


class DeltaAlphaPlayer(MouseModeTrack5):
    def music_player(self, start_time, bpm, fase, lower_bound, upper_bound, draw_balls, balls, running, trek_number, final_running):
        """Mother of all the music players. Plays music with certain name and does bit check with certain bpm"""
        pg.mixer.init()  # Initializing audio player
        pg.mixer.music.set_volume(0.5)
        if self.number_checker(trek_number):
            pg.mixer.music.load(self.track_name)
            pg.mixer.music.play()
            game_running = True
            while game_running:
                m_eng.screen.fill((0, 0, 0))
                cl.Delta_Alpha_Timer.timer(start_time, bpm, fase, lower_bound, upper_bound)
                m_eng.Drawer(draw_balls)
                drawable_counter.draw_counter(m_eng.counter.getter())
                pg.display.update()
                if cl.timer.time_getter(start_time) >= 0:  # 31.5:
                    game_running = False
                    final_running.setter(True)
                for event in pg.event.get():
                    m_eng.Event_Holder(event, balls, draw_balls, cl.Delta_Alpha_Timer)
                    if event.type == pg.QUIT:  # Cl.timer.time_getter(start_time) >= 0:
                        running.setter(False)
                        game_running = False


drawable_counter = vss.DrawCounter(m_eng.screen)    #

Track_1_Player = KerKillPlayer("Soundtracks/Phonk/4WHEEL_-_KERAUNOS_KILLER_Speed_Up_73991451.mp3")
Track_2_Player = LiveAnotherDayPlayer("Soundtracks/Phonk/KORDHELL_-_Live_Another_Day_73349846.mp3")
Track_3_Player = PhonkTownPlayer("Soundtracks/Phonk/PlayaPhonk_-_Phonky_Town_72969550.mp3")
Track_4_Player = WhyNotPlayer("Soundtracks/Phonk/GHOSTFACE_PLAYA_-_Why_Not_74017956.mp3")
Track_5_Player = DeltaAlphaPlayer("Soundtracks/DeltaAlpha/Delta_Alpha.mp3")

import time as time
import pygame as pg


class NumVariables:
    """Class of numeric variables"""

    def __init__(self, num=0):
        self._num = num

    def adder(self, arg):
        self._num += arg

    def setter(self, arg):
        self._num = arg

    def timer_setter(self):  # Sets value to current time
        self._num = time.time()

    def getter(self):
        return self._num


class BullVariables:
    """Class of Bullian variables"""

    def __init__(self, init_bul=True):
        self._bul = init_bul

    def setter(self, arg):
        self._bul = arg

    def timer(self, start_time, bpm, fase, lower_bound, upper_bound):  # Returns True or False depending on current time
        if (((time.time() - start_time.getter() + fase) % (bpm) <= upper_bound) or  # 0.15
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

    def time_getter(self, start_time):
        return time.time() - start_time.getter()


class ListVariables():
    """Class of list variables, used in this program"""

    def __init__(self):
        self.list = []

    def setter(self, arg):
        self.list = arg

    def getter(self):
        return self.list


class Ker_Kill(BullVariables):
    def timer(self, start_time, bpm, fase, lower_bound, upper_bound):
        if (
                ((((time.time() - start_time.getter() + fase) % (bpm) <= upper_bound) or
                  ((time.time() - start_time.getter() + fase) % (bpm) >= bpm - lower_bound)))

                and

                (((((time.time() - start_time.getter() + fase) / (bpm)) % 8 <= 0.5)) or
                 ((((time.time() - start_time.getter() + fase) / (bpm)) % 8 >= 8 - 0.5))

                 or
                 (((((time.time() - start_time.getter() + fase) / (bpm)) % 8 <= 2 + 0.5)) and
                  ((((time.time() - start_time.getter() + fase) / (bpm)) % 8 >= 2 - 0.5)))

                 or
                 (((((time.time() - start_time.getter() + fase) / (bpm)) % 8 <= 4 + 0.5)) and
                  ((((time.time() - start_time.getter() + fase) / (bpm)) % 8 >= 4 - 0.5)))

                 or
                 (((((time.time() - start_time.getter() + fase) / (bpm)) % 8 <= 6 + 0.5)) and
                  ((((time.time() - start_time.getter() + fase) / (bpm)) % 8 >= 6 - 0.5)))

                 or
                 (((((time.time() - start_time.getter() + fase) / (bpm)) % 8 <= 1 + 0.5)) and
                  ((((time.time() - start_time.getter() + fase) / (bpm)) % 8 >= 1 - 0.5)))
                )
        ):
            self._bul = True
        else:
            self._bul = False


class Live_An_Day(BullVariables):
    def timer(self, start_time, bpm, fase, lower_bound, upper_bound):
        if (not
        ((((time.time() - start_time.getter() + fase) <= 16.5) and
          ((time.time() - start_time.getter() + fase) >= 14.5)) or

         (((time.time() - start_time.getter() + fase) <= 49.6) and
          ((time.time() - start_time.getter() + fase) >= 47.7)) or

         (((time.time() - start_time.getter() + fase) <= 66.5) and
          ((time.time() - start_time.getter() + fase) >= 64.5)) or

         (((time.time() - start_time.getter() + fase) <= 99.75) and
          ((time.time() - start_time.getter() + fase) >= 97.75)) or

         (((time.time() - start_time.getter() + fase) <= 116.5) and
          ((time.time() - start_time.getter() + fase) >= 114.5))
        )

                and
                (((time.time() - start_time.getter() + fase) % (bpm) <= upper_bound) or
                 ((time.time() - start_time.getter() + fase) % (bpm) >= bpm - lower_bound)

                 or

                 ((((time.time() - start_time.getter() + fase) <= 97)
                   and
                   ((time.time() - start_time.getter() + fase) >= 22))

                  and
                  ((((time.time() - start_time.getter() + fase) <= 25))
                   or
                   ((((time.time() - start_time.getter() + fase) >= 32)) and
                    ((time.time() - start_time.getter() + fase) <= 46))
                   or
                   ((((time.time() - start_time.getter() + fase) >= 72)) and
                    ((time.time() - start_time.getter() + fase) <= 76))
                   or
                   ((((time.time() - start_time.getter() + fase) >= 80)) and
                    ((time.time() - start_time.getter() + fase) <= 98))
                  )

                  and
                  (((((time.time() - start_time.getter() + fase) / (bpm)) % 8 <= 7.5 + 0.12)) and
                   ((((time.time() - start_time.getter() + fase) / (bpm)) % 8 >= 7.5 - 0.07)))))
        ):
            self._bul = True
        else:
            self._bul = False


class Phonk_Town(BullVariables):
    def timer(self, start_time, bpm, fase, lower_bound, upper_bound):
        if (not (((time.time() - start_time.getter() + fase) <= 15.7 and
                  (time.time() - start_time.getter() + fase) >= 13.5)
                 or
                 ((time.time() - start_time.getter() + fase) <= 46.5 and
                  (time.time() - start_time.getter() + fase) >= 44.25)
                 or
                 ((time.time() - start_time.getter() + fase) <= 92.5 and
                  (time.time() - start_time.getter() + fase) >= 91.25)
        )
                and
                (time.time() - start_time.getter() + fase) <= 136.5

                and

                (((((time.time() - start_time.getter() + fase) % (bpm) <= upper_bound) or
                   ((time.time() - start_time.getter() + fase) % (bpm) >= bpm - lower_bound)))

                 or

                 ((((((time.time() - start_time.getter() + fase) / (bpm)) % 16 <= 0.5 + upper_bound)) and
                   ((((time.time() - start_time.getter() + fase) / (bpm)) % 16 >= 0.5 - lower_bound))))
                 and not False

                )
        ):
            self._bul = True
        elif (
                ((time.time() - start_time.getter() + fase) <= 46.5 and
                 (time.time() - start_time.getter() + fase) >= 44.25)

                and
                ((((((time.time() - start_time.getter() + fase) / (bpm)) % 16 <= 14 + upper_bound)) and
                  ((((time.time() - start_time.getter() + fase) / (bpm)) % 16 >= 14 - lower_bound)))
                 or
                 (((((time.time() - start_time.getter() + fase) / (bpm)) % 16 <= 0 + upper_bound)) or
                  ((((time.time() - start_time.getter() + fase) / (bpm)) % 16 >= 16 - lower_bound)))
                )
        ):
            self._bul = True
        else:
            self._bul = False


class Why_Not(BullVariables):
    def timer(self, start_time, bpm, fase, lower_bound, upper_bound):
        if (
                (time.time() - start_time.getter() + fase) >= 37
                and
                (((time.time() - start_time.getter() + fase) % (bpm) <= upper_bound) or
                 ((time.time() - start_time.getter() + fase) % (bpm) >= bpm - lower_bound))
        ):
            self._bul = True
        elif (((time.time() - start_time.getter() + fase) / (bpm) - 2) // 8 % 2 == 0

              and
              (time.time() - start_time.getter() + fase) >= 4.75
              and
              ((time.time() - start_time.getter() + fase) <= 36.2
               and
               (((time.time() - start_time.getter() + fase) / (bpm) % 8 <= 3.5 + upper_bound) and
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 >= 3.5 - lower_bound)
                or
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 <= 2 + upper_bound) and
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 >= 2 - lower_bound)
                or
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 <= 5 + upper_bound) and
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 >= 5 - lower_bound)
                or
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 <= 7 + upper_bound) and
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 >= 7 - lower_bound)
                or
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 <= 1 + upper_bound) and
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 >= 1 - lower_bound)
                or
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 <= 0 + upper_bound) or
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 >= 8 - lower_bound)
                or
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 <= 0.5 + 0.12) and
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 >= 0.5 - 0.07)))
        ):
            self._bul = True
        elif (((time.time() - start_time.getter() + fase) / (bpm) - 2) // 8 % 2 == 1

              and
              (time.time() - start_time.getter() + fase) >= 4.75
              and
              ((time.time() - start_time.getter() + fase) <= 36.2
               and
               (((time.time() - start_time.getter() + fase) / (bpm) % 8 <= 3.5 + upper_bound) and
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 >= 3.5 - lower_bound)
                or
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 <= 2 + upper_bound) and
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 >= 2 - lower_bound)
                or
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 <= 5 + upper_bound) and
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 >= 5 - lower_bound)
                or
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 <= 7 + upper_bound) and
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 >= 7 - lower_bound)
                or
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 <= 0.75 + upper_bound) and
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 >= 0.75 - lower_bound)
                or
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 <= 1.25 + upper_bound) and
                ((time.time() - start_time.getter() + fase) / (bpm) % 8 >= 1.25 - lower_bound)))

        ):
            self._bul = True
        else:
            self._bul = False


class DeltaAlpha(BullVariables):
    def timer(self, start_time, bpm, fase, lower_bound, upper_bound):
        if ((((time.time() - start_time.getter() + fase) % (bpm) <= upper_bound) or
             ((time.time() - start_time.getter() + fase) % (bpm) >= bpm - lower_bound)) and
                (time.time() - start_time.getter() + fase >= 1 and time.time() - start_time.getter() + fase <= 31.45)):
            self._bul = True
        else:
            self._bul = False


class Button:

    def __init__(self, x, y, xsize, ysize, text):
        """ constructor of class "Button" """
        self.x = x
        self.y = y
        self.text = text
        self.xsize = xsize
        self.ysize = ysize

    def is_click(self, event):
        """ return True if you click on the Button """
        if self.x < event.pos[0] < self.x + self.xsize and self.y < event.pos[1] < self.y + self.ysize:
            return True

    def write_text_on_button(self, screen):
        """ writing text on the element of class "Button" """
        myfont = pg.font.SysFont("monospace", 30)
        text = myfont.render(str(self.text), 1, (255, 255, 255))
        screen.blit(text, (self.x, self.y))


class PlayButton(Button):
    def __init__(self, *args):
        """ constructor of class "PlayButton" which the subclass of class "Button" """
        super().__init__(*args)

    def start_game(self, mode):
        """ Using for run game if player click on the element of PlayButton """
        trek_choice.setter(mode)


class TrekButton(Button):
    def __init__(self, *args):
        """ constructor of class "TrekButton" which the subclass of class "Button" """
        super().__init__(*args)

    def get_trek_number(self):
        """ Return number of trek for which the element of TrekButton is responsible"""
        return self.trek_number


counter = NumVariables()
timer = BullVariables()
start_time = NumVariables()
TimerBull = BullVariables()
Ker_Kill_Timer = Ker_Kill()
Live_An_Day_Timer = Live_An_Day()
Phonky_Town_Timer = Phonk_Town()
Why_Not_Timer = Why_Not()
Delta_Alpha_Timer = DeltaAlpha()

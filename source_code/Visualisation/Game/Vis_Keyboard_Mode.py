import pygame as pg

red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
orange = (255, 180, 0)
dark_grey = (50, 50, 50)
light_grey = (90, 90, 90)


class DrawableArrow:
    """
    draws an arrow in direct place
    """
    def __init__(self, surface, x, y, scale, condition='normal'):
        """

        :param surface: surface, where arrow must be drawn
        :param x: x position of arrow's center
        :param y: y position of arrow's center
        :param scale: scale of an arrow
        :param condition: condition of an arrow: 'ok', if you hit the bit, 'bad', if you missed the bit,
        'normal', if the arrow is only going to be hit, 'target', if it is used like a target
        """
        self.surface = surface
        self.x = x
        self.y = y
        self.scale = scale
        self.condition = condition
        self.is_target = False
        self.direction = None

    def set_condition(self, condition):
        self.condition = condition

    def direction_getter(self):
        return self.direction

    def x_changer(self, deltax = 0):
        """

        :param deltax: change of coordinate
        :return: self.x += deltax
        """
        self.x = self.x + deltax


class DrawableArrowUp(DrawableArrow):
    def __init__(self, *args):
        """ constructor of class "DrawableArrowUp" which the subclass of class "DrawableArrow" """
        super().__init__(*args)
        self.direction = 'Up'

    def draw_up_arrow(self):
        color_arrow_width = None
        color_arrow_fill = None
        color_bar = None
        if self.condition == 'normal' and not self.is_target:
            color_arrow_width = white
            color_arrow_fill = light_grey
            color_bar = yellow
        elif self.condition == 'ok' and not self.is_target:
            color_arrow_width = white
            color_arrow_fill = green
            color_bar = green
        elif self.condition == 'bad' and not self.is_target:
            color_arrow_width = white
            color_arrow_fill = red
            color_bar = red
        pg.draw.rect(self.surface, color_arrow_fill, (self.x - 2.5 * self.scale, self.y,
                                                 5 * self.scale, 8 * self.scale)) # fill rect
        pg.draw.rect(self.surface, color_arrow_width, (self.x-2.5*self.scale, self.y,
                                                 5*self.scale,          8*self.scale), self.scale//3)# white around rect
        pg.draw.polygon(self.surface, color_arrow_fill, ((self.x - 6 * self.scale, self.y),
                                                    (self.x, self.y - 8 * self.scale),
                                                    (self.x + 6 * self.scale, self.y))) # fill triangle
        pg.draw.polygon(self.surface, color_arrow_width, ((self.x-6*self.scale, self.y),
                                                    (self.x, self.y-8*self.scale),
                                                    (self.x+6*self.scale, self.y)), self.scale//3)  # white arround triangle

        pg.draw.rect(self.surface, color_arrow_fill, (self.x - 2.2*self.scale, self.y - self.scale,
                                                   4.4 * self.scale,        5*self.scale))  # colors white bar in fill color
        pg.draw.rect(self.surface, color_bar, (self.x-0.23*self.scale, self.y-(44/6)*self.scale,
                                               0.6*self.scale,        (15.2)*self.scale))  # yellow bar


class DrawableArrowDown(DrawableArrow):
    def __init__(self, *args):
        """ constructor of class "DrawableArrowDown" which the subclass of class "DrawableArrow" """
        super().__init__(*args)
        self.direction = 'Down'

    def draw_down_arrow(self):
        color_arrow_width = None
        color_arrow_fill = None
        color_bar = None
        if self.condition == 'normal' and not self.is_target:
            color_arrow_width = white
            color_arrow_fill = light_grey
            color_bar = yellow
        elif self.condition == 'ok' and not self.is_target:
            color_arrow_width = white
            color_arrow_fill = green
            color_bar = green
        elif self.condition == 'bad' and not self.is_target:
            color_arrow_width = white
            color_arrow_fill = red
            color_bar = red
        pg.draw.rect(self.surface, color_arrow_fill, (self.x - 2.5 * self.scale, self.y - 8 * self.scale,
                                                      5 * self.scale, 8 * self.scale))
        pg.draw.rect(self.surface, color_arrow_width, (self.x - 2.5 * self.scale, self.y - 8 * self.scale,
                                                 5 * self.scale,            8 * self.scale), self.scale // 3)
        pg.draw.polygon(self.surface, color_arrow_fill, ((self.x - 6 * self.scale, self.y),
                                                    (self.x, self.y + 8 * self.scale),
                                                    (self.x + 6 * self.scale, self.y)))
        pg.draw.polygon(self.surface, color_arrow_width, ((self.x - 6 * self.scale, self.y),
                                                         (self.x, self.y + 8 * self.scale),
                                                         (self.x + 6 * self.scale, self.y)), self.scale // 3)

        pg.draw.rect(self.surface, color_arrow_fill, (self.x - 2.2*self.scale, self.y - self.scale,
                                                   4.4 * self.scale,        5*self.scale))
        pg.draw.rect(self.surface, color_bar, (self.x - 0.3 * self.scale, self.y - 7.7 * self.scale,
                                               0.6 * self.scale,          (44 / 6 + 8) * self.scale))


class DrawableArrowRight(DrawableArrow):
    def __init__(self, *args):
        """ constructor of class "DrawableArrowRight" which the subclass of class "DrawableArrow" """
        super().__init__(*args)
        self.direction = 'Right'

    def draw_right_arrow(self):
        color_arrow_width = None
        color_arrow_fill = None
        color_bar = None
        if self.condition == 'normal' and not self.is_target:
            color_arrow_width = white
            color_arrow_fill = light_grey
            color_bar = yellow
        elif self.condition == 'ok' and not self.is_target:
            color_arrow_width = white
            color_arrow_fill = green
            color_bar = green
        elif self.condition == 'bad' and not self.is_target:
            color_arrow_width = white
            color_arrow_fill = red
            color_bar = red
        elif self.is_target == True:
            color_arrow_width = white
            color_arrow_fill = dark_grey
            color_bar = dark_grey

        pg.draw.rect(self.surface, color_arrow_fill, (self.x - 8 * self.scale, self.y - 2.5 * self.scale,
                                                 8 * self.scale,          5 * self.scale))
        pg.draw.rect(self.surface, color_arrow_width, (self.x - 8 * self.scale, self.y - 2.5 * self.scale,
                                                      8 * self.scale, 5 * self.scale), self.scale // 3)
        pg.draw.polygon(self.surface, color_arrow_fill, ((self.x, self.y - 6 * self.scale),
                                                    (self.x + 8 * self.scale, self.y),
                                                    (self.x, self.y + 6 * self.scale)))
        pg.draw.polygon(self.surface, color_arrow_width, ((self.x, self.y - 6 * self.scale),
                                                         (self.x + 8 * self.scale, self.y),
                                                         (self.x, self.y + 6 * self.scale)), self.scale // 3)
        pg.draw.rect(self.surface, color_arrow_fill, (self.x - 1 * self.scale, self.y - 2.2 * self.scale,
                                                      2 * self.scale, 4.4 * self.scale))
        pg.draw.rect(self.surface, color_bar, (self.x - 7.7 * self.scale,   self.y - 0.3 * self.scale,
                                               (15.1) * self.scale, 0.6 * self.scale))


class DrawableArrowLeft(DrawableArrow):
    def __init__(self, *args):
        """ constructor of class "DrawableArrowRight" which the subclass of class "DrawableArrow" """
        super().__init__(*args)
        self.direction = 'Left'

    def draw_left_arrow(self):
        color_arrow_width = None
        color_arrow_fill = None
        color_bar = None
        if self.condition == 'normal' and not self.is_target:
            color_arrow_width = white
            color_arrow_fill = light_grey
            color_bar = yellow
        elif self.condition == 'ok' and not self.is_target:
            color_arrow_width = white
            color_arrow_fill = green
            color_bar = green
        elif self.condition == 'bad' and not self.is_target:
            color_arrow_width = white
            color_arrow_fill = red
            color_bar = red
        pg.draw.rect(self.surface, color_arrow_fill, (self.x,         self.y - 2.5 * self.scale,
                                                 8 * self.scale, 5 * self.scale))
        pg.draw.rect(self.surface, color_arrow_width, (self.x, self.y - 2.5 * self.scale,
                                                      8 * self.scale, 5 * self.scale), self.scale // 3)
        pg.draw.polygon(self.surface, color_arrow_fill, ((self.x, self.y - 6 * self.scale),
                                                    (self.x - 8 * self.scale, self.y),
                                                    (self.x, self.y + 6 * self.scale)))
        pg.draw.polygon(self.surface, color_arrow_width, ((self.x, self.y - 6 * self.scale),
                                                         (self.x - 8 * self.scale, self.y),
                                                         (self.x, self.y + 6 * self.scale)), self.scale // 3)
        pg.draw.rect(self.surface, color_arrow_fill, (self.x - 1 * self.scale, self.y - 2.2 * self.scale,
                                                      2 * self.scale, 4.4 * self.scale))
        pg.draw.rect(self.surface, color_bar, (self.x - (7.35) * self.scale, self.y - 0.3 * self.scale,
                                               (15.1) * self.scale,    0.6 * self.scale))

class DrawableRightTarget(DrawableArrowRight):
    def __init__(self, *args):
        """ constructor of class "DrawableRightTarget" which the subclass of class "DrawableArrow" """
        super().__init__(*args)
        self.is_target = True

    def draw_right_target(self):
        self.draw_right_arrow()


class DrawableLeftTarget(DrawableArrowLeft):
    def __init__(self, *args):
        """ constructor of class "DrawableLeftTarget" which the subclass of class "DrawableArrowLeft" """
        super().__init__(*args)
        self.is_target = True

    def draw_left_target(self):
        self.draw_left_arrow()

class DrawableUpTarget(DrawableArrowUp):
    def __init__(self, *args):
        """ constructor of class "DrawableUpTarget" which the subclass of class "DrawableArrowUp" """
        super().__init__(*args)
        self.is_target = True

    def draw_up_target(self):
        self.draw_up_arrow()

class DrawableDownTarget(DrawableArrowDown):
    def __init__(self, *args):
        """ constructor of class "DrawableDownTarget" which the subclass of class "DrawableArrowDown" """
        super().__init__(*args)
        self.is_target = True

    def draw_down_target(self):
        self.draw_down_arrow()

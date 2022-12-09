import pygame as pg

red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
orange = (255, 180, 0)


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
        'normal', if the arrow is only going to be hit
        """
        self.surface = surface
        self.x = x
        self.y = y
        self.scale = scale
        self.condition = condition

    def set_condition(self, condition):
        self.condition = condition


class DrawableArrowUp(DrawableArrow):
    def __init__(self, *args):
        """ constructor of class "DrawableArrowUp" which the subclass of class "DrawableArrow" """
        super().__init__(*args)

    def draw_up_arrow(self):
        color_arrow = None
        color_bar = None
        if self.condition == 'normal':
            color_arrow = white
            color_bar = yellow
        elif self.condition == 'ok':
            color_arrow = green
            color_bar = green
        elif self.condition == 'bad':
            color_arrow = red
            color_bar = red
        pg.draw.rect(self.surface, color_arrow, (self.x-2.5*self.scale, self.y,
                                                 5*self.scale,          8*self.scale), self.scale//3)
        pg.draw.polygon(self.surface, color_arrow, ((self.x-6*self.scale, self.y),
                                                    (self.x, self.y-8*self.scale),
                                                    (self.x+6*self.scale, self.y)), self.scale//3)
        pg.draw.rect(self.surface, color_bar, (self.x-0.3*self.scale, self.y-(44/6)*self.scale,
                                               0.6*self.scale,        (44/6+8)*self.scale))


class DrawableArrowDown(DrawableArrow):
    def __init__(self, *args):
        """ constructor of class "DrawableArrowDown" which the subclass of class "DrawableArrow" """
        super().__init__(*args)

    def draw_down_arrow(self):
        color_arrow = None
        color_bar = None
        if self.condition == 'normal':
            color_arrow = white
            color_bar = yellow
        elif self.condition == 'ok':
            color_arrow = green
            color_bar = green
        elif self.condition == 'bad':
            color_arrow = red
            color_bar = red
        pg.draw.rect(self.surface, color_arrow, (self.x - 2.5 * self.scale, self.y - 8 * self.scale,
                                                 5 * self.scale,            8 * self.scale), self.scale // 3)
        pg.draw.polygon(self.surface, color_arrow, ((self.x - 6 * self.scale, self.y),
                                                    (self.x, self.y + 8 * self.scale),
                                                    (self.x + 6 * self.scale, self.y)), self.scale // 3)
        pg.draw.rect(self.surface, color_bar, (self.x - 0.3 * self.scale, self.y - 8 * self.scale,
                                               0.6 * self.scale,          (44 / 6 + 8) * self.scale))


class DrawableArrowRight(DrawableArrow):
    def __init__(self, *args):
        """ constructor of class "DrawableArrowRight" which the subclass of class "DrawableArrow" """
        super().__init__(*args)

    def draw_right_arrow(self):
        color_arrow = None
        color_bar = None
        if self.condition == 'normal':
            color_arrow = white
            color_bar = yellow
        elif self.condition == 'ok':
            color_arrow = green
            color_bar = green
        elif self.condition == 'bad':
            color_arrow = red
            color_bar = red
        pg.draw.rect(self.surface, color_arrow, (self.x - 8 * self.scale, self.y - 2.5 * self.scale,
                                                 8 * self.scale,          5 * self.scale), self.scale // 3)
        pg.draw.polygon(self.surface, color_arrow, ((self.x, self.y - 6 * self.scale),
                                                    (self.x + 8 * self.scale, self.y),
                                                    (self.x, self.y + 6 * self.scale)), self.scale // 3)
        pg.draw.rect(self.surface, color_bar, (self.x - 8 * self.scale,   self.y - 0.3 * self.scale,
                                               (44 / 6 + 8) * self.scale, 0.6 * self.scale))


class DrawableArrowLeft(DrawableArrow):
    def __init__(self, *args):
        """ constructor of class "DrawableArrowRight" which the subclass of class "DrawableArrow" """
        super().__init__(*args)

    def draw_left_arrow(self):
        color_arrow = None
        color_bar = None
        if self.condition == 'normal':
            color_arrow = white
            color_bar = yellow
        elif self.condition == 'ok':
            color_arrow = green
            color_bar = green
        elif self.condition == 'bad':
            color_arrow = red
            color_bar = red
        pg.draw.rect(self.surface, color_arrow, (self.x,         self.y - 2.5 * self.scale,
                                                 8 * self.scale, 5 * self.scale), self.scale // 3)
        pg.draw.polygon(self.surface, color_arrow, ((self.x, self.y - 6 * self.scale),
                                                    (self.x - 8 * self.scale, self.y),
                                                    (self.x, self.y + 6 * self.scale)), self.scale // 3)
        pg.draw.rect(self.surface, color_bar, (self.x - (44/6) * self.scale, self.y - 0.3 * self.scale,
                                               (44 / 6 + 8) * self.scale,    0.6 * self.scale))

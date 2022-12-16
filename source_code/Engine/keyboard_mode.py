import pygame as pg
import numpy as np
from source_code.Classes import classes as CL
from source_code.Visualisation.Game import vis_keyboard_mode as Arr_Vis


width, height = 1280, 720       # Screen's width and height
background_color = (0, 0, 0)

pg.display.init()

screen = pg.display.set_mode((width, height))
screen.fill(background_color)
pg.display.flip()


def bit_checker(time_list, timer):
    for i in range(len(time_list)):
        if (0.15 >= time_list[i] - timer.time_getter(CL.start_time) >= -0.1 and
            time_list[i] - timer.time_getter(CL.start_time) <= 0.15):
            return i
    else:
        return 0


def rand_generator(time_list):
    arrow_gen = np.random.randint(4, size=len(time_list))
    return arrow_gen


def arrow_initializer(arrow_gen, time_list):
    arrow_list = []
    for i in range(len(arrow_gen)):
        if arrow_gen[i] == 0:
            arrow_up = Arr_Vis.DrawableArrowUp(screen, 250 + time_list[i] * 200, 225, 3)
            arrow_list.append(arrow_up)
        if arrow_gen[i] == 1:
            arrow_left = Arr_Vis.DrawableArrowLeft(screen, 250 + time_list[i] * 200, 350, 3)
            arrow_list.append(arrow_left)
        if arrow_gen[i] == 2:
            arrow_down = Arr_Vis.DrawableArrowDown(screen, 250 + time_list[i] * 200, 475, 3)
            arrow_list.append(arrow_down)
        if arrow_gen[i] == 3:
            arrow_right = Arr_Vis.DrawableArrowRight(screen, 250 + time_list[i] * 200, 600, 3)
            arrow_list.append(arrow_right)
    return arrow_list


def arrow_mover(arrow_list, timer):
    for i in range(len(arrow_list)):
        arrow_list[i].x_changer(arrow_list[i].start_x_getter() - 200 * timer.time_getter(CL.start_time))


def Event_Holder(event, arrow_list, bit_checker, time_list, fase, timer):       # bit_checker = Timer_Bull from Mouse_Mode
    i = bit_checker(time_list, fase, timer)
    if i != 0:
        if event.type == pg.KEYDOWN:
            if (event.key == pg.K_w or event.key == pg.K_UP) and arrow_list[i].direction_getter() == "Up":
                arrow_list[i].not_draw()
                CL.counter.adder(1)
            if (event.key == pg.K_a or event.key == pg.K_LEFT) and arrow_list[i].direction_getter() == "Left":
                arrow_list[i].not_draw()
                CL.counter.adder(1)
            if (event.key == pg.K_s or event.key == pg.K_DOWN) and arrow_list[i].direction_getter() == "Down":
                arrow_list[i].not_draw()
                CL.counter.adder(1)
            if (event.key == pg.K_d or event.key == pg.K_RIGHT) and arrow_list[i].direction_getter() == "Right":
                arrow_list[i].not_draw()
                CL.counter.adder(1)


def Arr_Drawer(arrow_list):
    for i in range(1, len(arrow_list)):
        if arrow_list[i].drawable_getter():
            arrow_list[i].draw_arrow()


Target_List = [Arr_Vis.DrawableUpTarget(screen, 250, 225, 4), Arr_Vis.DrawableLeftTarget(screen, 250, 350, 4),
               Arr_Vis.DrawableDownTarget(screen, 250, 475, 4), Arr_Vis.DrawableRightTarget(screen, 250, 600, 4)]


def Targ_Drawer(Target_List):
    for el in Target_List:
        el.draw_target()

import time

import pygame as pg
import numpy as np
from source_code.Visualisation.Game import Vis_Mouse_Mode as Ms_Vis
from source_code.Visualisation.Background import Background as bg
from source_code.Sound_Rhytm import Sound_Rhytm_Mouse as SR
from source_code.Classes import Classes as CL
from source_code.Classes import timer_creator as Time_Lists
from source_code.Visualisation.Game import Vis_Keyboard_Mode as Arr_Vis

width, height = 1280, 720       # Screen's width and height
background_color = (0, 0, 0)

pg.display.init()

screen = pg.display.set_mode((width, height))
screen.fill(background_color)
pg.display.flip()

def rand_generator(time_list):
    arrow_gen = np.random.randint(4, size=len(time_list))
    return arrow_gen

def arrow_initializer(arrow_gen):
    arrow_list = []
    for i in range(len(arrow_gen)):
        if arrow_gen[i] == 0:
            Arrow_Up = Arr_Vis.DrawableArrowUp(screen, 50 + i * 100, 200, 1)
            arrow_list.append(Arrow_Up)
        if arrow_gen[i] == 1:
            Arrow_Left = Arr_Vis.DrawableArrowLeft(screen, 50 + i * 100, 300, 1)
            arrow_list.append(Arrow_Left)
        if arrow_gen[i] == 2:
            Arrow_Down = Arr_Vis.DrawableArrowDown(screen, 50 + i * 100, 400, 1)
            arrow_list.append(Arrow_Down)
        if arrow_gen[i] == 3:
            Arrow_Right = Arr_Vis.DrawableArrowRight(screen, 50 + i * 100, 500, 1)
            arrow_list.append(Arrow_Right)
    return arrow_list

def arrow_mover(arrow_list, timer):
    for i in range(len(arrow_list)):
        arrow_list[i].x_changer(arrow_list[i].start_x_getter() - 100 * timer.time_getter(CL.start_time))

def Event_Holder(event, arrow_list, bit_checker):       # bit_checker = Timer_Bull from Mouse_Mode
    for i in range(len(arrow_list)):
        if event.type == pg.KEYDOWN and bit_checker:
            if event.key == pg.K_w or event.key == pg.K_UP and arrow_list[i].direction_getter() == "Up":
                arrow_list[i].not_draw()
            if event.key == pg.K_a or event.key == pg.K_LEFT and arrow_list[i].direction_getter() == "Left":
                arrow_list[i].not_draw()
            if event.key == pg.K_s or event.key == pg.K_DOWN and arrow_list[i].direction_getter() == "Down":
                arrow_list[i].not_draw()
            if event.key == pg.K_d or event.key == pg.K_RIGHT and arrow_list[i].direction_getter() == "Right":
                arrow_list[i].not_draw()

def Drawer(arrow_list): #
    for i in range(len(arrow_list)):
        if arrow_list[i].drawable_getter():
            arrow_list[i].draw_arrow()
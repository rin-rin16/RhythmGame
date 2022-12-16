import pygame as pg
from source_code.Engine import Final
from source_code.Classes import Classes as CL

pg.init()

screen = pg.display.set_mode((1280, 720))

finished = False
running = CL.BullVariables()
pressing = CL.NumVariables('none')
mode_type = CL.NumVariables()
mode_choice = CL.BullVariables(False)
play_quit_menu = CL.BullVariables(True)
trek_choice = CL.NumVariables(0)
while running.getter():
    Final.logic(running,pressing,screen,mode_type,mode_choice,trek_choice,play_quit_menu)


pg.quit()

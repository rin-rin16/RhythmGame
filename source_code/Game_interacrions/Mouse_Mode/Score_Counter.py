import pygame

from pygame.draw import *


class Score:

    def __init__(self):
        self.value = 0

    def score_up(self):
        self.value += 1

    def score_down(self):
        self.value -= 1

    def draw(self):
        myfont = pygame.font.SysFont("monospace", 50)
        score = myfont.render(f'Score: {str(self.value)} ', 1, (255, 255, 255))
        screen.blit(score, (270, 250))


def is_click():
    if (x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2 <= r ** 2:
        return True


def feedback():
    myfont = pygame.font.SysFont("monospace", 50)
    score = myfont.render(f'Это сигнал для Егора чтобы он заметил', 1, (255, 255, 255))
    screen.blit(score, (270, 250))
    print("щелчок прошел")


finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if is_click():
                feedback()

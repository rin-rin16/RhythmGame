import pygame

from pygame.draw import *


class Score:

    def __init__(self):
        self.value = 0

    def up(self):
        self.value += 1

    def down(self):
        self.value -= 1

    def draw(self):
        myfont = pygame.font.SysFont("monospace", 50)
        score = myfont.render(f'Score: {str(self.value)} ', 1, (255, 255, 255))
        screen.blit(score, (270, 250))


class HitBoxOfBall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 10

    def is_click(self):
        if (self.x - event.pos[0]) ** 2 + (self.y - event.pos[1]) ** 2 <= self.r ** 2:
            return True

    def feedback(self):
        myfont = pygame.font.SysFont("monospace", 50)
        score = myfont.render(f'Это сигнал для Егора чтобы он заметил', 1, (255, 255, 255))
        screen.blit(score, (270, 250))
        print("щелчок прошел")



finished = False
ball = HitBoxOfBall(x,y)
score = Score()


while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ball.is_click():
                score.up()
                ball.feedback()
                # поменять шарам цвета
                # переместить хит бокс шара к следующему

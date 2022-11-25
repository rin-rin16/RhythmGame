import pygame as pg


background_image = pg.image.load('Cyberpunk-2077-logo_1920x1080.jpeg')


def background_fill(screen):
    """
    Varning!!! put in the top of the main cicle
    :param screen: screen where photo must be put
    :return: fillss background with photo
    """

    screen.blit(background_image, (0, 0))



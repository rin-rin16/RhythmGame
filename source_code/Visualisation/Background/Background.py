import pygame as pg


def background_fill(screen):
    """
    Varning!!! put in the top of the main cicle
    :param screen: screen where photo must be put
    :return: fillss background with photo
    """
    background_image = pg.image.load('/Users/egorpatesman/PycharmProjects/RhythmGame/source_code/Visualisation/Background/Cyberpunk-2077-logo_1920x1080.jpeg')

    screen.blit(background_image, (0, 0))



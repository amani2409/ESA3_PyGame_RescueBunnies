import pygame

from classes import variables
# from classes.variables import WIDTH, HEIGHT, BLACK, WHITE


# help with sprite from http://programarcadegames.com/python_examples/en/sprite_sheets/
class SpriteSheet(object):
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert_alpha()

    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))

        return image
import pygame
import random

from classes.spritesheet import SpriteSheet
from classes.variables import WIDTH


class BunnyNPC(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        spritesheet = SpriteSheet('Assets/images/bunnyspriteNpc.png')
        sprite_width = 54
        sprite_height = 50

        self.npc_walking_right = []
        self.npc_walking_left = []

        for i in range(2):
            image = spritesheet.get_image(i * sprite_width, 0, sprite_width, sprite_height)
            image.set_colorkey([255, 255, 255])
            self.npc_walking_right.append(image)

        for i in range(2):
            image = pygame.transform.flip(spritesheet.get_image(i * sprite_width, 0, sprite_width, sprite_height), True,
                                          False)
            image.set_colorkey([255, 255, 255])
            self.npc_walking_left.append(image)

        self.image = self.npc_walking_right[0]
        self.rect = self.image.get_rect(topleft=(random.randint(0, WIDTH - sprite_width), 50))

        self.direction = random.choice(['right', 'left'])
        self.speed = random.randint(2, 4)
        self.frame = 0
        self.frame_tmp = 0
        self.frame_speed = 0.1

    # help for randomize movement of npc: https://www.geeksforgeeks.org/pygame-random-movement-of-object/
    def update(self):
        # frame = int((self.rect.x // 10) % 2)  # weil nur 3 frames vom spritesheet pro Richtung genutzt werden

        if self.direction == 'right':
            self.rect.x += self.speed
            self.frame_tmp += self.frame_speed
            if self.frame_tmp >= len(self.npc_walking_left):
                self.frame_tmp = 0
            self.frame = int(self.frame_tmp) % len(self.npc_walking_left)
            self.image = self.npc_walking_left[self.frame]
            if self.rect.x >= WIDTH:
                self.direction = 'left'

        else:
            self.rect.x -= self.speed
            self.frame_tmp += self.frame_speed
            if self.frame_tmp >= len(self.npc_walking_right):
                self.frame_tmp = 0
            self.frame = int(self.frame_tmp) % len(self.npc_walking_right)
            self.image = self.npc_walking_right[self.frame]
            if self.rect.x <= 0:
                self.direction = 'right'

        # self.is_moving = False


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        spritesheet = SpriteSheet('Assets/images/bunnysprite.png')

        sprite_width = 80
        sprite_height = 51

        self.player_walking_right = []
        self.player_walking_left = []

        # initial standing of the player
        self.direction = 'right'
        self.is_moving = False

        for i in range(3, 6):  # frame 3 - 6 sind für die rechte Richtung
            image = spritesheet.get_image(i * sprite_width, 0, sprite_width, sprite_height)
            self.player_walking_right.append(image)

        for i in range(3):  # frame 1 - 3 sind für die rechte Richtung
            image = spritesheet.get_image(i * sprite_width, 0, sprite_width, sprite_height)
            self.player_walking_left.append(image)

        self.image = self.player_walking_right[2]  # frame 3-6, aber hat index 0-2!
        self.rect = self.image.get_rect()

    def moving(self, x, y):
        self.rect.x += x
        self.rect.y += y
        self.is_moving = True

    def update(self):
        if self.is_moving:
            frame = int((self.rect.x // 10) % 3)  # weil nur 3 frames vom spritesheet pro Richtung genutzt werden
            if self.direction == 'right':
                self.image = self.player_walking_right[frame]
            if self.direction == 'left':
                self.image = self.player_walking_left[frame]
        else:  # if standing, dann soll es auch das richtige frame haben und die dazugehörige Richtung
            if self.direction == 'right':
                self.image = self.player_walking_right[2]
            if self.direction == 'left':
                self.image = self.player_walking_left[0]

        self.is_moving = False

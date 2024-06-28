import pygame
import random

from classes.spritesheet import SpriteSheet
from classes.variables import WIDTH


# Creating the NPCs
class BunnyNPC(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        spritesheet = SpriteSheet('Assets/images/bunnyspriteNpc.png')
        sprite_width = 54
        sprite_height = 50

        self.npc_walking_right = []
        self.npc_walking_left = []

        # Animation for walking to the right side
        for i in range(2):
            image = spritesheet.get_image(i * sprite_width, 0, sprite_width, sprite_height)
            image.set_colorkey([255, 255, 255])
            self.npc_walking_right.append(image)

        # 2. animation so the spritesheet can be flipped and the npc is facing the right side (left)
        for i in range(2):
            image = pygame.transform.flip(spritesheet.get_image(i * sprite_width, 0, sprite_width, sprite_height), True,
                                          False)
            image.set_colorkey([255, 255, 255])
            self.npc_walking_left.append(image)

        self.image = self.npc_walking_right[0]  # initial image
        self.rect = self.image.get_rect(topleft=(random.randint(0, WIDTH - sprite_width), 50))

        self.direction = random.choice(['right', 'left'])
        self.speed = random.randint(2, 4)
        self.frame = 0
        self.frame_tmp = 0
        self.frame_speed = 0.1
        self.is_catched = False

    # help for randomize movement of npc: https://www.geeksforgeeks.org/pygame-random-movement-of-object/
    def update(self, player=None):
        if not self.is_catched:
            if self.direction == 'right':
                self.rect.x += self.speed
                if self.rect.right > WIDTH:
                    self.rect.right = WIDTH
                    self.direction = 'left'
                self.frame_tmp += self.frame_speed
                if self.frame_tmp >= len(self.npc_walking_left):
                    self.frame_tmp = 0
                self.frame = int(self.frame_tmp) % len(self.npc_walking_left)
                self.image = self.npc_walking_left[self.frame]
                if self.rect.x >= WIDTH:
                    self.direction = 'left'

            else:
                self.rect.x -= self.speed
                if self.rect.left < 0:
                    self.rect.left = 0
                    self.direction = 'right'
                self.frame_tmp += self.frame_speed
                if self.frame_tmp >= len(self.npc_walking_right):
                    self.frame_tmp = 0
                self.frame = int(self.frame_tmp) % len(self.npc_walking_right)
                self.image = self.npc_walking_right[self.frame]
                if self.rect.x <= 0:
                    self.direction = 'right'

        else:
            self.carried_npc(player)

    # NPC shoudn't move alone -> should move with the player
    def carried_npc(self, player):
        if player is not None and player.rect is not None:
            self.rect.x = player.rect.x + player.rect.width // 2 - self.rect.width // 2
            self.rect.y = player.rect.y + player.rect.height // 2 - self.rect.height // 2


# Creating Player
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

        for i in range(3, 6):  # frame 3 - 6 for walking right
            image = spritesheet.get_image(i * sprite_width, 0, sprite_width, sprite_height)
            self.player_walking_right.append(image)

        for i in range(3):  # frame 1 - 3 for walking left
            image = spritesheet.get_image(i * sprite_width, 0, sprite_width, sprite_height)
            self.player_walking_left.append(image)

        self.image = self.player_walking_right[2]  # frame 3-6, aber hat index 0-2! -> inital standing frame
        self.rect = self.image.get_rect()

        self.catched_bunny = None
        self.count_catched_bunny = 0

    def moving(self, x, y):
        self.rect.x += x
        self.rect.y += y
        self.is_moving = True

        # for not moving beyond the window
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    # updating the player movement
    def update(self):
        if self.is_moving:
            frame = int((self.rect.x // 10) % 3)  # using only 3 frames because its divide in two directions
            if self.direction == 'right':
                self.image = self.player_walking_right[frame]
            if self.direction == 'left':
                self.image = self.player_walking_left[frame]
        else:  # if standing, then it should face the right direction
            if self.direction == 'right':
                self.image = self.player_walking_right[2]
            if self.direction == 'left':
                self.image = self.player_walking_left[0]

        self.is_moving = False

    def catch_release(self, npc_bunny, house):
        keys = pygame.key.get_pressed()

        if self.catched_bunny is None and keys[
            pygame.K_s]:  # if no bunny is catched already, because can only catch one!
            collide = pygame.sprite.spritecollide(self, npc_bunny,
                                                  False)  # if it collides with a npc bunny; no kill because need to release

            for bunny in collide:
                self.catched_bunny = bunny
                self.catched_bunny.is_catched = True
                self.catched_bunny.carried_npc(bunny)
                break  # only 1 bunny to catch

        elif self.catched_bunny is not None and self.catched_bunny.is_catched and keys[pygame.K_w]:
            if house.collidepoint(self.rect.center):
                self.catched_bunny.kill()
                self.count_catched_bunny += 1  # counting the npc which were catched
            else:
                self.catched_bunny.is_catched = False  # release npc if its not collide with the house
            self.catched_bunny = None

import pygame

import levels
from classes.spritesheet import SpriteSheet

from classes.variables import WIDTH, HEIGHT


class Bunny(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/images/bunnyspriteNpc.png')
        self.rect = self.image.get_rect(topleft=(50, 50))
        self.caught = False

    def update(self):
        if self.caught:
            self.rect.x, self.rect.y = pygame.mouse.get_pos()


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

        self.image = self.player_walking_right[2]  # fram 3-6, aber hat index 0-2!
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


def game(level):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Rescue Bunnies')

    bunny = Bunny()
    player = Player()

    if level == 1:
        levels.Level1(player)

    player_sprite = pygame.sprite.Group()
    player_sprite.add(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.direction = 'left'
            player.moving(-5, 0)
        if keys[pygame.K_d]:
            player.direction = 'right'
            player.moving(5, 0)

        player_sprite.update()

        screen.fill((0, 0, 0))  # Bildschirm löschen
        player_sprite.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

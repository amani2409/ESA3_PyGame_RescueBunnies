import pygame

from classes.variables import WIDTH, HEIGHT
from classes.characters import BunnyNPC, Player


class Level:
    def __init__(self):
        self.player = None
        self.npc_bunny = None
        self.background = None
        self.ground = None
        self.ground_rect = None
        self.house = None
        self.house_rect = None
        self.player_sprite = pygame.sprite.Group()
        self.npc_bunny_sprite = pygame.sprite.Group()

        self.time_limit = 0

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.ground, self.ground_rect)
        screen.blit(self.house, self.house_rect)
        self.npc_bunny_sprite.draw(screen)
        self.player_sprite.draw(screen)


class Level1(Level):
    def __init__(self):
        super().__init__()

        self.time_limit = 15

        self.background = pygame.image.load('Assets/images/background.png')
        self.ground = pygame.image.load('Assets/images/ground.png')
        self.ground = pygame.transform.scale(self.ground, (WIDTH, self.ground.get_height()))
        self.ground_rect = self.ground.get_rect()
        self.ground_rect.y = HEIGHT - self.ground_rect.height

        self.house = pygame.image.load('Assets/images/tiny-house.png')
        self.house = pygame.transform.scale(self.house, (80, 60))
        self.house_rect = self.house.get_rect()
        self.house_rect.y = self.ground_rect.y - self.house_rect.height
        self.house_rect.x = WIDTH - self.house_rect.width

        self.player = Player()

        self.player.rect.y = self.ground_rect.y - self.player.rect.height
        self.player_sprite = pygame.sprite.Group()
        self.player_sprite.add(self.player)

        for i in range(2):
            self.npc_bunny = BunnyNPC()
            self.npc_bunny.rect.y = self.ground_rect.y - self.npc_bunny.rect.height
            self.npc_bunny_sprite.add(self.npc_bunny)


class Level2(Level):
    def __init__(self):
        super().__init__()

        self.time_limit = 30

        self.background = pygame.image.load('Assets/images/background.png')
        self.ground = pygame.image.load('Assets/images/ground.png')
        self.ground = pygame.transform.scale(self.ground, (WIDTH, self.ground.get_height()))

        self.ground_rect = self.ground.get_rect()
        self.ground_rect.y = HEIGHT - self.ground_rect.height


        self.house = pygame.image.load('Assets/images/tiny-house.png')
        self.house = pygame.transform.scale(self.house, (80, 60))
        self.house_rect = self.house.get_rect()
        self.house_rect.y = self.ground_rect.y - self.house_rect.height
        self.house_rect.x = WIDTH - self.house_rect.width

        self.player = Player()

        self.player.rect.y = self.ground_rect.y - self.player.rect.height
        self.player_sprite = pygame.sprite.Group()
        self.player_sprite.add(self.player)

        for i in range(2):
            self.npc_bunny = BunnyNPC()
            self.npc_bunny.rect.y = self.ground_rect.y - self.npc_bunny.rect.height
            self.npc_bunny_sprite.add(self.npc_bunny)

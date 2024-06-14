import pygame
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

        sprite_width = 50
        sprite_height = 60
        # self.anims = anims
        # self.frame = 0
        # self.image = spritesheet.get_image(self.anims['right'][0])

        self.player_walking_right = []
        self.player_walking_left = []

        # initial standing of the player
        self.direction = 'right'

        image = spritesheet.get_image(0, 0, sprite_width, sprite_height)
        self.player_walking_right.append(image)

        image = spritesheet.get_image(sprite_width, 0, sprite_width, sprite_height)
        self.player_walking_right.append(image)

        image = spritesheet.get_image(sprite_width*2, 0, sprite_width, sprite_height)
        self.player_walking_right.append(image)

        image = spritesheet.get_image(0, 0, sprite_width, sprite_height)
        image = pygame.transform.flip(image, True, False)
        self.player_walking_left.append(image)

        image = spritesheet.get_image(sprite_width, 0, sprite_width, sprite_height)
        image = pygame.transform.flip(image, True, False)
        self.player_walking_left.append(image)

        image = spritesheet.get_image(sprite_width * 2, 0, sprite_width, sprite_height)
        image = pygame.transform.flip(image, True, False)
        self.player_walking_left.append(image)


        self.image = self.player_walking_right[0]
        self.rect = self.image.get_rect()

        # self.rect = self.image.get_rect(topleft=(50, 50))
        # self.holding = None

    def moving(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def update(self):
        if self.direction == 'right':
            self.image = self.player_walking_right[0]
        if self.direction == 'left':
            self.image = self.player_walking_left[0]


def game(level):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Rescue Bunnies')

    bunny = Bunny()
    #
    # player_sprite_width = 50
    # player_sprite_height = 60
    #
    # anims = {
    #     'right': [(0, 0), (50, 0), (50, 0)],
    #     'left': [(0, 0), (300, 0), (150, 0)],
    # }
    #
    # player_spritesheet_data = (0, 0, 50, 60)
    player = Player()

    player_sprite = pygame.sprite.Group()
    player_sprite.add(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.moving(-1, 0)
        if keys[pygame.K_d]:
            player.moving(1, 0)

        player_sprite.update()

        player_sprite.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    game(1)

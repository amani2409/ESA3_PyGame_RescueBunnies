import pygame, random
from levels import *
from classes.spritesheet import SpriteSheet
from classes.variables import WIDTH, HEIGHT, BLACK


def game(level_nr):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Rescue Bunnies')

    font = pygame.font.SysFont('Arial', 20)
    quit_button = font.render('Quit [Esc]', True, (255, 255, 255))
    quit_button_rect = quit_button.get_rect(topright=(WIDTH - 10, 10))


    # http://programarcadegames.com/python_examples/en/sprite_sheets/
    level_list = [Level1, Level2]
    level = level_list[level_nr - 1]()
    text_level = font.render('Level ' + str(level_nr), True, (255, 255, 255))

    # later to do the loop dynamical
    # for i in range(level_count):
    #     level_list.append(level.Level.__str__(i))

    current_level = 0  # later get number of the logged user
    current_level = level_list[current_level]

    player = level.player
    player_sprite = pygame.sprite.Group(player)
    npc_bunny_sprite = level.npc_bunny_sprite

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

        if keys[pygame.K_ESCAPE]:
            return "start_menu"

        player_sprite.update()
        npc_bunny_sprite.update()

        screen.fill((0, 0, 0))  # Bildschirm löschen
        level.draw(screen)
        screen.blit(quit_button, quit_button_rect.topleft)
        screen.blit(text_level, text_level.get_rect(topleft=(10, 10)))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

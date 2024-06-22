import pygame, random
from levels import *
from classes.spritesheet import SpriteSheet
from classes.variables import WIDTH, HEIGHT, BLACK
from screen import draw_endScreen


def draw_timer(screen, time, font):
    timer_text = font.render(str(time), True, (255, 255, 255))
    screen.blit(timer_text, timer_text.get_rect(midtop=(WIDTH // 2, 20)))


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

    # current_level = 0  # later get number of the logged user
    # current_level = level_list[current_level]

    player = level.player
    player_sprite = pygame.sprite.Group(player)
    npc_bunny_sprite = level.npc_bunny_sprite

    all_bunnies = len(npc_bunny_sprite.sprites())

    time_limit = level.time_limit
    timer = pygame.USEREVENT + 1
    pygame.time.set_timer(timer, 1000)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # https://www.reddit.com/r/pygame/comments/enougf/adding_a_countdown_timer_to_a_game/
            elif event.type == timer:
                time_limit -= 1
                if time_limit <= 0:
                    draw_endScreen()
                    pygame.display.flip()
                # else:
                #     pygame.time.set_timer(timer, 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.direction = 'left'
            player.moving(-5, 0)
        if keys[pygame.K_d]:
            player.direction = 'right'
            player.moving(5, 0)

        if keys[pygame.K_ESCAPE]:
            return "start_menu"

        player.catch_release(npc_bunny_sprite, level.house_rect)

        player_sprite.update()
        npc_bunny_sprite.update(player)

        screen.fill((0, 0, 0))  # Bildschirm löschen
        level.draw(screen)
        screen.blit(quit_button, quit_button_rect.topleft)
        text_level_rect = text_level.get_rect(topleft=(10, 10))
        screen.blit(text_level, text_level_rect)

        draw_timer(screen, time_limit, font)

        catched_bunnies_text = font.render(f'{player.count_catched_bunny}/{all_bunnies} Bunnies', True, (255, 255, 255))
        screen.blit(catched_bunnies_text, catched_bunnies_text.get_rect(topleft=(10, text_level_rect.bottom + 10)))

        player_sprite.draw(screen)
        npc_bunny_sprite.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

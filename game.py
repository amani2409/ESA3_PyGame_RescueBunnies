import pygame
from levels import *
from classes.variables import WIDTH, HEIGHT
from screen import draw_nextLevel
from database import get_level, get_highscore, update_user


def draw_timer(screen, time, font):
    timer_text = font.render(str(time), True, (255, 255, 255))
    screen.blit(timer_text, timer_text.get_rect(midtop=(WIDTH // 2, 20)))


def game(user_data):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Rescue Bunnies')

    level_nr = user_data['currentlevel']
    font = pygame.font.SysFont('Arial', 20)
    quit_button = font.render('Quit [Esc]', True, (255, 255, 255))
    quit_button_rect = quit_button.get_rect(topright=(WIDTH - 10, 10))

    # http://programarcadegames.com/python_examples/en/sprite_sheets/
    level_list = [Level1, Level2]
    if level_nr > len(level_list):
        return 'game_completed', user_data['highscore'], user_data['currentlevel']
    level = level_list[level_nr - 1]()
    text_level = font.render('Level ' + str(level_nr), True, (255, 255, 255))

    score = 0

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
                    return 'end_screen', score, level_nr

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.direction = 'left'
            player.moving(-5, 0)
        if keys[pygame.K_d]:
            player.direction = 'right'
            player.moving(5, 0)

        if keys[pygame.K_ESCAPE]:
            return 'start_menu', score, level_nr

        player.catch_release(npc_bunny_sprite, level.house_rect)

        player_sprite.update()
        npc_bunny_sprite.update(player)
        screen = pygame.display.get_surface()
        screen.fill((0, 0, 0))
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

        if player.count_catched_bunny == all_bunnies:
            score = time_limit
            update_user(user_data['username'], user_data['highscore'] + time_limit, user_data['currentlevel'] + 1)
            new_highscore = get_highscore(user_data['username'])
            new_level = get_level(user_data['username'])
            draw_nextLevel()
            if level_nr + 1 > len(level_list):
                return 'game_completed', new_highscore, new_level
            else:
                return 'next_level', new_highscore, new_level


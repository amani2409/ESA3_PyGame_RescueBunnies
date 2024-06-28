# I - Import and initialize
import pygame
from pygame.locals import *

import database
from game import game
from screen import draw_startScreen, draw_endScreen, draw_loginScreen, draw_nextLevel, draw_highscore_screen, \
    draw_gamecompleted_screen
from database import update_highscore, update_level, get_highscore, get_level, init_db, reset_highscore_level, update_user

from classes.variables import WIDTH, HEIGHT, BLACK, WHITE


def main():
    pygame.init()
    init_db()
    display_screen = "login"
    user_data = {}

    keepGoing = True
    # L - Set up loop
    # main loop for running the programm
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if display_screen == 'login':
            user_data = draw_loginScreen()
            if user_data:
                display_screen = 'start_menu'

        elif display_screen == 'start_menu':
            if user_data:
                user_data['highscore'] = get_highscore(user_data['username'])
                user_data['currentlevel'] = get_level(user_data['username'])
                draw_startScreen(user_data)

            if keys[pygame.K_g]:
                display_screen = 'game'
                screen_result, score, new_level = game(user_data)

                if screen_result == 'end_screen':
                    display_screen = 'end_screen'
                    if score > user_data['highscore']:
                        user_data['highscore'] = score
                    if new_level > user_data['currentlevel']:
                        user_data['currentlevel'] = new_level
                    update_user(user_data['username'], user_data['highscore'], user_data['currentlevel'])


                elif screen_result == 'start_menu':
                    display_screen = 'start_menu'

                elif screen_result == 'next_level':
                    if new_level > user_data['currentlevel']:
                        user_data['currentlevel'] = new_level
                    display_screen = 'next_level'

                elif screen_result == 'game_completed':
                    if new_level > user_data['currentlevel']:
                        user_data['currentlevel'] = new_level
                        user_data['highscore'] = score
                    display_screen = 'game_completed'

            if keys[pygame.K_t]:
                display_screen = 'highscore'

            if keys[pygame.K_r]:
                reset_highscore_level(user_data)
                user_data['highscore'] = 0
                user_data['currentlevel'] = 1
                draw_startScreen(user_data)

            if keys[pygame.K_q]:
                keepGoing = False

        elif display_screen == 'highscore':
            draw_highscore_screen()
            if keys[pygame.K_b]:
                display_screen = 'start_menu'
                draw_startScreen(user_data)


        elif display_screen == 'game':
            screen_result, score, new_level = game(user_data)

            if screen_result == 'end_screen':
                display_screen = 'end_screen'
                if score > user_data['highscore']:
                    user_data['highscore'] = score
                if new_level > user_data['currentlevel']:
                    user_data['currentlevel'] = new_level
                update_user(user_data['username'], user_data['highscore'], user_data['currentlevel'])

            elif screen_result == 'start_menu':
                display_screen = 'start_menu'

            elif screen_result == 'next_level':
                if new_level > user_data['currentlevel']:
                    user_data['currentlevel'] = new_level
                display_screen = 'next_level'

            elif screen_result == 'game_completed':
                if new_level > user_data['currentlevel']:
                    user_data['currentlevel'] = new_level
                    user_data['highscore'] = score
                update_user(user_data['username'], user_data['highscore'], user_data['currentlevel'])
                display_screen = 'game_completed'

        elif display_screen == 'next_level':
            draw_nextLevel()
            pygame.display.flip()

            # Wait for user input to go to the next level screen
            waiting_for_input = True
            while waiting_for_input:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_h:
                            display_screen = 'start_menu'
                            waiting_for_input = False
                        elif event.key == pygame.K_n:
                            user_data['currentlevel'] = get_level(user_data['username'])
                            display_screen = 'game'
                            waiting_for_input = False
                        elif event.key == pygame.K_q:
                            keepGoing = False
                            waiting_for_input = False

        elif display_screen == 'end_screen':
            draw_endScreen()
            if keys[pygame.K_r]:
                display_screen = 'game'
            elif keys[pygame.K_h]:
                display_screen = 'start_menu'
            elif keys[pygame.K_q]:
                keepGoing = False

        elif display_screen == 'game_completed':
            draw_gamecompleted_screen()
            if keys[pygame.K_r]:
                reset_highscore_level(user_data)
                user_data['highscore'] = 0
                user_data['currentlevel'] = 1
                display_screen = 'game'
            elif keys[pygame.K_h]:
                display_screen = 'start_menu'
            elif keys[pygame.K_q]:
                keepGoing = False

        pygame.display.flip()
        # clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

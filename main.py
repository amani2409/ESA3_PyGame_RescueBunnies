# I - Import and initialize
import pygame
from pygame.locals import *

import database
from game import game
from screen import draw_startScreen, draw_endScreen, draw_loginScreen, draw_nextLevel, draw_highscore_screen
from database import update_highscore, update_level, get_highscore, get_level, init_db

from classes.variables import WIDTH, HEIGHT, BLACK, WHITE


def main():
    pygame.init()
    database.init_db()
    display_screen = "login"
    user_data = {}

    keepGoing = True
    # L - Set up loop
    # prüft immer ob irgendwann das Programm beendet wurde
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                pygame.quit()
                quit()

        # if display_screen == "login":
        keys = pygame.key.get_pressed()

        if display_screen == 'login':
            user_data = draw_loginScreen()
            if user_data:
                display_screen = 'start_menu'

        elif display_screen == 'start_menu':
            if user_data:
                draw_startScreen(user_data)

            if keys[pygame.K_s]:
                display_screen = 'game'
                screen_result, score, new_level = game(user_data)

                if screen_result == 'end_screen':
                    display_screen = 'end_screen'
                    if score > user_data['highscore']:
                        user_data['highscore'] = score
                        update_highscore(user_data['username'], score)
                    if new_level > user_data['currentlevel']:
                        user_data['currentlevel'] = new_level
                        update_level(user_data['username'], new_level)

                elif screen_result == 'start_menu':
                    update_level(user_data['username'], new_level)
                    display_screen = 'start_menu'

                elif screen_result == 'next_level':
                    display_screen = 'next_level'

            if keys[pygame.K_h]:
                display_screen = 'highscore'

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
                    update_highscore(user_data['username'], score)
                if new_level > user_data['currentlevel']:
                    user_data['currentlevel'] = new_level
                    update_level(user_data['username'], new_level)

            elif screen_result == 'start_menu':
                update_level(user_data['username'], new_level)
                display_screen = 'start_menu'

            elif screen_result == 'next_level':
                display_screen = 'next_level'

        elif display_screen == 'next_level':
            draw_nextLevel()
            pygame.display.flip()

            # Wait for user input on next level screen
            waiting_for_input = True
            while waiting_for_input:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            display_screen = 'game'
                            waiting_for_input = False
                        elif event.key == pygame.K_h:
                            display_screen = 'start_menu'
                            waiting_for_input = False
                        elif event.key == pygame.K_n:
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

        pygame.display.flip()
        # clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

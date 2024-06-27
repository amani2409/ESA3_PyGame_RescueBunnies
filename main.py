# I - Import and initialize
import pygame
from pygame.locals import *

import database
from game import game
from screen import draw_startScreen, draw_endScreen, draw_loginScreen
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
                draw_startScreen(user_data['username'])
            if keys[pygame.K_s]:
                display_screen = 'game'
                # game_over = False
                screen_result, score, new_level = game(user_data['currentlevel'])
                if screen_result == 'end_screen':
                    display_screen = 'end_screen'
                    if score > user_data['highscore']:
                        user_data['highscore'] = score
                        update_highscore(user_data['username'], score)
                    if new_level > user_data['currentlevel']:
                        user_data['currentlevel'] = new_level
                        update_level(user_data['username'], new_level)
                elif screen_result == 'start_menu':
                    display_screen = 'start_menu'
            if keys[pygame.K_q]:
                keepGoing = False
                pygame.quit()
                quit()

        elif display_screen == 'game':
            # running = False
            screen_result, score, new_level = game(user_data['currentlevel'])
            if screen_result == 'end_screen':
                display_screen = 'end_screen'
                if score > user_data['highscore']:
                    user_data['highscore'] = score
                    update_highscore(user_data['username'], score)
                if new_level > user_data['currentlevel']:
                    user_data['currentlevel'] = new_level
                    update_level(user_data['username'], new_level)
            elif screen_result == 'start_menu':
                display_screen = 'start_menu'

        elif display_screen == 'end_screen':
            screen_result = draw_endScreen()
            if keys[pygame.K_r]:
                display_screen = 'game'
            if keys[pygame.K_h]:
                display_screen = 'start_menu'
            if keys[pygame.K_q]:
                display_screen = 'exit'
                keepGoing = False
                pygame.quit()
                quit()

        pygame.display.flip()
        # clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

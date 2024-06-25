# I - Import and initialize
import pygame
from pygame.locals import *

from game import game
from screen import draw_startScreen, draw_endScreen
from highscore import Highscore
from functions import Button

from classes.variables import WIDTH, HEIGHT, BLACK, WHITE


def main():
    pygame.init()
    #
    # #D - Display configuration
    # screen = pygame.display.set_mode((800, 600))
    # pygame.display.set_caption('Hello to Bunnyworld!')
    #
    # #E - Entities
    # background = pygame.image.load('Assets/images/background.png')
    # ground = pygame.image.load('Assets/images/ground.png')
    #
    # #A - Action
    # clock = pygame.time.Clock()
    # startScreen = StartScreen(screen)
    display_screen = "start_menu"

    keepGoing = True
    # L - Set up loop
    # prüft immer ob irgendwann das Programm beendet wure
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                pygame.quit()
                quit()

        # if display_screen == "login":
        keys = pygame.key.get_pressed()

        if display_screen == 'start_menu':
            draw_startScreen()
            if keys[pygame.K_s]:
                display_screen = 'game'
                # game_over = False
                screen_result = game(1)
                if screen_result == 'end_screen':
                    display_screen = 'end_screen'
                elif screen_result == 'start_menu':
                    display_screen = 'start_menu'
            if keys[pygame.K_q]:
                keepGoing = False
                pygame.quit()
                quit()

        elif display_screen == 'game':
            # running = False
            screen_result = game(1)
            if screen_result == 'end_screen':
                display_screen = 'end_screen'
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

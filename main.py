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
                pygame.quit()
                quit()

        # keys = pygame.key.get_pressed()
        # if display_screen == "login":
        keys = pygame.key.get_pressed()

        if display_screen == 'start_menu':
            draw_startScreen()
            if keys[pygame.K_s]:
                display_screen = 'game'
                game_over = False
                game(1)
            if keys[pygame.K_q]:
                display_screen = 'exit'
                pygame.quit()
                quit()

        elif keys[pygame.K_ESCAPE]:
            # running = False
            display_screen = "start_menu"

        elif display_screen == 'endScreen':
            draw_endScreen()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                display_screen = 'game'
                game(1)
            if keys[pygame.K_h]:
                display_screen = "start_menu"
            if keys[pygame.K_q]:
                display_screen = "exit"
            pygame.quit()
            quit()

        pygame.display.flip()
        # clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

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
    displayScreen = "start_menu"

    keepGoing = True
    # L - Set up loop
    # prüft immer ob irgendwann das Programm beendet wure
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        # keys = pygame.key.get_pressed()
        # if displayScreen == "login":
        keys = pygame.key.get_pressed()

        if displayScreen == 'start_menu':
            draw_startScreen()
            if keys[pygame.K_s]:
                displayScreen = 'game'
                game_over = False
                game(level=1)
            if keys[pygame.K_q]:
                displayScreen = 'exit'
                pygame.quit()
                quit()

        elif keys[pygame.K_ESCAPE]:
            # running = False
            displayScreen = "start_menu"


        elif displayScreen == 'endScreen':
            draw_endScreen()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                displayScreen = 'game'
                game(level=1)
            if keys[pygame.K_h]:
                displayScreen = "start_menu"
            if keys[pygame.K_q]:
                displayScreen = "exit"
            pygame.quit()
            quit()

        pygame.display.flip()
        # clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

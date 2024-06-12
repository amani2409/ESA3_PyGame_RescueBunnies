# I - Import and initialize
import pygame
from pygame.locals import *
from screen import draw_startScreen, draw_endScreen
from highscore import Highscore
from functions import Button

from classes.variables import WIDTH, HEIGHT, BLACK, WHITE

# def main():
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
while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

    # keys = pygame.key.get_pressed()
    # if displayScreen == "login":


    if displayScreen == "start_menu":
        draw_startScreen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            displayScreen = "endScreen"
            game_over = False
        if keys[pygame.K_q]:
            displayScreen = "exit"
            pygame.quit()
            quit()

    elif displayScreen == "endScreen":
        draw_endScreen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            displayScreen = "start_menu"
        if keys[pygame.K_h]:
            displayScreen = "start_menu"
        if keys[pygame.K_q]:
            displayScreen = "exit"
            pygame.quit()
            quit()


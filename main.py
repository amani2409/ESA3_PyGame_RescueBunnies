#I - Import and initialize
import pygame
from pygame.locals import *
from startScreen import StartScreen
from highscore import Highscore

def main():
    pygame.init()

    #D - Display configuration
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Hello to Bunnyworld!')

    #E - Entities
    background = pygame.image.load('Assets/images/background.png')
    ground = pygame.image.load('Assets/images/ground.png')

    #A - Action
    clock = pygame.time.Clock()
    startScreen = StartScreen(screen)



    keepGoing = True
    #L - Set up loop
    while keepGoing:
        #T - Timer to set frame rate
        clock.tick(30)
        #E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        #R - Refresh display
        screen.blit(background, (0, 0))
        screen.blit(ground, (600, 800))
        pygame.display.flip()


if __name__ == '__main__':
    main()
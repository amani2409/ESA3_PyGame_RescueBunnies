import sys

import pygame

from classes.variables import WIDTH, HEIGHT


# from functions import Button

# def StartScreen(login_mask=None):
# def __init__(self, screen):
#     self.screen = screen
#     self.font = pygame.font.SysFont('Arial', 50)
#
#     self.player_name = ''
#     self.levels = [1, 2]  # Adding levels
#     self.playing_level = 1
#
#     Button(color=(255, 0, 0), x=60, y=60, width=80, height=100, text='START', fontsize=20, hover_color=(0, 255, 0),
#            font=pygame.font.init(), fontcolor=(0, 0, 0))

# https://www.makeuseof.com/start-menu-and-game-over-screen-with-pygame/
def draw_startScreen():
    background = pygame.image.load('Assets/images/background.png')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Start Menu')
    font = pygame.font.SysFont('Arial', 50)
    title = font.render('Hallo', True, (255, 255, 255))
    start_button = font.render('Start [s]', True, (255, 255, 255))
    quit_button = font.render('Quit [q]', True, (255, 255, 255))
    screen.blit(background, (0, 0))  # blit wird genutzt um eine Sache auf einen andere Sache/Oberfläche zu zeichnen
    screen.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 3 - title.get_height() / 2))
    screen.blit(start_button, (WIDTH / 2 - start_button.get_width() / 2, HEIGHT / 2 - start_button.get_height() / 2))
    screen.blit(quit_button, (WIDTH / 2 - quit_button.get_width() / 2, HEIGHT / 2 + start_button.get_height()))
    pygame.display.update()


def draw_endScreen():
    background = pygame.image.load('Assets/images/background.png')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('End Screen')
    font = pygame.font.SysFont('Arial', 50)
    title = font.render('GameOver', True, (255, 255, 255))
    restart_button = font.render('Restart [r]', True, (255, 255, 255))
    home_button = font.render('Home Screen [h]', True, (255, 255, 255))
    quit_button = font.render('Quit [q]', True, (255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 4 - title.get_height() / 2))
    screen.blit(restart_button,
                (WIDTH / 2 - restart_button.get_width() / 2, HEIGHT / 2 - restart_button.get_height() / 2))
    screen.blit(home_button, (WIDTH / 2 - home_button.get_width() / 2, HEIGHT / 2 + restart_button.get_height()))
    screen.blit(quit_button, (WIDTH / 2 - quit_button.get_width() / 2, HEIGHT / 4 + restart_button.get_height()))
    pygame.display.update()


def draw_nextLevel():
    background = pygame.image.load('Assets/images/background.png')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Winning Screen')
    font = pygame.font.SysFont('Arial', 50)
    title = font.render('Won: You made it!', True, (255, 255, 255))
    restart_button = font.render('Restart [r]', True, (255, 255, 255))
    next_button = font.render('next Level [n]', True, (255, 255, 255))
    home_button = font.render('Home Screen [h]', True, (255, 255, 255))
    quit_button = font.render('Quit [q]', True, (255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 4 - title.get_height() / 2))
    screen.blit(restart_button,
                (WIDTH / 2 - restart_button.get_width() / 2, HEIGHT / 2 - restart_button.get_height() / 2))
    screen.blit(home_button, (WIDTH / 2 - home_button.get_width() / 2, HEIGHT / 2 + restart_button.get_height()))
    screen.blit(next_button, (WIDTH / 2 - next_button.get_width() / 2, HEIGHT / 4 + restart_button.get_height()))
    screen.blit(quit_button, (WIDTH / 2 - quit_button.get_width() / 2, HEIGHT / 6 + restart_button.get_height()))
    pygame.display.update()



def draw_login_mask():
    pygame.display.update()
    pygame.display.set_caption('Login')

# def level_screen():
#     for i in range(0, 20):
#         # D - Display configuration
#         screen = pygame.display.set_mode((800, 600))
#         pygame.display.set_caption('Hello to Bunnyworld!')
#
#         # E - Entities
#         background = pygame.image.load('Assets/images/background.png')
#         ground = pygame.image.load('Assets/images/ground.png')
#
#         pygame.display.flip()
#         pygame.time.wait(10)
#
#
# while login_mask:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             x, y = event.pos
#             if play_button_rect.collidepoint(x, y):
#                 show_menu = False
#                 import main
#
#                 main.main()
#                 break
#             elif quit_button_rect.collidepoint(x, y):
#                 pygame.quit()
#                 sys.exit()

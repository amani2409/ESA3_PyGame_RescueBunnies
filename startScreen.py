import pygame
from functions import Button

def StartScreen():
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 50)

        self.player_name = ''
        self.levels = [1, 2]  # Adding levels
        self.playing_level = 1

        Button(color=(255, 0, 0), x=60, y=60, width=80, height=100, text='START', fontsize=20, hover_color=(0, 255, 0), font=pygame.font.init(), fontcolor=(0, 0, 0))


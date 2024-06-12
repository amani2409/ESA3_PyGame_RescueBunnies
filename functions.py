import pygame
import pygame.font


class Button:
    def __init__(self, color, x, y, width, height, text, font, fontcolor, fontsize, hover_color):
        button = Button(color, x, y, width, height, text, font)
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.color = color
        self.fontcolor = fontcolor
        self.fontsize = fontsize
        self.hover_color = hover_color
        self.buttonf = pygame.font.SysFont(font, self.fontsize)

    def drawButton(self, screen):
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

    # def update(self, screen):

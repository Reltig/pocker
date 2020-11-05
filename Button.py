import pygame
from consts import *


class Button(object):
    def __init__(self, x, y, w, h, text):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.text = text

    def isClicked(self, x, y):
        return (self.x <= x <= self.x + self.width) and (self.y <= y <= self.y + self.height)

    def draw(self, win, color, text_color=BLACK):
        pygame.draw.rect(win, color, (self.x, self.y, self.height, self.width))
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, 1, text_color)
        win.blit(text, (self.x, self.y))

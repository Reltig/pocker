import pygame


class TextPanel(object):
    def __init__(self, x, y, w, h):
        self.text = ''
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, win, text_color=(0,0,0)):
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, 1, text_color)
        win.blit(text, (self.rect.x, self.rect.y))

    def get_rect(self):
        return self.rect

    def get_text(self):
        return self.text

    def update_text(self, t):
        self.text += t

    def clear(self):
        self.text = ''

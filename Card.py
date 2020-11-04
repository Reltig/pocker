import pygame

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['spade', 'heart', 'diamond', 'club']


class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.img = pygame.image.load(f'images/{suit}s.png')

    def __str__(self):
        return f'{self.value} of {self.suit}s'

    def draw(self, win, x0, y0):
        rect = self.img.get_rect(topleft=(x0, y0))
        win.blit(self.img, rect)


def create_new_deck():
    deck = []
    for suit in suits:
        for val in values:
            card = Card(val, suit)
            deck.append(card)
    return deck

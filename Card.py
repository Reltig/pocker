class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f'{self.value} of {self.suit}s'


def create_new_deck():
    deck = []
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['spade', 'heart', 'diamond', 'club']
    for suit in suits:
        for val in values:
            card = Card(val, suit)
            deck.append(card)
    return deck

class Card(object):
    def __init__(self, value, mast):
        self.value = value
        self.mast = mast

    def __str__(self):
        return f'{self.value} of {self.mast}s'


def create_new_deck():
    deck = []
    values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    mast = ['spade', 'heart', 'diamond', 'club']
    for m in mast:
        for val in values:
            card = Card(val, m)
            deck.append(card)
    return deck
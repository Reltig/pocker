class Player(object):
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.score = 0

    def add_card(self, card):
        self.hand.append(card)

    def get_hand(self):
        return self.hand

    def update_score(self, delta_score):
        self.score += delta_score

    def __str__(self):
        return f'{self.name} have score: {self.score}'

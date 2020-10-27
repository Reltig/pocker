class Player(object):
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.cash = 0
        self.current_bet = 0
        self.isPlaying = True

    def add_card(self, card):
        self.hand.append(card)

    def get_hand(self):
        return self.hand

    def update_cash(self, delta_cash):
        self.cash += delta_cash

    def set_current_bet(self, bet):
        self.current_bet = bet

    def get_current_bet(self):
        return self.current_bet

    def exit_from_round(self):
        self.isPlaying = False

    def __str__(self):
        return f'{self.name} have score: {self.cash}'

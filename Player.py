class Player(object):
    def __init__(self, name, cash=300):
        self.hand = []
        self.name = name
        self.cash = cash
        self.current_bet = 0
        self.inGame = True

    def add_card(self, card):
        self.hand.append(card)

    def get_hand(self):
        return self.hand

    def get_cash(self):
        return self.cash

    def update_cash(self, delta_cash):
        self.cash += delta_cash

    def set_current_bet(self, bet):
        self.current_bet = bet

    def get_current_bet(self):
        return self.current_bet

    def exit_from_round(self):
        self.inGame = False

    def __str__(self):
        return self.name

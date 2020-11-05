class Player(object):
    def __init__(self, name, cash=300):
        self.temp_cash = 0
        self.hand = []
        self.name = name
        self.cash = cash
        self.current_bet = 0
        self.inGame = True
        self.current_action = None

    def draw(self):
        pass

    def add_card(self, card):
        self.hand.append(card)

    def get_hand(self):
        return self.hand.copy()

    def get_cash(self):
        return self.cash

    def get_current_bet(self):
        return self.current_bet

    def set_temp_cash(self, cash):
        self.temp_cash = cash

    def set_current_bet(self, bet):
        self.current_bet = bet

    def set_current_action(self, action):
        self.current_action = action

    def get_current_action(self):
        return self.current_action

    def set_current_bet(self, bet):
        self.current_bet = bet

    def update_cash(self, delta_cash):
        self.cash += delta_cash

    def exit_from_round(self):
        self.inGame = False

    def __str__(self):
        return self.name

    def strategy_request(self):
        return int(input("Выберите действие(1.Call 2.Rise 3.Fold 4.Check): "))

    def cash_request(self):
        cash = -1
        while not(cash > 0 and cash <= self.get_cash()):
            cash = self.temp_cash
        return cash

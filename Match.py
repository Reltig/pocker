from Card import create_new_deck
from HandСalcTHRules import get_hand_cost
import random


class Match(object):
    def __init__(self, players):
        self.deck = create_new_deck()
        self.rounds = ['Preflop', 'Flop', 'Turn', 'River']
        self.players = players
        self.dealer_id = 0
        self.cards_on_table = []

    def play_match(self):
        #  TODO: сделать класс для раундов
        self.deck = create_new_deck()
        self.dispensation(self.players, 2)
        for round in self.rounds:
            self.betting(round)
            self.cards_on_table.append(self.deck.pop())
            print('On table: ')
            for card in self.cards_on_table:
                print(f'{card} ')
        self.players_ranking()
        self.end_round()

    def dispensation(self, players, cards_count=2):
        random.shuffle(self.deck)
        for player in players:
            for _ in range(cards_count):
                card = self.deck.pop()
                player.add_card(card)

    def players_ranking(self):
        players_rank = {}
        for player in self.players:
            hand = player.get_hand()
            hand_cost = get_hand_cost(hand)
            players_rank.update([[player, hand_cost]])
        players_rank = {p: c for p, c in sorted(players_rank.items(), key=lambda item: item[1])}
        for p, c in players_rank.items():
            print(f'{p} has hand with {c} cost')
            for card in p.get_hand():
                print(card)

    def choose_action(self, player, axiom_action=None):
        # TODO:  реквесты заинжектить в Player и мб этот метод
        if axiom_action is None:
            strategy_id = self.player_strategy_request(player)
        else:
            strategy_id = axiom_action
        if strategy_id == 1:
            self.call(player)
        elif strategy_id == 2:
            self.rise(player)
        elif strategy_id == 3:
            self.fold(player)
        elif strategy_id == 4:
            self.check(player)
        elif strategy_id == 5:
            self.blind(player)
        elif strategy_id == 6:
            self.big_blind(player)

    def call(self, player):
        previous_player_id = (self.players.index(player) - 1) % len(self.players)
        previous_player = self.players[previous_player_id]
        bet = previous_player.get_current_bet()
        player.set_current_bet(bet)

    def rise(self, player):
        bet = self.player_cash_request(player)
        player.set_current_bet(bet)

    def fold(self, player):
        player.exit_from_round()

    def check(self, player):
        pass

    def blind(self, player):
        bet = self.player_cash_request(player)
        player.set_current_bet(bet)

    def big_blind(self, player):
        prev_player_id = 1
        bet = 2 * self.players[prev_player_id].get_current_bet()
        player.set_current_bet(bet)


    def player_strategy_request(self, player):
        return int(input("Выберите действие(1.Call 2.Rise 3.Fold 4.Check): "))

    def player_cash_request(self, player):
        cash = -1
        while not(cash > 0 and cash <= player.get_cash()):
            cash = int(input("Выберите сумму: "))
        return cash

    def betting(self, round):
        for player_id in range(len(self.players)):
            if round == 'Preflop':
                if player_id == 0:
                    self.choose_action(self.players[player_id], axiom_action=5)  # blind
                elif player_id == 1:
                    self.choose_action(self.players[player_id], axiom_action=6)  # big blind
                else:
                    self.choose_action(self.players[player_id])

            else:
                self.choose_action(self.players[player_id])

    def end_round(self):
        pass
        #  self.dealer_id = (self.dealer_id + 1) % len(self.players)

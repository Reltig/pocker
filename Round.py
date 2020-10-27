from Card import create_new_deck, get_hand_rating
import random


class Round(object):
    def __init__(self, players):
        self.deck = create_new_deck()
        self.players = players
        self.dealer_id = 0
        self.table_cards = []

    def play_round(self):
        self.deck = create_new_deck()
        self.dispensation(self.players, 2)
        self.betting()
        self.players_ranking()
        self.end_round()

    def dispensation(self, players, cards_count=2):
        random.shuffle(self.deck)
        for player in players:
            for _ in range(cards_count):
                card = self.deck.pop()
                player.add_card(card)

    def players_ranking(self):
        for player in self.players:
            hand = player.get_hand()
            #  TODO: реализация подсчёта старшинства карт игроков

    def choose_action(self, player, axiom_action=None):
        if axiom_action is None:
            strategy_id = self.player_strategy_request(player)
        else:
            strategy_id = axiom_action
        if strategy_id == 1:
            previous_player_id = (self.players.index(player) - 1) % len(self.players)
            previous_player = self.players[previous_player_id]
            bet = previous_player.get_current_bet()
            player.set_current_bet(bet)
        elif strategy_id == 2:
            bet = self.player_cash_request()
            player.set_current_bet(bet)
        elif strategy_id == 3:
            player.exit_from_round()
        elif strategy_id == 4:
            # TODO:  условия срабатывания
            pass
        elif strategy_id == 5:#blind
            self.player_cash_request(player)
            pass
        elif strategy_id == 6:#big blind
            previous_player_id = (self.players.index(player) - 1) % len(self.players)
            previous_player = self.players[previous_player_id]
            bet = 2 * previous_player.get_current_bet()
            player.set_current_bet(bet)

    def player_strategy_request(self, player):
        #  TODO: нормальная реализация
        return int(input("Выберите действие(1.Call 2.Rise 3.Fold 4.Check): "))

    def player_cash_request(self, player):
        #  TODO: нормальная реализация
        return int(input("Выберите сумму: "))

    def betting(self):
        # blind and big blind

    def end_round(self):
        self.dealer_id = (self.dealer_id + 1) % len(self.players)

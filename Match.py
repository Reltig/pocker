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

    #  Главная функция
    def play_match(self):
        #  TODO: сделать класс для раундов
        self.deck = create_new_deck()
        self.dispensation(self.players, 2)
        for round in self.rounds:
            if round != 'Preflop':
                print('On table: ')
                for card in self.cards_on_table:
                    print(f'{card} ')
            self.betting(round)
            self.cards_on_table.append(self.deck.pop())
        self.players_ranking()
        self.end_round()

    #  Раздача карт игрокам
    def dispensation(self, players, cards_count=2):
        random.shuffle(self.deck)
        for player in players:
            for _ in range(cards_count):
                card = self.deck.pop()
                player.add_card(card)

    #  Оценка рук игроков
    def players_ranking(self):
        players_rank = {}
        for player in self.players:
            hand = player.get_hand()
            hand.extend(self.cards_on_table)
            hand_cost = get_hand_cost(hand)
            players_rank.update([[player, hand_cost]])
        players_rank = {p: c for p, c in sorted(players_rank.items(), key=lambda item: item[1])}
        for p, c in players_rank.items():
            print(f'{p} has hand with {c} cost')
            for card in p.get_hand():
                print(card)

    # Максимальная ставка
    def get_max_bet(self):
        return max([p.get_current_bet() for p in self.players])

    #  Игрок выбирает действие
    def choose_action(self, player, axiom_action=None):
        # TODO:  реквесты заинжектить в Player и мб этот метод
        if axiom_action is None:
            strategy_id = player.strategy_request()
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

    #  Функции, реализующие действия игрока в период торгов
    def call(self, player):
        previous_player_id = (self.players.index(player) - 1) % len(self.players)
        previous_player = self.players[previous_player_id]
        bet = previous_player.get_current_bet()
        if bet <= player.get_cash():
            player.set_current_bet(bet)
        else:
            print("Невозможное действие. Повторите запрос")
            self.choose_action(player)

    def rise(self, player):
        bet = player.cash_request()
        if bet <= player.get_cash() and bet > self.get_max_bet():
            player.set_current_bet(bet)
        else:
            print("Невозможное действие. Повторите запрос")
            self.choose_action(player)

    def fold(self, player):
        player.exit_from_round()

    def check(self, player):
        bet = player.cash_request()
        if bet == self.get_max_bet():
            player.set_current_bet(bet)
        else:
            print("Невозможное действие. Повторите запрос")
            self.choose_action(player)

    def blind(self, player):
        bet = player.cash_request()
        if bet <= player.get_cash():
            player.set_current_bet(bet)
        else:
            print("Невозможное действие. Повторите запрос")
            self.choose_action(player)

    def big_blind(self, player):
        prev_player_id = 1
        bet = 2 * self.players[prev_player_id].get_current_bet()
        player.set_current_bet(bet)

    #  Ставки
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

    #  Конец раунда
    def end_round(self):
        #  Игроки меняются местами, двигаются по часовому кругу
        t = self.players[1:]
        t.append(self.players[0])

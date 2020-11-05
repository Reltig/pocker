from Card import create_new_deck
from HandСalcTHRules import get_hand_cost
import random


class Match(object):
    def __init__(self, players):
        self.deck = create_new_deck()
        self.rounds = ['Preflop', 'Flop', 'Turn', 'River']
        self.player_actions = {'call': 1, 'rise': 2, 'fold': 3, 'check': 4, 'blind': 5, 'big_blind': 6}
        self.current_round_id = 0
        self.players = players
        self.current_player_id = 0
        self.cards_on_table = []

    def draw(self, win):
        x0 = 0
        y0 = 0
        offset = 150
        i = 0
        for card in self.players[self.current_player_id].get_hand():
            card.draw(win, x0+offset*i, y0)
            i += 1
        i = 0
        if self.cards_on_table is not None:
            for card in self.cards_on_table:
                card.draw(win, x0 + offset*i, y0+260)
                i += 1

    def set_current_action(self, action):
        self.players[self.current_player_id].set_current_action(action)

    #  Главная функция
    def start_match(self):
        #  TODO: сделать класс для раундов
        self.deck = create_new_deck()
        self.dispensation(self.players, 2)

    def update_match(self):
        player = self.players[self.current_player_id]
        if player.get_current_action() is not None:
            round = self.rounds[self.current_round_id]
            action = self.players[self.current_player_id].get_current_action()
            self.betting(round, action)
            self.players[self.current_player_id].set_current_action(None)
            self.current_player_id += 1
            if self.current_player_id >= len(self.players):
                self.start_next_round()

        if self.current_round_id >= len(self.rounds):
            self.end_round()

    #  Раздача карт игрокам
    def dispensation(self, players, cards_count=2):
        random.shuffle(self.deck)
        for player in players:
            for _ in range(cards_count):
                card = self.deck.pop()
                player.add_card(card)

    def start_new_round(self):
        #  TODO: implementation
        self.current_round_id += 1

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
    def choose_action(self, action):
        # TODO:  реквесты заинжектить в Player и мб этот метод
        strategy_id = self.player_actions[action]
        if strategy_id == 1:
            self.call()
        elif strategy_id == 2:
            self.rise()
        elif strategy_id == 3:
            self.fold()
        elif strategy_id == 4:
            self.check()
        elif strategy_id == 5:
            self.blind()
        elif strategy_id == 6:
            self.big_blind()

    #  Функции, реализующие действия игрока в период торгов
    def call(self):
        player = self.players[self.current_player_id]
        previous_player_id = self.current_player_id - 1
        previous_player = self.players[previous_player_id]
        bet = previous_player.get_current_bet()
        if bet <= player.get_cash():
            self.players[self.current_player_id].set_current_bet(bet)

    def get_current_player(self):
        return self.players[self.current_player_id]

    def rise(self):
        player = self.players[self.current_player_id]
        bet = player.cash_request()
        if player.get_cash() >= bet > self.get_max_bet():
            self.players[self.current_player_id].set_current_bet(bet)

    def fold(self):
        self.players[self.current_player_id].exit_from_round()

    def check(self):
        player = self.players[self.current_player_id]
        bet = player.cash_request()
        if bet == self.get_max_bet():
            self.players[self.current_player_id].set_current_bet(bet)

    def blind(self):
        player = self.players[self.current_player_id]
        bet = player.cash_request()
        if bet <= player.get_cash():
            self.players[self.current_player_id].set_current_bet(bet)

    def big_blind(self):
        prev_player_id = 0
        bet = 2 * self.players[prev_player_id].get_current_bet()
        self.players[self.current_player_id].set_current_bet(bet)

    #  Ставки
    def betting(self, round, action):
        if round == 'Preflop':
            if self.current_player_id == 0:
                self.choose_action('blind')  # blind
            elif self.current_player_id == 1:
                self.choose_action('big_blind')  # big blind
            else:
                self.choose_action(action)

        else:
            self.choose_action(action)

    #  Конец раунда
    def end_round(self):
        #  Игроки меняются местами, двигаются по часовому кругу
        #  TODO: перечисление лавэ победителю
        t = self.players[1:]
        t.append(self.players[0])
        self.players = t

    def start_next_round(self):
        self.cards_on_table.append(self.deck.pop())
        self.current_round_id += 1
        self.current_player_id = 0
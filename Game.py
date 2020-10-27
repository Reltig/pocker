from Player import Player
from Card import create_new_deck, get_hand_rating
import random


class Game(object):
    def __init__(self, players_count):
        self.players = [Player('Player' + i) for i in range(players_count)]
        self.deck = create_new_deck()
        self.time = 0
        # TODO: implementation of time

    def dispensation(self, players, cards_count):
        random.shuffle(self.deck)
        for player in players:
            for _ in range(cards_count):
                card = self.deck.pop()
                player.add_card(card)

    def start_round(self):
        self.deck = create_new_deck()
        self.dispensation(self.players, 2)
        for player in self.players:
            hand = player.get_hand()
            delta_score = get_hand_rating(hand)
            player.update_score(delta_score)
            print(player)



if __name__ == '__main__':
    player_count = int(input('Введите количество игроков: '))
    game = Game(player_count)
    game.start_round()

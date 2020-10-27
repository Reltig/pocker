from Card import create_new_deck, get_hand_rating
import random


class Round(object):
    def __init__(self, players):
        self.deck = create_new_deck()
        self.players = players

    def dispensation(self, players, cards_count):
        random.shuffle(self.deck)
        for player in players:
            for _ in range(cards_count):
                card = self.deck.pop()
                player.add_card(card)

    def round(self):
        self.deck = create_new_deck()
        self.dispensation(self.players, 2)
        self.update_players_score()

    def update_players_score(self):
        for player in self.players:
            hand = player.get_hand()
            delta_score = get_hand_rating(hand)
            player.update_score(delta_score)
            print(player, [str(c) for c in player.get_hand()])
            #  print(player)

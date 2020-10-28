import Card
import random


def get_hand_cost(hand):
    random.seed()
    return 100 + random.randint(100, 200)
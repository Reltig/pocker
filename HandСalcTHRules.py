import Card
import random


def calculate_hand_cost(comb):
    random.seed()
    return 100 + random.randint(100, 200)


def get_hand_cost(comb):
    best_comb_cost = -1
    for i in range(len(comb)):
        t = comb[:i]
        t.extend(comb[i + 1:])
        comb_cost = calculate_hand_cost(t)
        if comb_cost > best_comb_cost:
            best_comb_cost = comb_cost
    return best_comb_cost

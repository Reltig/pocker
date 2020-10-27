from Player import Player
from Round import Round


class Game(object):
    def __init__(self, players_count=2):
        self.players = [Player(f'Player {i}') for i in range(players_count)]
        self.time = 0
        # TODO: implementation of time(a nahuya?)

    def start_new_round(self):
        round = Round(self.players)
        round.round()


if __name__ == '__main__':
    # player_count = int(input('Введите количество игроков: '))
    game = Game()
    game.start_new_round()

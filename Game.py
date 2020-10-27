#  правила - техасский холдем
from Player import Player
from Round import Round


class Game(object):
    def __init__(self, players_count=2):
        self.players = [Player(f'Player {i}') for i in range(players_count)]
        self.time = 0
        self.game_is_running = True
        # TODO: implementation of time(a nahuya?)

    def start_game(self):
        while self.game_is_running:
            round = Round(self.players)
            round.play_round()


if __name__ == '__main__':
    # player_count = int(input('Введите количество игроков: '))
    game = Game()
    game.start_game()

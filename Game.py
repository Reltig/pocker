#  правила - техасский холдем
from Player import Player
from Match import Match
import pygame

pygame.init()


class Game(object):
    def __init__(self, win=None, players_count=2):
        self.players = [Player(f'Player {i}') for i in range(players_count)]
        self.time = 0
        self.match = None
        self.win = win
        # TODO: implementation of time(a nahuya?)

    def draw(self):
        self.match.draw(self.win)
        pygame.display.update()

    def run(self):
        run = True
        self.match = Match(self.players)
        self.match.start_match()
        while run:
            self.match.update_match()
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

        pygame.quit()


if __name__ == '__main__':
    # player_count = int(input('Введите количество игроков: '))
    win = pygame.display.set_mode((600, 400))
    game = Game(win)
    game.run()

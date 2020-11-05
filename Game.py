#  правила - техасский холдем
from Player import Player
from Match import Match
import pygame
from consts import *

pygame.init()


class Game(object):
    def __init__(self, win=None, players_count=3):
        self.players = [Player(f'Player {i}') for i in range(players_count)]
        self.time = 0
        self.match = None
        self.win = win
        # TODO: implementation of time(a nahuya?)

    def draw(self):
        self.win.fill(WHITE)
        self.match.draw(self.win)
        pygame.display.update()

    def run(self):
        run = True
        self.match = Match(self.players, self.win)
        self.match.start_match()
        while run:
            self.match.update_match()
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.match.check_buttons(*event.pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.match.text_pan.clear()
                    else:
                        t = event.unicode
                        self.match.text_pan.update_text(t)
        pygame.quit()


if __name__ == '__main__':
    # player_count = int(input('Введите количество игроков: '))
    win = pygame.display.set_mode((600, 400))
    game = Game(win)
    game.run()

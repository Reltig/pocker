#  правила - техасский холдем
from Player import Player
from Match import Match
from Button import Button
import pygame

pygame.init()


class Game(object):
    def __init__(self, win=None, players_count=2):
        self.players = [Player(f'Player {i}') for i in range(players_count)]
        self.time = 0
        self.buttons = [Button(40, 0, 40, 40, 'call'), Button(40, 40, 40, 40, 'rise'), Button(40, 80, 40, 40, 'fold'), Button(40, 120, 40, 40, 'check')]
        self.match = None
        self.win = win
        # TODO: implementation of time(a nahuya?)

    def draw(self):
        self.win.fill((255, 255, 255))
        self.match.draw(self.win)
        for button in self.buttons:
            button.draw(self.win, (125,125,0))
        pygame.display.update()

    def check_buttons(self, x, y):
        for button in self.buttons:
            if button.isClicked(x, y):
                self.match.set_current_action(button.text)

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
                    if event.button == 1:
                        self.check_buttons(*event.pos)

        pygame.quit()


if __name__ == '__main__':
    # player_count = int(input('Введите количество игроков: '))
    win = pygame.display.set_mode((600, 400))
    game = Game(win)
    game.run()

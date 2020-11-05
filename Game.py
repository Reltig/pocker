#  правила - техасский холдем
from Player import Player
from Match import Match
from Button import Button
import pygame
from tempTextPanel import TextPanel

pygame.init()


class Game(object):
    def __init__(self, win=None, players_count=3):
        self.players = [Player(f'Player {i}') for i in range(players_count)]
        self.time = 0
        self.buttons = [Button(0, 200, 40, 60, 'call'), Button(60, 200, 40, 60, 'rise'), Button(120, 200, 40, 60, 'fold'), Button(180, 200, 40, 60, 'check')]
        self.match = None
        self.win = win
        self.text_pan = TextPanel(0, 250, 40, 120)
        # TODO: implementation of time(a nahuya?)

    def draw(self):
        self.win.fill((255, 255, 255))
        self.match.draw(self.win)
        self.text_pan.draw(self.win)
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.text_pan.clear()
                    elif event.key == pygame.K_F1:
                        self.match.get_current_player().set_temp_cash(int(self.text_pan.get_text()))
                    else:
                        t = event.unicode
                        self.text_pan.update_text(t)
        pygame.quit()


if __name__ == '__main__':
    # player_count = int(input('Введите количество игроков: '))
    win = pygame.display.set_mode((600, 400))
    game = Game(win)
    game.run()

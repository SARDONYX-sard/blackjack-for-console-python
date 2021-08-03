import random

from card import Card
from dealer import Dealer
from player import Player


class Blackjack:
    def __init__(self):
        self.message = 'You win.'
        self.cards = [Card(i) for i in range(52)]
        random.shuffle(self.cards)
        self.player = Player()
        self.dealer = Dealer()

    def start_game(self):
        for _ in range(2):
            self.player.draw(self)
            self.dealer.draw(self)
        self.player.act(self)
        player_point = self.player.point()
        self.message = 'You lose.'
        if player_point <= 21:
            self.dealer.act(self)
            dealer_point = self.dealer.point()
            if player_point == dealer_point:
                self.message = 'Draw'

        self.show(False)
        print(self.message)

    def show(self, hide):
        p = self.player.point()
        s = self.player.sequence()
        print(f'Player({p}): {s}')
        p = '--' if hide else self.dealer.point()
        s = self.dealer.sequence(hide)
        print(f'Dealer({p}): {s}')

    def pop(self):
        return self.cards.pop(0)


if __name__ == '__main__':
    while True:
        bj = Blackjack()  # 引数を変えると山札も変わります
        bj.start_game()
        print('-----------------------------------')

import random
import sys

from utils.card import Card
from utils.dealer import Dealer
from utils.player import Player

# 一個上の階層をpathに追加
sys.path.append('../../blackjack-for-console-python')


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

        # Player turn
        self.player.act(self)
        player_point = self.player.get_point()

        self.message = 'You lose.'
        if player_point <= 21:
            # Dealer turn
            self.dealer.act(self)
            dealer_point = self.dealer.get_point()

            if player_point == dealer_point:
                self.message = 'Draw'
            elif dealer_point >= 22 or dealer_point < player_point:
                self.message = 'You win.'

        self.show(False)
        print(self.message)

    def show(self, hide: bool):
        """ディーラーとプレイヤーの得点結果を出力

        Args:
            hide (bool): 最新の持ち札を隠すかどうか
        """
        # Player
        player_point = self.player.get_point()
        player_sequence = self.player.sequence()
        # Dealer
        dealer_point = '--' if hide else self.dealer.get_point()
        dealer_sequence = self.dealer.sequence(hide)

        print(f'Player({player_point}): {player_sequence}')
        print(f'Dealer({dealer_point }): {dealer_sequence}')

    def pop(self):
        return self.cards.pop(0)

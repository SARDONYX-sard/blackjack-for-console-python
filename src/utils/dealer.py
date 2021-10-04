
from .game_part import Blackjack
from .owner import Owner


class Dealer(Owner):
    def act(self, bj: Blackjack):
        """持ち点が16になるまでカードを引き続ける

        Args:
            bj (Blackjack): [description]
        """
        while self.get_point() <= 16:
            self.draw(bj)

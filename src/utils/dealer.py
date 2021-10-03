
import sys

from src.utils.game_part import Blackjack
from src.utils.owner import Owner

# 一個上の階層をpathに追加
sys.path.append('../../blackjack-for-console-python')


class Dealer(Owner):
    def act(self, bj: Blackjack):
        """持ち点が16になるまでカードを引き続ける

        Args:
            bj (Blackjack): [description]
        """
        while self.get_point() <= 16:
            self.draw(bj)

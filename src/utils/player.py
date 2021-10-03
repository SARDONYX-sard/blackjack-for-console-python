import sys

from src.utils.game_part import Blackjack
from src.utils.owner import Owner

# 一個上の階層をpathに追加
sys.path.append('../')


class Player(Owner):
    """カードを引く行動を定義するクラス

    Args:
        Owner ([type]): Ownerクラスを継承している
    """

    def ask_more_draw(self):
        answer = input('もう一枚引く？(y/n):')

        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            return None

    def act(self, bj: Blackjack):
        """持ち点が20以下の間、カードを引くか尋ねる

        Args:
            bj (Blackjack): [description]
        """
        while self.get_point() <= 20:
            self.show_present_state(True)

            is_draw = self.ask_more_draw()
            if is_draw:
                self.draw(bj)
            if is_draw or (is_draw is None):
                continue
            break

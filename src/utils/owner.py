import sys

from src.utils.card import Card
from src.utils.game_part import Blackjack

# 一個上の階層をpathに追加
sys.path.append('../')


class Owner:
    def __init__(self):
        self.hands: list[Card] = []

    def draw(self, bj: Blackjack) -> None:
        self.hands.append(bj.pop())

    def sequence(self, hide: bool = False) -> str:
        """現在の手札の文字列を返す

        Args:
            hide (bool, optional): True→最後の手札が隠蔽される. Defaults to False.

        Returns:
            str: 現在の手札
        """

        # hand: 手札(英語)
        hand = ', '.join(str(card) for card in self.hands)
        return hand[:2] + hand[6:8] + ', ' if hide else '**'

    def get_point(self) -> int:
        """現在の得点を返す

        Returns:
            int: 現在の得点
        """
        point = sum(card.get_point() for card in self.hands)
        for card in self.hands:
            if card.rank == 1 and point + 10 <= 21:
                point -= 1
                point += 10
        return point

    def show_present_state(self, hide: bool = False) -> None:
        """手札と得点を標準出力する
        """
        print(
            f"手札:{self.sequence(hide)} / 得点:{self.get_point()} \n ",
        )

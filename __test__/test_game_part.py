import sys
import unittest

from utils.game_part import Blackjack

import os
sys.path.append(
    os.path.join(
        os.path.abspath(
            os.path.dirname(__file__)),
        'utils/'))


class TestOwner(unittest.TestCase):

    def setUp(self):
        """[summary]
        全てのテストの前に自動実行される準備用の関数
        """
        bj = Blackjack(0)
        self.onetime = ", ".join(
            [f"{bj.pop()}", f"{bj.pop()}", f"{bj.pop()}", f"{bj.pop()}", f"{bj.pop()}", ])

    def test_evalate(self):
        self.assertRegex("♠3, ♦K, ♣7, ♣3, ♠K", f"{self.onetime}")

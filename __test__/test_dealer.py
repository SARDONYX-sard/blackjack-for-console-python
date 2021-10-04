import sys
import unittest

from src.utils.dealer import Dealer
from src.utils.game_part import Blackjack

import src
sys.path.append(src.__path__)


class TestDealer(unittest.TestCase):

    def setUp(self):
        """[summary]
        全てのテストの前に自動実行される準備用の関数
        """
        bj = Blackjack(11)
        dealer = Dealer()
        dealer.act(bj)
        self.onetime = dealer.sequence()

        bj = Blackjack(2)
        dealer = Dealer()
        dealer.act(bj)
        self.twotime = dealer.sequence()

    def test_evalate(self):
        self.assertRegex("♥6, ♦5, ♥5, ♥3", self.onetime)
        self.assertRegex("♥3, ♠4, ♦10", self.twotime)

import unittest

from src.utils.persons.dealer import Dealer
from src.utils.game_part import Blackjack


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
        self.assertEqual("♥6, ♦5, ♥5, ♥3", self.onetime)
        self.assertEqual("♥3, ♠4, ♦10", self.twotime)

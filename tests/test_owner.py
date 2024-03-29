import sys
import unittest

from src.utils.game_part import Blackjack
from src.utils.persons.owner import Owner

import src
sys.path.append(src.__path__)


class TestOwner(unittest.TestCase):

    def setUp(self):
        """[summary]
        全てのテストの前に自動実行される準備用の関数
        """
        bj = Blackjack(7)
        own = Owner()
        own.draw(bj)
        own.draw(bj)
        self.onetime = own.sequence()

        own.draw(bj)
        self.twotime = own.sequence()

    def test_evalate(self):
        self.assertEqual("♥5, ♣A", self.onetime)
        self.assertEqual("♥5, ♣A, ♠6", self.twotime)

import sys
import unittest

from utils.game_part import Blackjack
from utils.owner import Owner

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
        bj = Blackjack(7)
        own = Owner()
        own.draw(bj)
        own.draw(bj)
        self.onetime = own.sequence()

        own.draw(bj)
        self.twotime = own.sequence()

    def test_evalate(self):
        self.assertRegex("♥5, ♣A", self.onetime)
        self.assertRegex("♥5, ♣A, ♠6", self.twotime)

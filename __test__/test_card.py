import sys
import unittest

from utils.card import Card

sys.path.append('../../blackjack-for-console-python/src/utils')


class TestCard(unittest.TestCase):

    def test_evalate(self):
        self.assertRegex("♦A", f"{Card(0)}")
        self.assertRegex("♦2", f"{Card(1)}")
        self.assertRegex("♥A", f"{Card(13)}")

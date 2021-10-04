from src.utils.card import Card
import sys
import unittest

import src
sys.path.append(src.__path__)


class TestCard(unittest.TestCase):

    def test_evalate(self):
        self.assertRegex("♦A", f"{Card(0)}")
        self.assertRegex("♦2", f"{Card(1)}")
        self.assertRegex("♥A", f"{Card(13)}")

import unittest

from src.utils.card import Card


class TestCard(unittest.TestCase):

    def test_evalate(self):
        self.assertEqual("♦A", f"{Card(0)}")
        self.assertEqual("♦2", f"{Card(1)}")
        self.assertEqual("♥A", f"{Card(13)}")

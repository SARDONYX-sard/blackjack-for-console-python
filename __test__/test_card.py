import sys
import unittest

from utils.card import Card

import os
sys.path.append(
    os.path.join(
        os.path.abspath(
            os.path.dirname(__file__)),
        'utils/'))


class TestCard(unittest.TestCase):

    def test_evalate(self):
        self.assertRegex("♦A", f"{Card(0)}")
        self.assertRegex("♦2", f"{Card(1)}")
        self.assertRegex("♥A", f"{Card(13)}")

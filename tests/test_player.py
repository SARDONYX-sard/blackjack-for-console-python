import sys
import unittest

from src.utils.game_part import Blackjack
from src.utils.persons.player import Player

import src
sys.path.append(src.__path__)


class TestOwner(unittest.TestCase):

    def setUp(self):
        """[summary]
        全てのテストの前に自動実行される準備用の関数
        """
        bj = Blackjack(0)
        player = Player()
        commands = list('yyyn')
        player.ask_more_draw = lambda: commands.pop(0)
        player.act(bj)
        self.onetime = player.sequence()

        bj = Blackjack(3)
        player = Player()
        commands = list('yyyyyyyyn')
        player.ask_more_draw = lambda: commands.pop(0)
        player.act(bj)
        self.twotime = player.sequence()

        bj = Blackjack(4)
        player = Player()
        commands = list('yyyyn')
        player.ask_more_draw = lambda: commands.pop(0)
        player.act(bj)
        self.threetime = player.sequence()

    def test_evalate(self):
        self.assertEqual("♠3, ♦K, ♣7, ♣3", self.onetime)
        self.assertEqual("♥A, ♠3, ♦4, ♥7, ♠4, ♠A, ♣K", self.twotime)
        self.assertEqual("♠Q, ♥10, ♣A", self.threetime)

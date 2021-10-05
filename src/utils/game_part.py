import random

from .card import Card


class Blackjack:
    def __init__(self, seed: int):
        self.cards = [Card(i) for i in range(52)]
        random.seed(seed)
        random.shuffle(self.cards)

    def pop(self):
        return self.cards.pop(0)

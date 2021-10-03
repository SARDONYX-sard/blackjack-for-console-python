class Card:
    def __init__(self, num: int) -> None:
        self.suit = num // 13 + 1
        self.rank = num % 13 + 1

    def get_point(self):
        return min(10, self.rank)

    def __str__(self) -> str:
        suit = '♦♥♠♣'[self.suit - 1]
        rank = ["A", "2", "3", "4", "5", "6", "7", "8",
                "9", "10", "J", "Q", "K"][self.rank - 1]
        return suit + rank

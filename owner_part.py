from main_part import Blackjack


class Owner:
    def __init__(self):
        self.hands = []

    def draw(self, bj: Blackjack):
        self.hands.append(bj.pop())

    def sequence(self, hide=False):
        s = ''.join(str(cd) for cd in self.hands)
        return s[:2] + '＊＊' + s[4:] if hide else s


if __name__ == '__main__':
    bj = Blackjack(0)
    own = Owner()
    own.draw(bj)
    own.draw(bj)
    print(own.sequence())  # ♠⒊♦Ｋ
    print(own.sequence(True))  # ♠⒊＊＊

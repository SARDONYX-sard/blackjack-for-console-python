from main_part import Blackjack


class Owner:
    def __init__(self):
        self.hands = []

    def draw(self, bj):
        self.hands.append(bj.pop())

    def sequence(self, hide=False):
        s = ''.join(str(cd) for cd in self.hands)
        return s[:2] + '＊＊' + s[4:] if hide else s

    def point(self):
        pass  # ここを修正してください
        p = sum(cd.point() for cd in self.hands)
        for cd in self.hands:
            if cd.rank == 1 and p + 10 <= 21:
                p += 10
        return p


if __name__ == '__main__':
    bj = Blackjack(7)
    own = Owner()
    own.draw(bj)
    own.draw(bj)
    print(own.sequence(), own.point())  # ♥⒌♣Ａ 16
    own.draw(bj)
    print(own.sequence(), own.point(True))  # ♥⒌♣Ａ♠⒍ 12

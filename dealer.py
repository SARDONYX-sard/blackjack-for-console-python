from owner import Blackjack, Owner


class Dealer(Owner):
    def act(self, bj):
        while self.point() <= 16:
            self.draw(bj)


if __name__ == '__main__':
    bj = Blackjack(11)
    dealer = Dealer()
    dealer.act(bj)
    print(dealer.sequence())  # ♥⒍♦⒌♥⒌♥⒊
    bj = Blackjack(2)
    dealer = Dealer()
    dealer.act(bj)
    print(dealer.sequence())  # ♥⒊♠⒋♦⒑

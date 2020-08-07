from owner import Blackjack, Owner


class Player(Owner):
    def ask(self):
        print('もう一枚引く？(y/n)', end='')
        return input()

    def act(self, bj):
        while self.point() <= 20:
            bj.show(True)
            s = ''
            while s != 'y' and s != 'n':
                s = self.ask()
            if s == 'n':
                break
            self.draw(bj)


if __name__ == '__main__':
    bj = Blackjack(0)
    player = Player()
    commands = list('yyn')
    player.ask = lambda: commands.pop(0)
    player.act(bj)
    print(player.sequence())  # ♠⒊♦Ｋ
    bj = Blackjack(3)
    player = Player()
    commands = list('yyyyyyyyn')
    player.ask = lambda: commands.pop(0)
    player.act(bj)
    print(player.sequence())  # ♥Ａ♠⒊♦⒋♥⒎♠⒋♠Ａ♣Ｋ
    bj = Blackjack(4)
    player = Player()
    commands = list('yyyyn')
    player.ask = lambda: commands.pop(0)
    player.act(bj)
    print(player.sequence())  # ♠Ｑ♥⒑♣Ａ

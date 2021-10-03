from src.game import Blackjack

if __name__ == '__main__':
    while True:
        bj = Blackjack()  # 引数を変えると山札も変わります
        bj.start_game()
        print('-----------------------------------')

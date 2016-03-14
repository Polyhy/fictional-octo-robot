import re

order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
suit = ["S", "D", "H", "C"]


class PokerHand():
    card = []
    grade = 0
    highest = ''

    def __init__(self, name):
        self.name = name

    def set_card(self, card):
        self.card.append([re.split("([SDHC])", x)[0] for x in card])
        self.card.append([re.split("([SDHC])", x)[1] for x in card])


player1 = PokerHand('player1')
player2 = PokerHand('player2')
try:
    with open("poker_data.txt", "r") as poker_file:
        poker_datas = poker_file.read().split("\n")
        for poker_data in poker_datas:
            player1.set_card(poker_data.split()[:5])
            player2.set_card(poker_data.split()[5:])
            break
except IOError:
    print("poker_data.txt is Not Found")

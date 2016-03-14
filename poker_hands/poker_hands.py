import re

orders = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
suits = ["S", "D", "H", "C"]

ROYAL_FLUSH = 9
STRAIGHT_FLUSH = 8
FOUR_OF_KIND = 7
FULL_HOUSE = 6
FLUSH = 5
STRAIGHT = 4
THREE_OF_KIND = 3
TWO_PAIRS = 2
ONE_PAIRS = 1
HIGH_CARD = 0


class PokerHand():
    card = []
    grade = 0
    highest = ""
    sort_card = lambda self, card: [x for x in orders for y in card if y == x]

    def __init__(self, name):
        self.name = name

    def get_card_numbers(self, suit):
        card_place = [i for i, x in enumerate(self.card[1]) if x == suit]
        return [self.card[0][i] for i in card_place]

    def set_card(self, card):
        self.card.append([re.split("([SDHC])", x)[0] for x in card])
        self.card.append([re.split("([SDHC])", x)[1] for x in card])

    def royal_flush(self):
        for s in suits:
            if self.card[1].count(s) == 5:
                card_numbers = self.get_card_numbers(s)
                if self.sort_card(card_numbers) == ["A", "K", "Q", "J", "T"]:
                    self.highest = "A"
                    self.grade = ROYAL_FLUSH

    def straight_flush(self):
        return

    def of_kind(self):
        for x in self.sort_card(self.card[0]):
            if self.card[0].count(x) == 4:
                self.highest = x
                self.grade = FOUR_OF_KIND
                return
            elif self.card[0].count(x) == 3:
                self.highest = x
                for y in self.sort_card(self.card[0]):
                    if y != x and self.card[0].count(y) == 2:
                        self.grade = FULL_HOUSE
                self.grade = THREE_OF_KIND
                return
            elif self.card[0].count(x) == 2:
                self.highest = x
                for y in self.sort_card(self.card[0]):
                    if y != x and self.card[0].count(y) == 3:
                        self.grade = FULL_HOUSE
                        return
                for y in self.sort_card(self.card[0]):
                    if y != x and self.card[0].count(y) == 2:
                        self.grade = TWO_PAIRS
                        return
                    self.grade = ONE_PAIRS




player1 = PokerHand("player1")
player2 = PokerHand("player2")
try:
    with open("poker_data.txt", "r") as poker_file:
        poker_datas = poker_file.read().split("\n")
        for poker_data in poker_datas:
            player1.set_card(poker_data.split()[:5])
            player2.set_card(poker_data.split()[5:])

except IOError:
    print("poker_data.txt is Not Found")

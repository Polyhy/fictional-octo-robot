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
    card = [[], []]
    grade = 0
    highest = ""
    sort_card = lambda self, card: [x for x in orders for y in card if y == x]

    def get_card_numbers(self, suit):
        card_place = [i for i, x in enumerate(self.card[1]) if x == suit]
        return [self.card[0][i] for i in card_place]

    def set_card(self, card):
        self.card[0] = ([re.split("([SDHC])", x)[0] for x in card])
        self.card[1] = ([re.split("([SDHC])", x)[1] for x in card])
        functions = [self.royal_flush, self.straight_flush, self.four_of_kind,
                     self.full_house, self.flush, self.straight,
                     self.pairs, self.high_card]
        for f in functions:
            if f():
                break

    def royal_flush(self):
        for s in suits:
            if self.card[1].count(s) == 5:
                card_numbers = self.get_card_numbers(s)
                if self.sort_card(card_numbers) == ["A", "K", "Q", "J", "T"]:
                    self.highest = "A"
                    self.grade = ROYAL_FLUSH
                    return True

    def straight_flush(self):
        for s in suits:
            if self.card[1].count(s) == 5:
                if self.straight():
                    self.grade = STRAIGHT_FLUSH
                    return True

    def four_of_kind(self):
        for x in self.sort_card(self.card[0]):
            if self.card[0].count(x) == 4:
                self.highest = x
                self.grade = FOUR_OF_KIND
                return True

    def full_house(self):
        for x in self.sort_card(self.card[0]):
            if self.card[0].count(x) == 3:
                for y in self.sort_card(self.card[0]):
                    if y != x and self.card[0].count(y) == 2:
                        if orders.index(x) < orders.index(y):
                            self.highest = x
                        else:
                            self.highest = y
                        self.grade = FULL_HOUSE
                        return True

    def flush(self):
        for s in suits:
            if self.card[1].count(s) == 5:
                self.highest = self.sort_card(self.card[0])[0]
                self.grade = FLUSH
                return True

    def straight(self):
        ordered = self.sort_card(self.card[0])
        i = 5
        while i <= len(orders):
            temp = orders[i - 5:i]
            if ordered == temp:
                self.highest = temp[0]
                self.grade = STRAIGHT
                return True
            i += 1

    def pairs(self):
        for x in self.sort_card(self.card[0]):
            if self.card[0].count(x) == 3:
                self.highest = x
                self.grade = THREE_OF_KIND
                return True
            elif self.card[0].count(x) == 2:
                self.highest = x
                for y in self.card[0]:
                    if y != x and self.card[0].count(y) == 2:
                        self.grade = TWO_PAIRS
                        return True
                self.grade = ONE_PAIRS
                return True

    def high_card(self):
        self.grade = HIGH_CARD
        self.highest = self.sort_card(self.card[0])[0]


player1 = PokerHand()
player2 = PokerHand()
try:
    with open("poker_data.txt", "r") as poker_file:
        poker_datas = poker_file.read().split("\n")
        for poker_data in poker_datas:
            player1.set_card(poker_data.split()[:5])
            player2.set_card(poker_data.split()[5:])

except IOError:
    print("poker_data.txt is Not Found")

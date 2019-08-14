import logging


class Card():

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)8s:%(lineno)4s:%(filename)15s: '
        '%(message)s', datefmt='%Y%m%d %H:%M:%S',
    )

    def __init__(self, num, suit):
        self._num = num
        self._suit = str(suit).lower()

    def __repr__(self):
        return "Card('{}', '{}')".format(self.num, self.suit)

    def __str__(self):
        return "{}{}".format(self.num, self.suit)

    def __eq__(self, other):
        return isinstance(other, Card) and other.num == self.num \
            and other.suit == self.suit

    @property
    def short(self):
        return "{}{}".format(self.num, self.suit)

    @property
    def long(self):
        return "{} of {}".format(self.numLong, self.suitLong)

    @property
    def colour(self):
        if self._suit in ["h", "d"]:
            return "red"
        else:
            return "black"

    @property
    def numLong(self):
        valuesDict = {"A": "Ace", "K": "King", "Q": "Queen", "J": "Jack",
                      "T": "Ten", "9": "9", "8": "8", "7": "7", "6": "6",
                      "5": "5", "4": "4", "3": "3", "2": "2"}
        if str(self._num).capitalize() in valuesDict:
            return valuesDict.get(str(self._num).capitalize())
        else:
            return None

    @property
    def suitLong(self):
        if self._suit == 's':
            return "Spades"
        elif self._suit == 'h':
            return "Hearts"
        elif self._suit == 'd':
            return "Diamonds"
        elif self._suit == 'c':
            return "Clubs"
        else:
            return None

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if str(suit).lower() in ["s", "h", "d", "c"]:
            self._suit = str(suit).lower()
        else:
            print("Invalid suit")

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, num):
        values = ["A", "K", "Q", "J", "T", "9",
                  "8", "7", "6", "5", "4", "3", "2"]
        if str(num).capitalize() in values:
            self._num = str(num)
        else:
            print("Invalid number")


def main():
    c1 = Card("A", "s")
    print(repr(c1))
    print(c1)
    c1.suit = "h"
    c1.num = "k"
    print(c1)
    print(c1.colour)
    print(c1.suitLong)
    print(c1.numLong)
    print(c1.long)


if __name__ == "__main__":
    main()

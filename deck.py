from card import Card
import random
# from operator import attrgetter


class Deck():

    def __init__(self):
        self.cards = []
        self.create()

    def create(self):
        suits = ['s', 'h', 'd', 'c']
        numbers = ['A', 'K', 'Q', 'J', 'T', '9',
                   '8', '7', '6', '5', '4', '3', '2']
        self.cards = [Card(n, s) for n in numbers for s in suits]

    @property
    def shuffleCards(self):
        return random.shuffle(self.cards)

    @property
    def printCards(self):
        for card in self.cards:
            print(card, end=" ")
        print("")

    @property
    def sortCards(self):
        order = "AKQJT98765432"
        order2 = "shdc"
        s_cards = sorted(self.cards, key=lambda Card:
                         (order.index(Card.num), order2.index(Card.suit)))
        self.cards = s_cards

    @property
    def removeCard(self):
        if len(self.cards) > 0:
            return self.cards.pop()


class Hand(Deck):

    def __init__(self):
        self.handFolded = False
        self.cards = []
        self.deck = Deck
        self.owner = ''

    def addHand(self, Deck):
        self.cards = []

    # @property
    def dealSingleCard(self, Deck):
        if not self.handFolded:
            card = Deck.removeCard
            if card:
                self.cards.append(card)
            else:
                print("no cards in deck to deal")

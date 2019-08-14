from card import Card
from collections import Counter
from operator import attrgetter
import random

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)8s:%(lineno)4s:%(filename)15s: '
    '%(message)s', datefmt='%Y%m%d %H:%M:%S',)


class Deck():

    order = "23456789TJQKA"
    order2 = "cdhs"

    def __init__(self):
        self.cards = []
        self.create()
        self.activeHands = 0

    def create(self):
        numbers = list(self.order)
        suits = list(self.order2)
        self.cards = [Card(n, s) for n in numbers for s in suits]

    @property
    def shuffleCards(self):
        return random.shuffle(self.cards)

    # @property
    # def printCards(self):
    #     for n, card in enumerate(self.cards):
    #         print(card, end=" ")
    #     if n < 5:
    #         for _ in range(5-n):
    #             print("  ", end=" ")
    #     print(f" - {self.handName:<14} - {self.value:>7}")

    @property
    def sortCards(self):
        s_cards = sorted(self.cards, key=lambda Card:
                         (self.order.index(Card.num),
                          self.order2.index(Card.suit)), reverse=True)
        self.cards = s_cards

    @property
    def removeCard(self):
        if len(self.cards) > 0:
            return self.cards.pop()

    def removeSpecificCard(self, namedCard):
        if len(self.cards) > 0:
            obj = Card(namedCard[:1], namedCard[1:])
            try:
                cardPosition = self.cards.index(obj)
                returnedCard = self.cards[cardPosition]
                self.cards.remove(returnedCard)
                return returnedCard
            except:
                logging.error(f"{obj.long} not in deck")
                return None


class Hand(Deck):

    def __init__(self, parentDeck):
        self.handFolded = False
        self.cards = []
        self.deck = Deck
        self.parent = parentDeck
        self.owner = ''
        self.seat = 0
        self.handPosition = 0
        self.value = 0
        self.handName = ''
        parentDeck.activeHands += 1

    def __eq__(self, other):
        return isinstance(other, Hand) and other.value == self.value

    def __gt__(self, other):
        return isinstance(other, Hand) and self.value > other.value

    @property
    def printCards(self):
        for n, card in enumerate(self.cards):
            print(card, end=" ")
        if n < 5:
            for _ in range(5-n):
                print("  ", end=" ")
        print(f" - {self.handName:<14} - {self.value:>7}")

    @property
    def foldHand(self):
        self.handFolded = True
        self.parent.activeHands -= 1

    def createHandsFromList(self, parentDeck, players):
        hands = []
        for n, _ in enumerate(players):
            hands.append(Hand(parentDeck))
            hands[n].owner = players[n]
            hands[n].seat = n+1
            hands[n].handPosition = n+1
        return hands

    @property
    def dealSingleCard(self):
        if not self.handFolded:
            card = self.parent.removeCard
            if card:
                self.cards.append(card)
                if len(self.cards) > 4:
                    self.calculateHandValues
            else:
                print("no cards in deck to deal")

    def dealSpecificCard(self, namedCard):
        if not self.handFolded:
            card = self.parent.removeSpecificCard(namedCard)
            if card:
                # logging.debug(f"dealing {namedCard}")
                self.cards.append(card)
                if len(self.cards) > 5:
                    logging.warning(f"Dealing {len(self.cards)} cards")
                    pass
                    # self.calculateHandValue

    def dealRound(self, handList, numCards):
        # Make sure there is at least 1 hands that has not folded
        if handList[0].parent.activeHands < 1:
            return
        # find a hand that is not folded to be used to make
        # sure there are enough cards left.
        for k in range(len(handList)):
            if not handList[k].handFolded:
                break
        # Make sure there are enough cards left and then deal them
        for _ in range(numCards):
            if len(handList[k].parent.cards) >= handList[k].parent.activeHands:
                for j in range(len(handList)):
                    handList[j].dealSingleCard

    def calculateHandValues(self, handList):
        for h1 in handList:
            h1.calculateHandValue

    @property
    def calculateHandValue(self):
        # High Card, 1-Pair, 2-2 Pairs, 3-Trips, 4-Straight, 5-Flush
        # 6-Full house, 7-Quads, 8-Straight Flush 9-Royal Flush
        if self.handFolded:
            self.value = 0
            self.handName = 'Folded'
            return

        straight = False
        flush = False
        currentHandName = ''
        currentValue = 0

        self.sortCards
        numCtr = Counter(getattr(Card, 'num') for Card in self.cards)
        suitCtr = Counter(getattr(Card, 'suit') for Card in self.cards)
        # logging.debug(numCtr)

        if 4 in numCtr.values():
            currentValue = 7000000
            currentHandName = '4 of a Kind'
            # TODO: Check eval of last card
        elif 3 in numCtr.values():
            if 2 in numCtr.values():
                value1 = list(numCtr.keys())[list(numCtr.values()).index(3)]
                value2 = list(numCtr.keys())[list(numCtr.values()).index(2)]
                position1 = Hand.order.find(value1)
                position2 = Hand.order.find(value2)
                currentValue = 6000000 + 12*position1 + position2
                currentHandName = 'Full House'
            else:
                currentValue = 3000000
                currentHandName = '3 of a Kind'
        elif 2 in numCtr.values():
            if len(self.cards)-2 == len(numCtr):
                currentValue = 2000000
                currentHandName = '2 Pairs'
            else:
                currentValue = 1000000
                currentHandName = '1 Pair'

        # Flush
        if len(suitCtr) == 1 and len(self.cards) == 5:
            currentValue = 5000000
            currentHandName = 'Flush'
            flush = True
            # TODO: check eval of cards

        # Straight & straight flush
        if len(numCtr) == 5:
            # print(self.cards)
            straight = False
            minNum = min(Deck.order.index(x) for x in numCtr.keys())
            maxNum = max(Deck.order.index(x) for x in numCtr.keys())
            if int(maxNum)-int(minNum) == 4:
                straight = True
            else:
                lowStraight = set(('A', '2', '3', '4', '5'))
                if not set(numCtr.keys()).difference(lowStraight):
                    straight = True
            if straight and flush:
                currentValue = 8000000 + minNum
                currentHandName = 'Straight Flush'
                royal = set(('T', 'J', 'Q', 'K', 'A'))
                if not set(numCtr.keys()).difference(royal):
                    currentValue = 9000000
                    currentHandName = 'Royal Flush'
            elif straight:
                currentValue = 4000000 + minNum
                currentHandName = 'Straight'

        # Check for remaining non ranked cards
        if not straight and currentHandName != 'Full House':
            used = 0
            if currentValue < 1000000:
                currentHandName = 'No Pair'
            for _, i in enumerate(self.cards):
                if numCtr[i.num] != 1:
                    position = Hand.order.find(i.num)
                    value = 12**(4-used) * position
                    # logging.debug(
                    #     f"{i.num} = {position} = {n} = {4-used} = {value}")
                    currentValue += value
                    used += 1
            for _, i in enumerate(self.cards):
                if numCtr[i.num] == 1:
                    position = Hand.order.find(i.num)
                    value = 12**(4-used) * position
                    # logging.debug(
                    #     f"{i.num} = {position} = {n} = {4-used}= {value}")
                    currentValue += value
                    used += 1

        # Check if hand highest so far
        if currentValue >= self.value:
            self.value = currentValue
            self.handName = currentHandName

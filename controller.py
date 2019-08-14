from card import Card
from deck import Deck
from deck import Hand

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)8s:%(lineno)4s:%(filename)15s: %(message)s',
    datefmt='%Y%m%d %H:%M:%S',
)


def printCurrentStandings(myHands, players):
    for i in players:
        x = len(players)

    maxNameLen = max([len(i) for i in players])
    for n, i in enumerate(players):
        # myHands[n].sortCards
        print(f"{n+1:>2}", end='  ')
        print("{msg1:>2}  {msg2:<{width}}".format(msg1=myHands[n].ordinal,
                                                  msg2=myHands[n].owner, width=maxNameLen+2), end=' ')
        myHands[n].printCards
    print("------------------------------------------------------")


def main():
    myDeck = Deck()
    myDeck.shuffleCards

    players = ["Peter", "John", "David", "Ford", "Derrick",
               "Darcy", "Jim", "Joyce", "Joanne", "Ruth"]
    myHands = Hand.createHandsFromList(Hand, myDeck, players)

    Hand.dealRound(Hand, myHands, 5)

    Hand.calculateHandValues(Hand, myHands)
    myHands.sort(key=lambda x: x.value, reverse=True)
    printCurrentStandings(myHands, players)

    # print(myHands[2] > myHands[n])

    # Hand.printCards

    # logging.debug(f"{len(myDeck.cards)} cards left in the deck")
    # myDeck.printCards

    # h1.dealSingleCard(myDeck)
    # h1.dealSingleCard(myDeck)
    # h1.dealSingleCard(myDeck)
    # h1.dealSingleCard(myDeck)
    # h1.sortCards
    # h1.printCards
    # print(len(myDeck.cards))
    # print(len(h1.cards))


if __name__ == "__main__":
    main()

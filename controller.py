from card import Card
from deck import Deck
from deck import Hand

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)8s:%(lineno)4s:%(filename)15s: '
    '%(message)s', datefmt='%Y%m%d %H:%M:%S',
)


def printCurrentStandings(myHands, players):
    maxNameLen = max([len(i) for i in players])
    print("Rnk Seat {msg1:<{width}} Cards                   Hand"
          "             Score".format(msg1="Name", width=maxNameLen+2))
    for n, _ in enumerate(players):
        # myHands[n].sortCards
        print(f"{n+1:>2}", end='   ')
        print("{msg1:>2}  {msg2:<{width}}"
              .format(msg1=myHands[n].seat,
                      msg2=myHands[n].owner,
                      width=maxNameLen+2), end=' ')
        myHands[n].printCards
    print("------------------------------------------------------")


def main():
    myDeck = Deck()
    myDeck.shuffleCards

    players = ["Peter", "John", "David", "Ford", "Derrick",
               "Darcy", "Jim"]  # , "Joyce", "Joanne", "Ruth"]
    myHands = Hand.createHandsFromList(Hand, myDeck, players)

    Hand.dealRound(Hand, myHands, 3)
    # myHands[2].foldHand
    Hand.dealRound(Hand, myHands, 4)

    # Hand.calculateHandValues(Hand, myHands)
    myHands.sort(key=lambda x: x.value, reverse=True)
    printCurrentStandings(myHands, players)

    # players = ["Player 1", "Player 2", "Player 3"]
    # myHands = Hand.createHandsFromList(Hand, myDeck, players)
    # Hand.dealSpecificCard(myHands[0], 'Ac')
    # Hand.dealSpecificCard(myHands[0], '2c')
    # Hand.dealSpecificCard(myHands[0], '3c')
    # Hand.dealSpecificCard(myHands[1], '9c')
    # Hand.dealSpecificCard(myHands[1], '9h')
    # Hand.dealSpecificCard(myHands[1], 'Kd')
    # Hand.dealSpecificCard(myHands[2], '9d')
    # Hand.dealSpecificCard(myHands[2], '9s')
    # Hand.dealSpecificCard(myHands[2], 'Ad')
    # Hand.calculateHandValues(Hand, myHands)
    # myHands.sort(key=lambda x: x.value, reverse=True)
    # printCurrentStandings(myHands, players)


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

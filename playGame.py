from card import Card
from deck import Deck
from deck import Hand
import game

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)8s:%(lineno)4s:%(filename)15s: '
    '%(message)s', datefmt='%Y%m%d %H:%M:%S',
)


def main():
    players = ["Peter", "John", "David", "Ford", "Derrick",
               "Darcy", "Jim", "Joyce", "Joanne", "Ruth"]
    myGame = game.Holdem(players)
    myDeck = Deck(myGame)
    myHands = Hand.createHandsFromList(Hand, myDeck, myGame.players)
    communityHand = Hand(myDeck)
    print(myGame.players)


if __name__ == "__main__":
    main()

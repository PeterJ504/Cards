from card import Card
from deck import Deck
from deck import Hand
import game
import sys

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)8s:%(lineno)4s:%(filename)15s: '
    '%(message)s', datefmt='%Y%m%d %H:%M:%S',
)


def printCurrentStandings(game, hands, community):
    maxNameLen = max([len(i) for i in game.players])
    maxNameLen = 9 if maxNameLen < 9 else maxNameLen
    print(f"\nCurrent standings - {game.gameName}")
    print("Rnk Seat {msg1:<{width}} Cards                  Hand"
          "               Score".format(msg1="Name", width=maxNameLen + 2))
    if game.useCommunity:
        print("         {msg1:<{width}}".format(
            msg1="Community", width=maxNameLen + 1), end='  ')
        community.printCards
    for n, _ in enumerate(game.players):
        # myHands[n].sortCards
        print(f"{n+1:>2}", end='   ')
        print("{msg1:>2}  {msg2:<{width}}"
              .format(msg1=hands[n].seat,
                      msg2=hands[n].owner,
                      width=maxNameLen + 2), end=' ')
        hands[n].printCards
    print("------------------------------------------------------")


def playGame(myGame):
    print(f"The game is {myGame.gameName}")
    myDeck = Deck(myGame)
    myDeck.shuffleCards

    myHands = Hand.createHandsFromList(Hand, myDeck, myGame.players)
    communityHand = Hand(myDeck)

    # Deal each round
    for rnd in myGame.rounds:
        if isinstance(rnd[0], list):
            for subrnd in rnd:
                if subrnd[1] == 'c':
                    Hand.dealCommunityCards(Hand, myHands,
                                            communityHand, subrnd[0])
                elif subrnd[1] == 'u' or subrnd[1] == 'd':
                    Hand.dealRound(Hand, myHands, subrnd[0])
                else:
                    pass
                    # TODO - code for draw
        else:
            if rnd[1] == 'c':
                Hand.dealCommunityCards(Hand, myHands,
                                        communityHand, rnd[0])
            elif rnd[1] == 'u' or rnd[1] == 'd':
                Hand.dealRound(Hand, myHands, rnd[0])
            else:
                pass
                # TODO - code for draw
    Hand.calculateHandValues(Hand, myHands, communityHand, myGame)
    myHands.sort(key=lambda x: x.value, reverse=True)
    printCurrentStandings(myGame, myHands, communityHand)
    input("Press Enter to continue...")


def main():
    allPlayers = ["Peter", "John", "David", "Ford", "Derrick",
                  "Darcy", "Jim", "Joyce", "Joanne", "Ruth"]

    # Create a list of all games available
    allGames = []
    gamesList = game.Game.__subclasses__()
    for xGame in gamesList:
        allGames.append(xGame)
        subGamesList = xGame.__subclasses__()
        for xxGame in subGamesList:
            allGames.append(xxGame)

    # List all games
    # for item in allGames:
    #     print(item.gameName)
    # sys.exit()

    # Play each game according to the rules
    for item in allGames:
        players = allPlayers[:item.maxPlayers]
        newGame = item(players)
        playGame(newGame)
    sys.exit()

    # myGame = game.Stud7(allPlayers)
    # playGame(myGame)
    # sys.exit()

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


class Game():

    gameName = 'Poker'
    minPlayers = 2
    maxPlayers = 10
    rounds = [(5, 'd')]
    currentRound = 0
    useCommunity = False
    useDraws = False
    useJokers = False
    scoreHigh = True
    scoreLow = False
    minHandToScore = 5
    maxHandToScore = 5
    showDownCards = False
    players = []

    def __init__(self, players):
        self.players = players
        # self.deck = Deck(self)
        self.createGame(players)

    def __str__(self):
        """Not implemented yet"""
        pass

    @property
    def gameDescription(self):
        """Prints a description of the game selected"""

        print(self.gameName)
        print(
            f"{self.minPlayers} to {self.maxPlayers} players",
            "using a single deck of cards", end=' ')
        if self.useJokers:
            print("plus 2 jokers).")
        else:
            print("(no jokers).")
            if self.bettingRounds == 1:
                print(f"There is {self.bettingRounds} betting round:")
            else:
                print(f"There are {self.bettingRounds} betting rounds:")

            desc = {"u": "face up", "d": "face down",
                    "c": "community face up", "x": "(max) discarded and redrawn"}
            for n, item in enumerate(self.rounds):
                if isinstance(item[0], list):
                    print(f"  {n+1} - ", end='')
                    for y, subitem in enumerate(item):
                        print(
                            f"{subitem[0]} {desc.get(subitem[1], None)}",
                            end=' ')
                        if y + 1 < len(item):
                            print(f"and", end=' ')
                    print()
                else:
                    print(f"  {n+1} - {item[0]} {desc.get(item[1], None)}")
            if self.useCommunity:
                if self.minHandToScore == self.maxHandToScore:
                    print(
                        f"Use exactly {self.minHandToScore} cards plus {5-self.minHandToScore} community cards make the best 5 card hand(s)")
                else:
                    print(
                        f"Use {self.minHandToScore} to {self.maxHandToScore} cards"
                        " plus community cards to make the best 5 card hand(s)")
            if self.scoreLow:
                if self.scoreHigh:
                    print("Pot is split between best high and low hands.", end=' ')
                else:
                    print("Low hand wins.", end=' ')
                print("Straights do not count for low hands.")
            else:
                print("High hand wins.")

    @property
    def bettingRounds(self):
        return len(self.rounds)

    def createGame(self, players):
        pass


class DrawPoker(Game):
    gameName = 'Draw Poker (1 draw of 3)'
    maxPlayers = 6
    useDraws = True
    rounds = [[5, 'd'], [3, 'x']]


class Holdem(Game):
    gameName = "Texas Hold'em"
    useCommunity = True
    rounds = [[2, 'd'], [3, 'c'], [1, 'c'], [1, 'c']]
    minHandToScore = 0


class Lowball(Game):
    gameName = 'Lowball'
    useCommunity = True
    scoreHigh = False
    scoreLow = True
    rounds = [[2, 'd'], [3, 'c'], [1, 'c'], [1, 'c']]
    minHandToScore = 0


class OmahaHi(Game):
    gameName = 'Omaha (high)'
    useCommunity = True
    minHandToScore = 2
    maxHandToScore = 2
    rounds = [[4, 'd'], [3, 'c'], [1, 'c'], [1, 'c']]


class OmahaHiLo(OmahaHi):
    gameName = 'Omaha (high/low)'
    scoreLow = True


class Stud5(Game):
    gameName = '5 Card Stud'
    rounds = [[[1, 'd'], [1, 'u']], [1, 'u'], [1, 'u'], [1, 'u']]


class Stud7(Game):
    gameName = '7 Card Stud'
    maxPlayers = 7
    rounds = [[[2, 'd'], [1, 'u']], [1, 'u'], [1, 'u'], [1, 'u'], [1, 'd']]

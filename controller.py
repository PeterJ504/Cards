from card import Card
from deck import Deck, Hand


def main():
    myDeck = Deck()
    # print(len(myDeck.cards))
    # myDeck.printCards
    myDeck.shuffleCards
    # myDeck.printCards
    # myDeck.sortCards
    # myDeck.printCards
    hand = []
    players = ["Peter", "John", "David", "Jim", "Ford",
               "Joyce", "Joanne", "Ruth"]
    for n, i in enumerate(players):
        hand.append(Hand())
        hand[n].owner = players[n]
    for i in range(7):
        if len(myDeck.cards) >= len(players):
            for n, i in enumerate(players):
                # hand[n].cards=hand[n].dealSingleCard(myDeck)
                hand[n].dealSingleCard(myDeck)

    print(len(hand[0].cards))
    max_len = max([len(i) for i in players])
    blankStr = "                                              "
    for n, i in enumerate(players):
        hand[n].sortCards
        end_str_len = max_len + 2 - len(hand[n].owner)
        xStr = blankStr[:end_str_len]
        print(hand[n].owner, end=xStr)
        hand[n].printCards

    print(f"{len(myDeck.cards)} cards left in the deck")
    myDeck.printCards

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

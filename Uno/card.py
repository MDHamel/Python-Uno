from random import shuffle

class Card:
    color = None
    value = None

    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return self.color + " " + self.value

    def effect(self):
        pass


class Deck:
    cardList = []

    def __init__(self):
        for i in range(10):
            self.cardMaker(str(i))

        self.cardMaker("Card") #Wild card
        self.cardMaker("+4 Card") #wild +4
        self.cardMaker("Skip")
        self.cardMaker("+2 Card")
        self.cardMaker("Reverse")

        for n in range(500):
            shuffle(self.cardList)

    def cardMaker(self, value):
        count = 2 # x 4
        colors = ["Red", "Green", "Blue", "Yellow"]
        if value == "Card" or value == "+4 Card":
            colors = ["Wild", "Wild", "Wild", "Wild"]
            count = 1
        elif value == "0":
            count = 1

        for i in range(count):
            for color in colors:
                c = Card(color, value)
                self.cardList.append(c)

    def draw(self):
        return self.cardList.pop(0)


class Player:
    playerNumber = 0
    hand = []

    def __init__(self, playerNumber):
        self.hand = []
        self.playerNumber = playerNumber

    def addToHand(self, card):
        self.hand.append(card)

    def __str__(self):
        display = "Player " + str(self.playerNumber) + " Hand: \n"

        for n in range(len(self.hand)):
            display += "[" + str(n) + "] " + str(self.hand[n]) + "  "

        return display

    def playCard(self, index):
        return self.hand.pop(index)


d = Deck()
for c in d.cardList:
    print(c)
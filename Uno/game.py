from card import Deck, Player

deck = Deck()
cardInPlay = None
players = []
currentPlayerIndex = 0
direction = 1
skipMod = 1

for n in range(4):
    players.append(Player(n))

for m in range(7):
    players[0].addToHand(deck.draw())
    players[1].addToHand(deck.draw())
    players[2].addToHand(deck.draw())
    players[3].addToHand(deck.draw())

cardInPlay = deck.draw()

winner = False

def nextPlayerHandler():
    global currentPlayerIndex, skipMod, direction

    num = currentPlayerIndex + direction * skipMod

    if num > 3:
        return num - 4
    elif num < 0:
        return num + 4
    else:
        return num


while not winner:
    ###display the players layout and play card

    skipMod = 1
    choice = -1
    currentPlayer = players[currentPlayerIndex]

    while choice == -1:

        hasPlayableCard = False

        for card in currentPlayer.hand:
            if card.color == cardInPlay.color or card.value == cardInPlay.value or card.color == "Wild":
                hasPlayableCard = True
                break

        print("The card in play: " + str(cardInPlay))
        print(str(currentPlayer))

        if hasPlayableCard:
            choice = int(input("Select a card number: "))

            #TODO: check if player has that card or is out of range

            playerCard = players[currentPlayerIndex].playCard(choice)

            if playerCard.color == cardInPlay.color or playerCard.value == cardInPlay.value or playerCard.color == "Wild":
                cardInPlay = playerCard
                playerCard = None
                break
            else:
                print("Card not playable, select again")
                players[currentPlayerIndex].addToHand(playerCard)
        else:
            while not hasPlayableCard:
                drawnCard = deck.draw()
                print("Player " + currentPlayer.playerNumber + " does not have a usable card, drawing from deck: " + str(drawnCard))
                if drawnCard.color == cardInPlay.color or drawnCard.value == cardInPlay.value or drawnCard.color == "Wild":
                    print("Player plays the drawn card")
                    cardInPlay = drawnCard
                    hasPlayableCard = True
                    choice = -2
                else:
                    currentPlayer.addToHand(drawnCard)


    #card has been played, next to determine special effects
    if cardInPlay.value == "Reverse":
        direction *= -1
    elif cardInPlay.value == "Skip":
        skipMod = 2
    elif cardInPlay.value == "+2 Card":
        players[nextPlayerHandler()].addToHand(deck.draw())
        players[nextPlayerHandler()].addToHand(deck.draw())
        skipMod = 2
    elif cardInPlay.value == "+4 Card":
        for i in range(4):
            players[nextPlayerHandler()].addToHand(deck.draw())
        skipMod = 2
    if cardInPlay.color == "Wild":
        color = False
        while not color:
            color = input("Change color to Red, Green, Blue, or Yellow: ")
            if color.lower()[0] == "r":
                cardInPlay.color = "Red"
            elif color.lower()[0] == "g":
                cardInPlay.color = "Green"
            elif color.lower()[0] == "b":
                cardInPlay.color = "Blue"
            elif color.lower()[0] == "y":
                cardInPlay.color = "Yellow"
            else:
                print("Not a valid color, try again")
                color = False

    #currentPlayer -> players[currentPlayerIndex]
    if(len(currentPlayer.hand) == 1):
        print("UNO!\nPlayer " + currentPlayer.playerNumber + " has 1 card left!")
    elif(len(currentPlayer.hand) == 0):
        winner = currentPlayer
        print("Player " + winner.playerNumber + " Wins!")

    #end of turn phase, increment order
    currentPlayerIndex = nextPlayerHandler()


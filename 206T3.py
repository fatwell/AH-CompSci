#fatwell
#206T4
#8/9/25
SuitRankings = ["Spades", "Hearts", "Diamonds", "Clubs"]
myCards = ['1 Spades', '13 Hearts', '1 Clubs', '10 Diamonds', '5 Hearts', '5 Diamonds']

def SortCards(Cards, Rankings):
    for index in range(1, len(Cards)):
        currentvalue = Cards[index]
        position = index
        if position > 0 and Cards[position-1].split()[0] == currentvalue.split()[0]:
            Suit1 = Cards[position-1].split()[1]
            Suit2 = currentvalue.split()[1]
            if Rankings.index(Suit1) > Rankings.index(Suit2):
                Cards[position] = Cards[position-1]
                position -= 1

        while position > 0 and int(Cards[position-1].split()[0]) > int(currentvalue.split()[0]):
            Cards[position] = Cards[position-1]
            position -= 1

        Cards[position] = currentvalue
    return Cards

mySortedCards = SortCards(myCards, SuitRankings)
print(mySortedCards)


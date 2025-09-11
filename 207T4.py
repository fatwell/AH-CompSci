#fatwell
#207T4 - BubbleSort Questions
#10/9/25

SuitRankings = ["Spades", "Hearts", "Diamonds", "Clubs"]
myCards = ['1 Spades', '13 Hearts', '1 Clubs', '10 Diamonds', '5 Hearts', '5 Diamonds']


def BubbleSortCards(myList, Rankings):
    for outer in range (len(myList)-1,0,-1):
     for inner in range(outer):
        if int(myList[inner].split()[0]) > int(myList[inner+1].split()[0]):
           temp = myList[inner]
           myList[inner] = myList[inner+1]
           myList[inner+1] = temp
        if int(myList[inner].split()[0]) == int(myList[inner+1].split()[0]):
            Suit1 = myList[inner].split()[1]
            Suit2 = myList[inner-1].split()[1]
            if Rankings.index(Suit1) > Rankings.index(Suit2):
                temp = myList[inner]
                myList[inner] = myList[inner+1]
                myList[inner+1] = temp 
    return myList

           
mySortedCards = BubbleSortCards(myCards, SuitRankings)
print(mySortedCards)
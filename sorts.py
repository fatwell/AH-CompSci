#sorts
#fatwell
#4/9/25
import random 
Numbers = []

for i in range(6):
    number = random. randint(0,10)
    Numbers.append(number)

def Bubble(listA):
    swaps = True
    outer = len(listA)-1
    while (swaps == True):
        swaps = False
        for inner in range(outer):
            if listA[inner]>listA[inner+1]:
                swaps = True
                temp = listA[inner]
                listA[inner] = listA[inner+1]
                listA[inner+1] = temp      
        outer -= 1

def Insertion(list):
    print(list)
    for i in range(6):
        currentVal = list[i]
        position = i   
        while position > 0 and list[position - 1] > currentVal:
            list[position] = list[position - 1]
            position -= 1
        list[position] = currentVal
    return list


Numbers = Bubble(Numbers)
print(Numbers)

#If you want to go in reverse order, a line like "for outer in range (len(array)-1,0,-1):", making the list go in reverse (the last comma is used to show instead of i += 1 at the end of every loop it is i -=1)
# the ",-1" is setting the step to minus 1
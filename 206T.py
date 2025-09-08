#fatwell
#206T2
#8/9/25

myList = [3,4,9,7,1]
passes = 0
for index in range (1,len(myList)):

 currentvalue = myList[index]
 position = index

 while position > 0 and myList[position-1]<currentvalue:
   myList[position] = myList[position-1]
   position -= 1
   passes = passes + 1
 myList[position] = currentvalue


print(myList, passes)
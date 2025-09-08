#fatwell
#206T3
#8/9/25

myLetterList = ['p','o','r','t','y']
passes = 0
for index in range (1,len(myLetterList)):

 currentvalue = myLetterList[index]
 position = index

 while position > 0 and ord(myLetterList[position-1])>ord(currentvalue):
   myLetterList[position] = myLetterList[position-1]
   position -= 1
   passes = passes + 1
 myLetterList[position] = currentvalue


print(myLetterList, passes)
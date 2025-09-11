#fatwell
#207T1 - BubbleSort Questions
#10/9/25

myList = ["p","o","r","t","y"]
passes = 0

for outer in range (len(myList)-1,0,-1):
 for inner in range(outer):
   if ord(myList[inner])>ord(myList[inner+1]):
     temp = myList[inner]
     myList[inner] = myList[inner+1]
     myList[inner+1] = temp
     passes += 1
  
print("Bubble sort complete in", passes, "passes")
print(myList)


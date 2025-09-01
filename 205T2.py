#205T2
#Fatwell
#1/9/25

def initialise():
 searchlist = [90,90,91,92,92,93,1000]
 print("Original list:",searchlist)
 return searchlist


def BinarySearch(searchlist,goal):
 found = False
 startpos = 0
 endpos = len(searchlist) -1
 counter = 0

 print ("Endpos at beginning = ",endpos)

 while (startpos <= endpos) and found == False:
     middle = (startpos+endpos)//2 #Integer Division
     if searchlist[middle] == goal:
         found = True
     elif searchlist[middle]<goal:
         startpos = middle + 1
     else:
         endpos = middle -1
     counter = counter + 1

 if found == False:
    middle = -1

 if found == True:
   print("Match has been found at position",middle)
   print("The target was found in", counter, "iterations")
 else:
   print("Goal not found")


values = initialise()


goal = int(input("Enter goal: "))
BinarySearch(values,goal)

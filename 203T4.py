#fatwell
#26/8/25
#203T4

from dataclasses import dataclass

@dataclass
class node():
  data : str = ''
  nextptr : int = -1

fat = [node() for x in range(12)]
headptr = 5 # position of first colour 

fat[1].data = 'Yellow'
fat[2].data = 'Indigo'
fat[4].data = 'Violet'
fat[5].data = 'Red'
fat[6].data = 'Orange'
fat[10].data = 'Green'
fat[11].data = 'Blue'

fat[5].nextptr = 6
fat[6].nextptr = 1
fat[1].nextptr = 10
fat[10].nextptr = 11
fat[11].nextptr = 2
fat[2].nextptr = 4
fat[4].nextptr = -1

print("headptr : ",headptr)
for x in range(12):
  print(x,": ",fat[x].data, "-> ",fat[x].nextptr)

# Process linked list
nextptr = headptr
while nextptr != -1:
  data = fat[nextptr].data
  nextptr = fat[nextptr].nextptr
  print(data)

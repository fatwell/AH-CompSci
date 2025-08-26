#fatwell
#26/8/25
#203T5

from dataclasses import dataclass

@dataclass
class node():
  data : str = ''
  nextptr : int = -1

fat = [node() for x in range(710)]
headptr = 318 # position of first colour 

fat[318].data = 'Australia'
fat[706].data = 'France'
fat[153].data = 'USA'
fat[241].data = 'Germany'
fat[439].data = 'UK'
fat[208].data = 'Brazil'

fat[318].nextptr = 706
fat[706].nextptr = 153
fat[153].nextptr = 67
fat[241].nextptr = 439
fat[439].nextptr = 208
fat[208].nextptr = -1

#Addition
fat[67].data = 'Russia'
fat[67].nextptr = 241

# Process linked list
nextptr = headptr
while nextptr != -1:
  data = fat[nextptr].data
  nextptr = fat[nextptr].nextptr
  print(data)

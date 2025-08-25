#25/8/25
#Lesson 203T - programming tasks
#fatwell

from dataclasses import dataclass 
@dataclass
class customer:
    FullName: str = ''
    rowLetter: str = ''
    seatNumber: int = 0.0

CinemaCustomers = [customer() for i in range(5)]

CinemaCustomers[0].FullName = "Finlay Atwell"
CinemaCustomers[0].seatNumber = 5
CinemaCustomers[0].rowLetter = "C"

print(CinemaCustomers[0])



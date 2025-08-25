#25/8/25
#Lesson 203T - programming task 2
#fatwell

class BuyTicket:
    def __init__(self):
        self.Fullname = ""
        self.seat = ""
        self.MovieName = ""
        self.MovieTime = ""

    def GetSeat(self):
        return self.seat

    def SetSeat(self, newSeat):
        self.seat = newSeat

    def GetName(self):
        return self.Fullname

    def SetName(self,newName):
        self.Fullname = newName

    def GetMovie(self):
        return self.MovieName
    
    def SetMovie(self, newMovie):
        self.MovieName = newMovie

    def GetMovieTime(self):
        return self.MovieTime

    def SetMovieTime(self, newMovieTime):
        self.MovieTime = newMovieTime
        
customers = [BuyTicket() for i in range(5)]

customers[0].SetMovie("TASM 2")
customers[0].SetName("Fin Atwell")
customers[0].SetMovieTime("12:00")
customers[0].SetSeat("C4")


#using "Get" to show (print is cheating)

def showCustomer(number):
    print(customers[number].GetName())
    print(customers[number].GetSeat())
    print(customers[number].GetMovie())
    print(customers[number].GetMovieTime())


showCustomer(0)
        
    


    


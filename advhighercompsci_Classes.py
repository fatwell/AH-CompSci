#Advanced higher CompSci
#Fatwell
#Classes

class person():
    def __init__(self): #init (initiate) and underscores is the contstructor
        self.name = "Fin" #String
        self.age = 16 #Integer
        self.FavColour = "White" #String

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getColour(self):
        return self.colour

    def setName(self, newName):
        self.name = newName

#outside of class definition
people = [person() for x in range(10)]
#dont do this as it is meant to be private: print(people[0].name) - its cheating

#print(people[0].getName()) -The right way to do above

        
for x in range(3):
    newName = input("What is your new name?")
    people[x].setName(newName)
    
print(people[0].getName())


#no need to pass in self, only exists within the class definition

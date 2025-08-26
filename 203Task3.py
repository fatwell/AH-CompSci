#fatwell
#26/8/25
#203Task3

rowNum = 6
colNum = 4
Seat = [["" for x in range(colNum)] for y in range(rowNum)]
Seat[1][2] = "F.A"
Seat[0][0] = "C.M"
Seat[5][3] = "I.S"



Initials = input("What are your initials?:  ")
ChosenRow = int(input("Enter a Chosen Row: "))
ChosenCol = int(input("Enter a Chosen Collumn: "))

while Seat[ChosenRow][ChosenCol] != "":
    print("Error the seat you have selected has been taken")
    ChosenRow = int(input("Enter a Chosen Row: "))
    ChosenCol = int(input("Enter a Chosen Collumn: "))

if Seat[ChosenRow][ChosenCol] == "":
    Seat[ChosenRow][ChosenCol] = 1
    print("Successful! The seat has been booked")





#to print
#for x in range(rowNum):
    #row = ""
    #for y in range(colNum):
    #    row += str(Seat[x][y])+ ","

    #row = row[:-1]
    #print(row)

    


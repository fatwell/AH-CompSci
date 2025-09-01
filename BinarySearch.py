#BinarySearch
#Fatwell
#1/9/25

numbers = [9,16,34,48,57,59,72,82,80,91]

target = 82
startpos = 0
endpos = len(numbers)-1
counter = 0
found = False

while found == False and (startpos<=endpos):
    middle = int((startpos+endpos)//2)
    if numbers[middle] == target:
        found = True
    elif numbers[middle] < target:
        startpos = middle + 1
    else:
        endpos = middle - 1
    counter += 1

if found == True: 
    print("The target", target, "was found at position", counter)

if found == False:
    print("We were unable to find the target,", target, " in the array")

        

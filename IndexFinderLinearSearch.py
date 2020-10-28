## Author: Feras
## Description: A function that searches a number between 
##  1 and 100 using linear search, and return the index 
##  of the ordered list of numbers  Return -1 if not found


def numLinearSearch(integer):
    lst = list(range(1,101))
    for i in range(0,len(lst)):
        if (integer == lst[i]):
            print("Index is: " + str(i))
            return i
    print("The index is not found!")
    return -1

userInput = int(input("\nEnter an integer between 1 to 100 to get the index!\n Integer: "))
numLinearSearch(userInput)

# Andrew Jo
# Programming for Everybody (Getting Started with Python)
# Assignment 5.2
# 04/18/2016
# The code below repeatedly prompts a user for integer numbers
# until the user enters 'done'. Once 'done is entered, print out
# the largest and smallest of the numbers. If the user enters
# anything other than a valid number catch it with a try/except
# and put out an appropriate message and ignore the number. Enter
# the numbers from the book for problems 5.1 and Match the desired
# output as shown.

def printout(largest, smallest):
    print "Maximum is", largest
    print "Minimum is", smallest   

largest = None
smallest = None
while True:
    try:
        num = raw_input("Enter a number: ")
        if num == "done" : 
            break
        intnum = int(num)
        if largest is None and smallest is None:
            largest = intnum
            smallest = intnum
        if num > largest :
            largest = intnum
        elif num < smallest :
            smallest = intnum

        # print "Input number", intnum, type(intnum)
        # print "Largest= ", largest, type(largest)
        # print "Smallest= ", smallest, type(smallest)
    except:
        print "Invalid input"

printout(largest, smallest)
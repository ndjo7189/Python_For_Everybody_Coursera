# Andrew Jo
# Programming for Everybody (Getting Started with Python)
# Assignment 4.6
# 04/18/2016
# The code below prompts the user for hours and rate per hour using raw_input
# to compute gross pay. Award time-and-a-half for the hourly rate for all hours
# worked above 40 hours. Put the logic to do the computation for time-and-a-half
# in a function called computepay() and use the function to do the computation.
# The function should return a value. Use 45 hours and a rate of 10.50 per hour
# to test the program (the pay should be 498.75). You should use raw_input to read
# a string and float() to convert the string to a number. Do not worry about error
# checking the user input unless you want to - you can assume the user types
# numbers properly. DO not name your variable sum or use the sum() function.

def computepay(h,r):
    if h > 40 :
        pay = (40 * r) + (1.5 * (h - 40) * r)
    elif h <= 40 :
        pay = h * r
    return pay

h = raw_input("Enter Hours: ")
r = raw_input("Enter Rate per Hour: ")
h = int(h)
r = float(r)
p = computepay(h,r)
print p

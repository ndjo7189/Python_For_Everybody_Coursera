# Andrew Jo
# Programming for Everybody (Getting Started with Python
# Assignment 3.1
# 04/16/2016
# The code below prompts the user for hours and rate per h our using
# raw_input to compute gross pay. Pay the hourly rate for he hours up to 40 and
# 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and
# a rate of 10.50 per hour to test the program (the pay should be 498.75). You
# should use raw_input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types numbers
# properly.

hrs = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate per Hour: ")
h = float(hrs)
r = float(rate)
if (h <=40) :
    pay = h * r
    print pay
else :
    o = h - 40
    pay = (40 * r) + (1.5 * r * o)
    print pay
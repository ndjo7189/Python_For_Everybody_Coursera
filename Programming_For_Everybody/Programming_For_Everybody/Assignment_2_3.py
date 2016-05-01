# Andrew Jo
# Programming for Everybody (Getting Started with Python)
# Assignment 2.3
# 04/15/2016
# The code below prompts the user for hours and rate per hour using raw_input to compute gross pay
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25)
# You should use raw_input to read a string and float() to convert the string to a number.


hrs = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate per Hour: ")
hrs = int(hrs)
rate = float(rate)
pay = hrs * rate
print pay
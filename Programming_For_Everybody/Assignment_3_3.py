# Andrew Jo
# Programming for Everybody (Getting Started with Python)
# Assignment 3.3
# 04/16/2016
# The code below prompts for a score between 0.0 and 1.0. If the score is out of
# range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
#     >=     0.9     A
#     >=     0.8     B
#     >=     0.7     C
#     >=     0.6     D
#      <     0.6     F
# If the user enters a value out of range, print a suitable error message and exit. For the test,
# enter a score of 0.85.

score = raw_input("Enter Score: ")
try:
    s = float(score)
    if (s >= .9) :
        print 'A'
    elif (s >= .8) :
        print 'B'
    elif (s >= .7) :
        print 'C'
    elif (s >= .6) :
        print 'D'
    elif (s < .6) :
        print 'F'
except:
    print 'Please enter a number between 0.0 and 1.0'
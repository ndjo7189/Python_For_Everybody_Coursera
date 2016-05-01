# Andrew Jo
# Python Data Structures
# Assignment 6.5
# 4/19/2016
# The code uses find() and string slicing (see section 6.10) to extract
# the number at the end of the line below. Convert the extracted value
# to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";
sppos = text.rfind(' ')
length = len(text)
number = text[sppos+1 : length]
number = float(number)
print number
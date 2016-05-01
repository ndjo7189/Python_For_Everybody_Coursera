# Andrew Jo
# Python Data Structures
# Assignment 8.4
# 04/20/2016
# Open the file romeo.txt and read it line by line. For
# each line, split the line into a list of words using the
# split() method. The program should build a list of words.
# For each word on each line check to see if the word is
# already in the list and if not append it to the list.
# When the program completes, sorts and print the resulting
# words in alphabetical order. 
# You can download the sample data at
# http://www.pythonlearn.com/code/romeo.txt

fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print "File cannot be opened:",fname
    exit()

lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
        else: continue

lst.sort()

print lst

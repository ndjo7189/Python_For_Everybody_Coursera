# Andrew Jo
# Python Data Structures
# Assignment 10.2
# 04/20/2016
# The program below reads through the mbox-short.txt and figure
# out the distribution by hour of the day for each of the 
# messages. You can pull the hour out from the 'From ' line by
# finding the time and then splitting the string a second time
# using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.

name = raw_input("Enter file name: ")
if len(name) < 1 : name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print "File cannot be opened:",name
    exit()    

counts = dict()
        
for line in handle:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    time= words[5]
    hour = time[:2]
    counts[hour] = counts.get(hour,0) + 1
#print counts
#hs = counts.items()
#print hs, type(hs)

for hour, count in sorted(counts.items()):
    print hour, count

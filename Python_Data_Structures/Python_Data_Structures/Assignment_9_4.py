# Andrew Jo
# Python Data Structures
# Assignment 9.4
# 04/20/2016
# The program below reads through the
# mbox-short.txt and figure out who has send the greatest number of mail 
# messages. The program looks for 'From' lines and takes the second
# word of those lines as the person who sent the mail. The program creats 
# a Python dictionary  that maps the sender's mail address to a count
# of the number of times they appear in the file. After the dictionary is 
# produced, the program reads through the dictionary using a maximum loop
# to find the most prolific committer.
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
    email = words[1]
    counts[email] = counts.get(email,0) + 1
    #if email not in counts:
    #    counts[email] = 1
    #else:
    #    counts[email] += 1

bigcount = None
bigword = None
for word,count in counts.items():
    #print word, count
    if bigcount is None or count > bigcount:
        bigword = word 
        bigcount = count

print bigword, bigcount
#print counts
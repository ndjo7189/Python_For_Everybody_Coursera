# Andrew Jo
# Python Data Structures
# Assignment 7.2
# 04/19/2016
# The program below promopts for a file name, then opens that file and 
# reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of
# the lines and compute the average of those values and produce an output
# as shown below. Do not use the sum() function or a variable named sum
# in your solution. You can download the sample data at
# http://www.pythonlearn.com/code/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name

fname = raw_input('Enter file name: ')
try:
    fh = open(fname)
except:
    print 'File cannot be opened:',fname
    exit()

count = 0
runningtotal = 0
    
for line in fh:
    line = line.rstrip()
    # skip uninteresting lines
    if not line.startswith('X-DSPAM-Confidence:') :
        continue
    # parse through and extract the number/s
    elif line.startswith('X-DSPAM-Confidence:') :
        sppos = line.rfind(' ')
        length = len(line)
        number = line[sppos + 1 : length]
        number = float(number)
        runningtotal = runningtotal + number
        count = count + 1

average = (runningtotal/count)

print 'Average spam confidence:', average

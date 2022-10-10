# Exercise  8.5: Write a program to read through the mail box data and when you
# find the line that starts with "From", you will split the line into words
# using the split function. We are interested in who sent the message, which is
# second word on the From line.
from mailbox import mbox

# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# You will parse the From line and print out the second word for each From line,
# then you will also count the number of From (not From:) lines and print out a
# count at the end.

# This is a good sample output with a few lines removed:

# Enter a file name: mboxshort.txt
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# zqian@umich.edu

fname = input('Enter a file name')
if len(fname)<1 : fname = 'mboxshort.txt'
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith('From '): continue
    fromlines = line.split()
    count = count + 1
    print(fromlines[1])
print(count)


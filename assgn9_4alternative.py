# 10.1 Write a program to read through the mbox-short.txt and figure out who has sent the
# greatest number of mail messages. The program looks for 'From ' lines and takes the second word
# of those lines as the person who sent the mail. The program creates a Python dictionary that maps
# the name's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop
# to find the most prolific committer.
# Revise a previous program as follows: Read and parse the "From"
# lines and pull out the addresses from the line. Count the number of messages
# from each person using a dictionary.
# After all the data has been read, print the person with the most commits by
# creating a list of (count, email) tuples from the dictionary. Then sort the
# list in the reverse order and print out the person who has the most commits.
#
# Sample line:
# From stephen.marquard@uct.ac.az Sat Jan 05 09:14:16 2008
#
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
#
# Enter a file name: mbox.txt
# zqian@umich.edu 195
#
# Python for Everybody: Exploring Data Using Python 3
# by Charles R. Severance

fname = input('Enter a file name')
if len(fname) < 1: fname = 'mboxshort.txt'

fhand = open(fname)
counts = dict()
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From ': continue
    name = words[1]
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

    print(name)
#    counts[name] = counts.get(name, 0) + 1

    #    sender[name] = sender.get(name,0) + 1 #retrieve, create, update counter

#bigcount = None
#bigword = None
#for word, count in counts.items():
#    if bigcount is None or count > bigcount:
#        bigcount = count
#        bigword = word
#print(bigword, bigcount)

# counts = dict()
# for line in fhand:
#    words = line.split()
#    if len(line)<2 or words[0] != 'From ' : continue
#    for word in words:
#        counts[word] = counts.get(word,0) + 1

# bigcount = None
# bigword = None
# for word, count in sender.items():
#    if bigcount is None or count > bigcount:
#        bigcount = count
#        bigword = word
# print(bigword, bigcount)

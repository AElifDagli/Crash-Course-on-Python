# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the
# greatest number of mail messages. The program looks for 'From ' lines and takes the second word
# of those lines as the person who sent the mail. The program creates a Python dictionary that maps
# the name's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop
# to find the most prolific committer.

fname = input('Enter a file name')
if len(fname)<1 : fname = 'mboxshort.txt'

fhand = open(fname)
sender = dict()
for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    name = words[1]
    sender[name] = sender.get(name,0) + 1 #retrieve, create, update counter

bigcount = None
bigword = None
for word, count in sender.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
print(bigword, bigcount)





#counts = dict()
#for line in fhand:
#    line = line.rstrip()
#    words = line.split()
#    for word in words:
#        counts[word] = counts.get(word,0) + 1

#bigcount = None
#bigword = None
#for word, count in sender.items():
#    if bigcount is None or count > bigcount:
#        bigcount = count
#        bigword = word
#print(bigword, bigcount)
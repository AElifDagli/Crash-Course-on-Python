# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for
# each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string
# a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input('Enter a file name')
if len(fname)<2 : fname = 'mboxshort.txt'
fh = open(fname)
dich = dict()
lst = list()
for line in fh:
    if not line.startswith('From ') : continue
    hours = line.split()[5].split(':')[0]        # hour = exhour[5].split(':')
    dich[hours] = dich.get(hours, 0) + 1         # increase count for each hour in dictionary

#for k, v in dich.items():                        # k = hour, v = count
#    lst.append((k,v))                            # append tuples into list
#lst.sort()                                       # sort list by hour
#for k, v in lst:                                # loop through list of tuples
#    print(k, v)                                 # print counts sorted by hour

# OR THE SOLUTION CAN BE DONE AS BELOW ;

#    sorted(dich.items())                     # tuples will be sorted based on first item
for k, v in sorted(dich.items()) :            # loop through sorted list of tuples in dictionary
    print(k, v)                               # # print counts sorted by hour






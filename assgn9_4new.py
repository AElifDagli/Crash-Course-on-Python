sender=list()
senders=dict()
fname = input('Enter a file name')
if len(fname)<1 : fname = 'mboxshort.txt'
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        sender.append(words[1])
for teacher in sender:
    if teacher in senders:
        senders[teacher]=senders[teacher] + 1
    else:
        senders[teacher] = 1

bigcount = None
bigword = None
for aaa,bbb in senders.items():
    if bigcount is None or bbb > bigcount:
        bigcount = bbb
        bigword = aaa
print(bigword, bigcount)
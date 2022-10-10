fname = input('Enter a file name')
if len(fname)<1 : fname = 'mboxshort.txt'
fh = open(fname)
sender = dict()
for line in fh:
    if not line.startswith('From '): continue
    words = line.split()
    name = words[1]
    sender[name] = sender.get(name,0)+1
    #sender[name]=0
    #sender[name]=sender[name]+1
bigcount = None
bigword = None
for word,count in sender.items():
    if bigcount is None or count>bigcount:
        bigcount = count
        bigword = word
print(bigword, bigcount)
n = input('Enter score')
arr = map(int, input('Enter scores').split())
lst = []
for n in list(arr):
    if not n in lst:
        lst.append(n)
lst.sort(reverse=True)
print(lst[1])

#max = lst[0]
#result = []
#for item in lst:
#    if item < max :
#        result.append(item)
#result.sort(reverse=True)
#max = result[0]
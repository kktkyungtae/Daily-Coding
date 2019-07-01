N = int(input())
arr = [0,1,2,3,4,5,6,7,8,9]
n = len(arr)
lists = []

for i in range(1,(1<<n)):
    numlist = ''
    for j in range(0,n):
        if i & (1<<j):
            numlist += str(arr[j])
    lists.append(int(numlist))
lists.sort()

if N >= len(lists):
    print('-1')
else:
    print(lists[N])

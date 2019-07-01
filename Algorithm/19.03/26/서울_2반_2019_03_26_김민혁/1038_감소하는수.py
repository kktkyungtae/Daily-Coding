T = int(input())

num= [9,8,7,6,5,4,3,2,1,0]
n = len(num)
allN = []
for i in range(1,(1<<n)):
    numb = ''
    for j in range(0,n):
        if i & (1<<j):
            numb+= str(num[j])
    allN.append(int(numb))

allN.sort()
if T >= len(allN):
    print('-1')
else:
    print(allN[T])




    









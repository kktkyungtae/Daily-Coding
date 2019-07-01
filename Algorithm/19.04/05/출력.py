grid=[[[0] for _ in range(5)]  for _ in range(5)]
[print(*i) for i in grid]
a=list(range(1,10))
print(a)

b=[1,1,1,1,1,1,1,2,3,4,5,6,7,8,9,10,11]
b=list(set(b))
print(b)

grid=[[0 for _ in range(5)]  for _ in range(5)]
[print(*i) for i in grid]

from itertools import combinations

a=[1,2,3,4,5]
li=[]
for i in a:
    for j in combinations(a,i):
        li.append(j)
b=sorted(li, key=lambda x:len(x),reverse=True)
for i in b:
    print(i)


a=[1,2,3,4]
b=[5,6,7,8]
for i in zip(a,b):
    x,y=i
    x+=1
    print(x)
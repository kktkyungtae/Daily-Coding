a = [1,2,3,4,0,5]

for i in a:
    if i == 0:
        print(a.index(i))

c = [1,3,4]
b = [1,3,4]

print(b > c)

a.sort()
print(a)
b = sorted(a, reverse=True)
a.reverse()
print(b)
print(a)
print(a)

b.remove(3)
print(b)
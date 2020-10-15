from itertools import chain
# 2중 리스트를 일자로 펴기!
import numpy as np

dist = [[-1] * 3 for _ in range(3)]
dist_7 = [[7] * 3 for _ in range(3)]

print(dist)
li_1 = sum(dist, [])
li_2 = list(chain(*dist))
li_3 = [y for x in dist for y in x]
li_4 = []
for x in dist:
    for y in x:
        li_4.append(y)

li_5 = []
for x in dist:
    li_5.append(x)

print(li_1)
print(li_2)
print(li_3)
print(li_4)
print(li_5)

li_6 = np.array(dist)
print(li_6.flatten())

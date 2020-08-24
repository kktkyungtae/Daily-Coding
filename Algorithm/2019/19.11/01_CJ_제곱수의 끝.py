# CJ Coding Test
# 제곱수

# 주어지는 수의 각 자리수를 제곱해서 더하는 것을 반복하여
# 1이 되는 지 판별하고, 1이 될 시 몇회 반복하였는지 출력하고
# 1이 되지 않는 수는 -1을 출력
# 주어지는 수는 2**31 -1

import itertools

a = [i for i in range(1,10)]

for i in range(len(a)):
    a[i] = int(a[i] ** 2)

ten = []
for i in range(1, 11):
    ten.append(10**i)

for i in range(2, len(a)):
    perm = itertools.combinations()
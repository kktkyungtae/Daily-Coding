# 2309

# import sys
# sys.stdin = open('02_input.txt','r')
import random

hobit = []
for i in range(9):
    a = int(input())
    hobit.append(a)

result = []
for k in range(0,1<<9):
    temp_list = []
    for j in range(0,9):
        if k & (1<<j):
            temp_list.append(hobit[j])
    if sum(temp_list) == 100 and len(temp_list) == 7:
        result.append(temp_list)

ans = random.choice(result)
ans.sort()

for i in ans:
    print(i)
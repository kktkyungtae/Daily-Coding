# 난쟁이들의 키가 주어지고 아홉 난쟁이의 키는 다 다르다
# 더해서 100이 되는 7명을 랜덤으로 출력해라
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
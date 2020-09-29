# Baekjoon

# 완전탐색
# 9명의 난쟁이 중에서 키의 합이 100이 되는 7명을 랜덤으로 출력해라
# 키를 오름차 순으로 출력하시오!
#
# from itertools import combinations, permutations
# import random
#
# sangwon_li = []
# for i in range(9):
#     temp = int(input())
#     sangwon_li.append(temp)
#
# # 조합
# sangwon_com = combinations(sangwon_li, 7)
#
# sangwons = []
# for j in sangwon_com:
#     if sum(j) == 100:
#         sangwons.append(j)
#     else:
#         pass
#
# result = list(random.choice(sangwons))
# result.sort()
#
# for j in result:
#     print(j)

from itertools import combinations
import random

nanjangee = []
for i in range(9):
    nanjangee.append(int(input()))

com_nan = combinations(nanjangee, 7)

nan_li = []
for j in com_nan:
    if sum(j) == 100:
        nan_li.append(j)
    else:
        pass

result = list(random.choice(nan_li))
result.sort()

for _ in result:
    print(_)
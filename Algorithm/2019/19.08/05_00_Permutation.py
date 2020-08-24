# import itertools
#
# pool = ['A', 'B', 'C']
#
# pool_3 = list(itertools.permutations(pool))
#
# # print(pool_3)
# # print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
# # print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
#
# pool_2 = list(map(''.join, itertools.permutations(pool,2)))
# print(pool_2)
#
# nums = [1,2,3]
#
# num_per = list(itertools.permutations(nums, 2))
# print(num_per)
#
# for i in

from itertools import combinations, permutations

a = [1,2,3,4,5]

for combi in combinations(a,3):
    print(combi)

for permi in permutations(a,3):
    print(permi)
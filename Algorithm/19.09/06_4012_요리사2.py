# SW Expert Academy
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH

# 스타트와 링크랑 동일

import itertools

tc = int(input())

for t in range(tc):
    n = int(input())
    foods = [list(map(int, input().split())) for _ in range(n)]

    fd = [i for i in range(n)]
    com_fd = list(itertools.combinations(fd, n//2))

    min_result = 999999

    for i in range(len(com_fd)//2):
        donghwan = com_fd[i]
        dongjoon = fd[:]

        hwan_result = 0
        joon_result = 0

        for i in donghwan:
            dongjoon.remove(i)
            for j in donghwan:
                hwan_result += foods[i][j]

        for i in dongjoon:
            for j in dongjoon:
                joon_result += foods[i][j]

        min_result = min(abs(hwan_result - joon_result), min_result)

    print('#{} {}'.format(t+1,min_result))

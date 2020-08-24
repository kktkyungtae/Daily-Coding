# SW Expert Academy
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH

# 스타트와 링크랑 동일

import itertools

tc = int(input())
for t in range(tc):
    n = int(input())
    food = [list(map(int, input().split())) for _ in range(n)]

    # print(field)
    fd = [i for i in range(n)]

    # 리스트라고 선언해야 된다.
    combi_fd = list(itertools.combinations(fd, int(n//2)))

    # print(combi_player)

    result = []
    # 어짜피 combi 중에 처음꺼랑 제일 뒤에꺼랑 같이 묶이니까
    # for 문은 반만 돌면 된다
    for i in range(int(len(combi_fd)//2)):
        hwan = combi_fd[i]
        joon = fd[:]

        # 각
        hwan_result = 0
        joon_result = 0

        for k in hwan:
            joon.remove(k)
            for l in hwan:
                hwan_result += food[k][l]

        for k in joon:
            for l in joon:
                joon_result += food[k][l]

        result.append(abs(hwan_result - joon_result))

    print('#{} {}'.format(t + 1, min(result)))

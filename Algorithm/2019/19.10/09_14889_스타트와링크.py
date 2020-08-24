# baekjoon
# https://www.acmicpc.net/problem/14889

# 짝수의 선수가 있고 이 선수들을 2팀으로 나누어야한다
# 각각 팀이 되었을 때 능력치가 인풋으로 주어진다
# 팀을 나누고 그 능력치를 합했을 때
# 두 팀의 차이가 최소가 되는 값을 출력해라

import itertools

n = int(input())
him = [list(map(int, input().split())) for _ in range(n)]

mem = [i for i in range(n)]

gs = list(itertools.combinations(mem, n//2))

re = []
for i in range(len(gs)//2):
    start = gs[i]
    link = mem[:]

    start_re = 0
    link_re = 0

    for j in start:
        link.remove(j)
        for k in start:
            start_re += him[j][k]

    for j in link:
        for k in link:
            link_re += him[j][k]

    re.append(abs(start_re - link_re))

print(min(re))


'''
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
'''
# Baekjoon
# https://www.acmicpc.net/problem/17406

# 배열이 주어진다
# 각 행의 합 중에서 가장 작은 값을 뽑는데,,
# 회전 연산에 따라 배열을 회전 시키고나서
# 각 행의 합 중에서 최소값을 출력한다

from itertools import permutations as pm
from collections import deque

H, W, K = map(int, input().split())
g = [list(map(int, input().split())) for i in range(H)]
r = [list(map(int, input().split())) for i in range(K)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def rotate(y, x, r, gr):
    for ii in range(1, r+1):
        idx = []
        t = deque()
        ty, tx = y-ii, x-ii

        for k in range(4):
            for j in range(2*ii):
                ty, tx = ty + dy[k], tx + dx[k]
                idx.append((ty, tx))
                t.append(gr[ty][tx])

        t.appendleft(t.pop())

        for i in range(len(t)):
            gr[idx[i][0]][idx[i][1]] = t[i]

    return gr

# ans = float('inf')
ans = 99999

for ridx in pm(range(K), K):
    tmpg = [[x for x in g[k]] for k in range(H)]

    for i in range(K):
        tmpg = rotate(r[ridx[i]][0] - 1, r[ridx[i]][1] - 1, r[ridx[i]][2], tmpg)

    ans = min(ans, min([sum(tmpg[i]) for i in range(H)]))

print(ans)
# baekjoon
# https://www.acmicpc.net/problem/14502

# 바이러스가 퍼지는 것을 막아야되는데
# 벽은 3개만 세울 수 있다.
# 벽을 세워서 바이러스가 안퍼진 최대 영역을 구하여라

import collections
import itertools

def bfs():
    virus_q = collections.deque()
    visited = [[False]*m for a in range(n)]
    for i in range(n):
        for j in range(m):
            if sector[i][j] == 2:
                virus_q.append([i, j])
                visited[i][j] = True


    safe = 0

    while virus_q:
        x, y = virus_q.popleft()
        for i, j in (1,0), (-1,0), (0,1), (0,-1):
            nx = x + i
            ny = y + j
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False:
                    if copy_sec[nx][ny] == 0:
                        visited[nx][ny] = True
                        virus_q.append([nx, ny])
                        copy_sec[nx][ny] = 3
    # for a in copy_sec:
    #     print(a)

    for i in range(n):
        for j in range(m):
            if copy_sec[i][j] == 0:
                safe += 1
    # print(safe)
    return safe

n, m = map(int, input().split())
sector = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]

# 덱
zero_li = []

for i in range(n):
    for j in range(m):
        if sector[i][j] == 0:
            zero_li.append([i, j])

zero_combi = itertools.combinations(zero_li, 3)

safe_li = []
for pick in zero_combi:
    copy_sec = [0]*n
    for a in range(n):
        copy_sec[a] = sector[a][:]
    q, w, e = pick[0], pick[1], pick[2]
    copy_sec[q[0]][q[1]] = 1
    copy_sec[w[0]][w[1]] = 1
    copy_sec[e[0]][e[1]] = 1

    safe_li.append(bfs())


print(max(safe_li))
# baekjoon
# https://www.acmicpc.net/problem/14502

# 바이러스가 퍼지는 것을 막아야되는데
# 벽은 3개만 세울 수 있다.
# 벽을 세워서 바이러스가 안퍼진 최대 영역을 구하여라

import collections
import itertools

n, m = map(int, input().split())
sector = [list(map(int, input().split())) for _ in range(m)]
# print(sector)

visited = [[False]*m for _ in range(n)]

# 덱
virus_q = collections.deque()
move_q = collections.deque()
zero_li = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    for j in range(m):
        if sector[i][j] == 2:
            virus_q.append([i, j])
            visited[i][j] = True
        elif sector[i][j] == 0:
            zero_li.append([i, j])

pick_cell = itertools.combinations(zero_li, 3)

for pick in pick_cell:
    copy_sector = sector[:]
    q, w, e = pick[0], pick[1], pick[2]
    copy_sector[q[0]][q[1]] = 1
    copy_sector[w[0]][w[1]] = 1
    copy_sector[e[0]][e[1]] = 1

    while virus_q:
        tmp = virus_q.popleft()
        tmp_x = tmp[0]
        tmp_y = tmp[1]

        for i in range(4):
            tmp_xx = tmp_x + dx[i]
            tmp_yy = tmp_y + dy[i]

            if 0 <= tmp_xx < n and 0 <= tmp_yy < m:
                if visited[tmp_xx][tmp_yy] == False and sector[tmp_xx][tmp_yy] == 0:
                    sector[tmp_xx][tmp_yy] = 2
                    visited[tmp_xx][tmp_yy] = True
                    virus_q.append([tmp_xx, tmp_yy])






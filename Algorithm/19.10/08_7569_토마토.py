# Baekjoon
# https://www.acmicpc.net/problem/7569

# 1의 상하좌우로 인접한 0을 1로 바꾼다
# 주어진 전체 맵에서 0이 1로 바뀔 때 까지 걸리는 시간을 출력하라
# 2차원이 아닌, 3차원이다

import collections

m, n, h = map(int, input().split())
mapp = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

q = collections.deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if mapp[i][j][k] == 1:
                q.append((i, j, k))

def bfs():
    while q:
        x, y, z = q.popleft()

        dx = [-1, 1, 0, 0, 0, 0]
        dy = [0, 0, -1, 1, 0, 0]
        dz = [0, 0, 0, 0, -1, 1]

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if mapp[nx][ny][nz] == 0:
                    mapp[nx][ny][nz] = mapp[x][y][z] + 1
                    q.append((nx, ny, nz))

def solve():
    bfs()
    ans = 0
    for i in range(h):
        for j in range(n):
            if 0 in mapp[i][j]:
                return -1
            ans = max(ans, max(mapp[i][j]))
    return ans-1

print(solve())
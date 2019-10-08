# Baekjoon
# https://www.acmicpc.net/problem/7576

# 1의 상하좌우로 인접한 0을 1로 바꾼다
# 주어진 전체 맵에서 0이 1로 바뀔 때 까지 걸리는 시간을 출력하라

import collections

m, n = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]
q = collections.deque()

for i in range(n):
    for j in range(m):
        if mapp[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if mapp[nx][ny] == 0:
                mapp[nx][ny] = mapp[x][y] + 1
                q.append((nx, ny))

def solve():
    ans = 0
    for i in mapp:
        if 0 in i:
            return -1
        ans = max(ans, max(i))
    return ans - 1

print(solve())


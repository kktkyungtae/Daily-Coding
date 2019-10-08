# Baekjoon
# https://www.acmicpc.net/problem/7576

# 1의 상하좌우로 인접한 0을 1로 바꾼다
# 주어진 전체 맵에서 0이 1로 바뀔 때 까지 걸리는 시간을 출력하라

from collections import deque

m, n = map(int, input().split())
a = []
q = deque()

for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(m):
        if a[i][j] == 1:
            q.append((i, j))

def bfs():
    while q:
        x, y = q.popleft()
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny]:
                    continue
                a[nx][ny] = a[x][y] + 1
                q.append((nx, ny))

def solve():
    bfs()
    ans = 0
    for i in range(n):
        if 0 in a[i]:
            return -1
        ans = max(ans, max(a[i]))
    return ans-1

print(solve())
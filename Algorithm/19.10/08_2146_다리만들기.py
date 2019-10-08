# baekjoon
# https://www.acmicpc.net/problem/2146

# 섬을 연결하는데, 가장 짧게 연결할 수 있는 가장 짧은 다리는?

import sys
import collections
sys.setrecursionlimit(10**9)

n = int(input())
mapp = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = 10**9
k = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bbfs(x, y):
    visited[x][y] = True
    mapp[x][y] = k
    q = collections.deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False and mapp[nx][ny] == 1:
                    mapp[nx][ny] = k
                    visited[nx][ny] = True
                    q.append((nx, ny))

def bfs(h):
    global result
    dist = [[-1] * n for _ in range(n)]
    q = collections.deque()

    for i in range(n):
        for j in range(n):
            if mapp[i][j] == h:
                dist[i][j] = 0
                q.append((i, j))

    while q:
        # for i in dist:
        #     print(i)
        # print()

        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if mapp[nx][ny] and mapp[nx][ny] != h:
                result = min(result, dist[x][y])
                return
            if not mapp[nx][ny] and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y]+1
                q.append((nx, ny))

for i in range(n):
    for j in range(n):
        if mapp[i][j] and not visited[i][j]:
            bbfs(i, j)
            k += 1

for i in range(1, k+1):
    bfs(i)


print(result)
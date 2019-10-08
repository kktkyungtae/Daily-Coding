import sys
from collections import deque
sys.setrecursionlimit(10**6)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
check = [[False]*n for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, -1, 0, 1)
ans, k = 10**9, 1

def dfs(x, y):
    check[x][y] = True
    a[x][y] = k
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if not check[nx][ny] and a[nx][ny]:
            dfs(nx, ny)

def bfs(z):
    global ans
    dist = [[-1]*n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if a[i][j] == z:
                q.append((i, j))
                dist[i][j] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if a[nx][ny] and a[nx][ny] != z:
                ans = min(ans, dist[x][y])
                return
            if not a[nx][ny] and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y]+1
                q.append((nx, ny))

for i in range(n):
    for j in range(n):
        if not check[i][j] and a[i][j]:
            dfs(i, j)
            k += 1
for i in range(1, k+1):
    bfs(i)
print(ans)

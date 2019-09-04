from collections import deque
from sys import stdin
input = stdin.readline

def bfs():
    q = deque()
    q.append((0, 0))
    check = [[False]*m for _ in range(n)]
    check[0][0] = True
    while q:
        x, y = q.popleft()
        for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny] == False:
                    if a[nx][ny] >= 1:
                        a[nx][ny] += 1
                    else:
                        q.append((nx, ny))
                        check[nx][ny] = True

def melt():
    melted = False
    for i in range(n):
        for j in range(m):
            if a[i][j] >= 3:
                a[i][j] = 0
                melted = True
            elif a[i][j] == 2:
                a[i][j] = 1
    return melted


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
while True:
    bfs()
    if melt():
        ans += 1
    else:
        break
print(ans)

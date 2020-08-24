# Backjoon
# https://www.acmicpc.net/problem/1012

# 배추 밭에 배추들이 심어져있다
# 흰지렁이를 풀어서 해충이 못 갉아먹게 해야되는데
# 배추가 상하좌우로 연결되어 심어져 있으면 하나 마리만 풀면 된다
# 총 풀어야되는 흰지렁이 수를 구해라
import sys
sys.setrecursionlimit(3333)

def dfs(x, y):
    check[x][y] = True
    for dx, dy in (-1,0), (1,0), (0,1), (0,-1):
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m :
            if a[nx][ny] == 1 and check[nx][ny] == False:
                dfs(nx, ny)

def solve():
    ans = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1 and check[i][j] == False:
                dfs(i, j)
                ans += 1
    print(ans)

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    a = [[0]*m for _ in range(n)]
    check = [[False]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        a[y][x] = 1
    solve()

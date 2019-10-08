# baekjoon
# https://www.acmicpc.net/problem/2146

# 섬을 연결하는데, 가장 짧게 연결할 수 있는 가장 짧은 다리는?

'''
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
'''

import collections

n = int(input())
mapp = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
k = 1
ans = 9999999999

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(x, y):
    visited[x][y] = True
    mapp[x][y] = k
    q = collections.deque()
    q.append((x, y))

    # Q가 있을 때까지 돌아야지! 확인 잘하자
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

def bfs(z):
    global ans
    dist = [[-1]*n for _ in range(n)]

    q = collections.deque()

    for i in range(n):
        for j in range(n):
            if mapp[i][j] == z:
                dist[i][j] = 0
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if mapp[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                # mapp[nx][ny] == 1 and 얘는 달라 얘랑 mapp[nx][ny] and
                # mapp[nx][ny] and 얘랑 같아 얘는 mapp[nx][ny] != 0
                if mapp[nx][ny] != 0 and mapp[nx][ny] != z:
                    ans = min(ans, dist[x][y])
                    return

for i in range(n):
    for j in range(n):
        # visited 처리 확인 잘하자!
        if mapp[i][j] == 1 and visited[i][j] == False:
            check(i, j)
            k += 1

for i in range(1, k + 1):
    bfs(i)

print(ans)

# Baekjoon
# https://www.acmicpc.net/problem/2667

# 상하좌우로 연결된 그룹들의 수와
# 각각이 몇개 인지 오름차 순으로 출력해라

import collections

n = int(input())
mapp = [list(map(int, input())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
k = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = True
    mapp[x][y] = k
    num = 1
    q = collections.deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if mapp[nx][ny] == 1 and visited[nx][ny] == False:
                    mapp[nx][ny] = k
                    num += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return num


nums = []
for i in range(n):
    for j in range(n):
        if mapp[i][j] == 1 and visited[i][j] == False:
            nums.append(bfs(i, j))
            k += 1

nums.sort()
if k == 0:
    print(k)
else:
    print(k-1)
for i in nums:
    print(i)
print()
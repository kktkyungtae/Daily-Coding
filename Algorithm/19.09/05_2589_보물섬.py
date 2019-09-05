# 백준
# https://www.acmicpc.net/problem/2589

# 보물지도가 주어지고
# 지도에는 육지와 바다가 있다
# 육지만 따라가서 두개의 보물 사이의 최단 거리를 구해라
# BFS로 최단 거리를 구한다. 최단 거리 중에서 가장 긴 거리가 답

# BFS 하면서 매번 이동 거리를 저장하고, 가장 큰 이동거리를 저장.
# BFS 결과로 나오는 이동 거리 중, 가장 큰 값이 답

import collections

def bfs(x, y):
    max_cnt = 0
    q = collections.deque()
    q.append((x, y, 0))
    visit[x][y] = True

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visit[nx][ny] == False and mapp[nx][ny] == 'L':
                    q.append((nx, ny, cnt + 1))
                    visit[nx][ny] = True
                    max_cnt = max(max_cnt, cnt + 1)

    return max_cnt


n, m = map(int, input().split())
mapp = [list(input()) for _ in range(n)]
# visit = [[False]*m for _ in range(n)]
# print(mapp)

result = 0
for i in range(n):
    for j in range(m):
        if mapp[i][j] == 'L':
            visit = [[False] * m for _ in range(n)]
            result = max(result, bfs(i, j))

print(result)

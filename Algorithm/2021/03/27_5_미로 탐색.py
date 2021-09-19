# https://www.acmicpc.net/problem/2178
# 1은 지나갈 수 있는 곳
# 0을 지나갈 수 없는 칸
# 서로 인접한 칸으로만 이동가능
# 마지막 칸까지 가는 최단거리를 구하라

from collections import deque

sero, garo = map(int, input().split())

mapp = []
for i in range(s):
    mapp.append(list(map(int, input())))

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >=s or ny < 0 or ny >= 0:
                continue
            if mapp[nx][ny] == 0:
                continue
            if mapp[nx][ny] == 1:
                mapp[nx][ny] = mapp[x][y] + 1
                q.append((nx, ny))

    return mapp[sero-1][garo-1]



print(bfs(0,0))
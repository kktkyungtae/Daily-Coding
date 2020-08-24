# CJ Coding Test
# 오델로
# 주어지는 오델로의 맵과 맵 상의 돌들 중에서
# 어느 부분에 (흑돌)을 두었을 떄, 뒤집어 지는 흰돌의 수가 가장 큰 지
# 뒤집어 지는 흰 돌의 가장 큰 수를 구하라

import sys, collections
sys.stdin = open('01_CJ_오델로.txt', 'r')

def sol(x, y):
    result = [0]

    cnt = 0
    # 상 : x를 1씩 빼 // x 부터 0까지
    for i in range(1, x + 1):
        if mapp[x-i][y] == 0:
            break
        if mapp[x-i][y] == 2:
            cnt += 1
        if mapp[x-i][y] == 1:
            result.append(cnt)
            break

    cnt = 0
    # 하 : x를 1씩 더해 // X 부터 8까지
    for i in range(1, 8 - x):
        if mapp[x+i][y] == 0:
            break
        if mapp[x+i][y] == 2:
            cnt += 1
        if mapp[x+i][y] == 1:
            result.append(cnt)
            break

    cnt = 0
    # 좌 : Y를 1씩 빼 // 0까지
    for i in range(1, y + 1):
        if mapp[x][y - i] == 0:
            break
        if mapp[x-i][y] == 2:
            cnt += 1
        if mapp[x-i][y] == 1:
            result.append(cnt)
            break

    cnt = 0
    # 우 : y를 1씩 더해 // 8까지
    for i in range(1, 8 - y):
        if mapp[x][y + i] == 0:
            break
        if mapp[x][y + i] == 2:
            cnt += 1
        if mapp[x][y + i] == 1:
            result.append(cnt)
            break

    return max(result)

mapp = [list(map(int, input().split())) for _ in range(8)]

white = collections.deque()
for i in range(8):
    for j in range(8):
        if mapp[i][j] == 2:
            white.append((i, j))

atmp = collections.deque()
while white:
    x, y = white.popleft()
    visited = [[False]*8 for _ in range(8)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 8 and 0 <= ny < 8:
            if visited[nx][ny] == False and mapp[nx][ny] == 0:
                atmp.append((nx, ny))

maxx = []
while atmp:
    x, y = atmp.popleft()
    mapp[x][y] = 1
    maxx.append(sol(x, y))

print(max(maxx))
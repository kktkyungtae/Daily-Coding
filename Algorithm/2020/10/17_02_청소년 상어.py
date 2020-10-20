# https://www.acmicpc.net/problem/19236

import sys
from copy import deepcopy

input = sys.stdin.readline
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 첫 시작 x, y = 0, 0
# d, cnt 처음에 먹은 물고기 번호랑, 뱡향
def dfs(x, y, d, cnt):
    global ans, a, fish
    move_fish(x, y)
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if not 0 <= nx < 4 or not 0 <= ny < 4:
            ans = max(ans, cnt)
            return
        if not a[nx][ny]:
            x, y = nx, ny
            continue

        temp_a, temp_fish = deepcopy(a), deepcopy(fish)
        temp1, temp2 = fish[a[nx][ny][0]], a[nx][ny]
        fish[a[nx][ny][0]], a[nx][ny] = [], []
        dfs(nx, ny, temp2[1], cnt + temp2[0] + 1)
        a, fish = temp_a, temp_fish
        fish[a[nx][ny][0]], a[nx][ny] = temp1, temp2
        x, y = nx, ny


def move_fish(sx, sy):
    for i in range(16):
        if fish[i]:
            x, y = fish[i][0], fish[i][1]
            for _ in range(9):
                nx, ny = x + dx[a[x][y][1]], y + dy[a[x][y][1]]
                if not 0 <= nx < 4 or not 0 <= ny < 4 or (nx == sx and ny == sy):
                    a[x][y][1] = (a[x][y][1] + 1) % 8
                    continue
                if a[nx][ny]:
                    fish[a[nx][ny][0]] = [x, y]
                a[nx][ny], a[x][y] = a[x][y], a[nx][ny]
                fish[i] = [nx, ny]
                break

# 입력 받은 지도에 대한 정보는 a
a = [[] for _ in range(4)]
# 물고기의 좌표는 fish에 저장
fish = [[] for _ in range(16)]

for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(0, 7, 2):
        a[i].append([temp[j]-1, temp[j+1]-1])
        fish[temp[j]-1] = [i, j // 2]

ans = 0
# 먹은 물고기의 방향 d, 먹은 물고기의 번호 cnt
d, cnt = a[0][0][1], a[0][0][0] + 1
fish[a[0][0][0]], a[0][0] = [], []
dfs(0, 0, d, cnt)
print(ans)
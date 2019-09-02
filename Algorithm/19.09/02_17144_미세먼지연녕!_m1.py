# 행, 열, 시간
from sys import stdin
from itertools import combinations

r, c, t = map(int, input().split())

mapp = [list(map(int, input().split())) for _ in range(r)]

air_man = []
for i in range(r):
    if mapp[i][0] == -1:
        air_man.append([i, 0])
        air_man.append([i + 1, 0])
        break

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

temp_mp = [[0 for i in range(c)] for _ in range(r)]

#
def dust_diff():
    for y in range(r):
        for x in range(c):
            if mapp[y][x] > 4:
                expand_dust = int(mapp[y][x] / 5)

                for i in range(4):
                    tmp_y = y + dy[i]
                    tmp_x = x + dx[i]
                    if 0 <= tmp_y < r and 0 < tmp_x < c:
                        if mapp[y][x] != -1:
                            temp_mp[tmp_y][tmp_x] += expand_dust
                            mapp[y][x] -= expand_dust


    for y in range(r):
        for x in range(c):
            mapp[y][x] += temp_mp[y][x]
            temp_mp[y][x] = 0


def air_condition():
    y, x = air_man[0]

    # 아래 x : 좌 -> 우
    for i in range():
        mapp[][] = mapp[][]

    # 윗 x : 우 -> 좌
    for i in range():
        mapp[][] = mapp[][]

    # 왼 y : 위 -> 아래
    for i in range():
        mapp[][] = mapp[][]

    # 오른쪽 y : 아래 -> 위
    for i in range():
        mapp[][] = mapp[][]


def cnt():
    total = 0
    for i in mapp:
        total += sum(i)
    total += 2
    print(total)






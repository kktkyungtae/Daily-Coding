# chldkato

import sys
from copy import deepcopy

input = sys.stdin.readline

def remove_blue():
    global ans
    flag1 = 0
    for j in range(2, 6):
        flag2 = 0
        for i in range(4):
            if b[i][j] == -1:
                flag2 = 1
                break
        if flag2 == 1:
            continue
        flag1 = 1
        for i in range(4):
            b[i][j] = -1
        ans += 1
    return 1 if flag1 else 0


def remove_green():
    global ans
    flag1 = 0
    for i in range(2, 6):
        flag2 = 0
        for j in range(4):
            if g[i][j] == -1:
                flag2 = 1
                break
        if flag2 == 1:
            continue
        flag1 = 1
        for j in range(4):
            g[i][j] = -1
        ans += 1
    return 1 if flag1 else 0


def move_blue(t, x, num):
    y = 1
    if t == 1 or t == 2:
        while True:
            if y + 1 > 5 or b[x][y+1] != -1:
                b[x][y] = num
                if t == 2:
                    b[x][y-1] = num
                break
            y += 1

    else:
        while True:
            if y + 1 > 5 or b[x][y+1] != -1 or b[x+1][y+1] != -1:
                b[x][y], b[x+1][y] = num, num
                break
            y += 1

    if remove_blue():
        while True:
            flag = 0
            for j in range(4, 0, -1):
                for i in range(4):
                    if b[i][j] != -1 and b[i][j+1] == -1:
                        if i > 0 and b[i][j] == b[i-1][j]:
                            continue
                        if i < 3 and b[i][j] == b[i+1][j]:
                            d = 1
                            while True:
                                if j + d > 5:
                                    d -= 1
                                    break
                                if b[i][j+d] == -1 and b[i+1][j+d] == -1:
                                    d += 1
                                else:
                                    d -= 1
                                    break
                            if d:
                                b[i][j+d], b[i+1][j+d] = b[i][j], b[i][j]
                                b[i][j], b[i+1][j] = -1, -1
                                flag = 1
                            continue
                        d = 1
                        while True:
                            if j + d > 5:
                                d -= 1
                                break
                            elif b[i][j+d] == -1:
                                d += 1
                            else:
                                d -= 1
                                break
                        b[i][j+d] = b[i][j]
                        b[i][j] = -1
                        flag = 1

            if flag != 0 and not remove_blue():
                break
            if flag == 0:
                break

    if (y == 1 and b[x][y] != -1) or (y == 2 and b[x][y-1] != -1):
        for i in range(4):
            if t == 2 and y == 1:
                b[i][2:] = deepcopy(b[i][:4])
            else:
                b[i][2:] = deepcopy(b[i][1:5])

        if y == 2:
            y -= 1
        if t == 1:
            b[x][y] = -1
        elif t == 2:
            b[x][y], b[x][y-1] = -1, -1
        else:
            b[x][y], b[x+1][y] = -1, -1


def move_green(t, y, num):
    global ans
    x = 1
    if t == 1 or t == 3:
        while True:
            if x + 1 > 5 or g[x+1][y] != -1:
                g[x][y] = num
                if t == 3:
                    g[x-1][y] = num
                break
            x += 1

    else:
        while True:
            if x + 1 > 5 or g[x+1][y] != -1 or g[x+1][y+1] != -1:
                g[x][y], g[x][y+1] = num, num
                break
            x += 1

    if remove_green():
        while True:
            flag = 0
            for i in range(4, 0, -1):
                for j in range(4):
                    if g[i][j] != -1 and g[i+1][j] == -1:
                        if j > 0 and g[i][j] == g[i][j-1]:
                            continue
                        if j < 3 and g[i][j] == g[i][j+1]:
                            d = 1
                            while True:
                                if i + d > 5:
                                    d -= 1
                                    break
                                if g[i+d][j] == -1 and g[i+d][j+1] == -1:
                                    d += 1
                                else:
                                    d -= 1
                                    break
                            if d:
                                g[i+d][j], g[i+d][j+1] = g[i][j], g[i][j]
                                g[i][j], g[i][j+1] = -1, -1
                                flag = 1
                            continue
                        d = 1
                        while True:
                            if i + d > 5:
                                d -= 1
                                break
                            if g[i+d][j] == -1:
                                d += 1
                            else:
                                d -= 1
                                break
                        g[i+d][j] = g[i][j]
                        g[i][j] = -1
                        flag = 1

            if flag != 0 and not remove_green():
                break
            if flag == 0:
                break

    if (x == 1 and g[x][y] != -1) or (x == 2 and g[x-1][y] != -1):
        if t == 3 and x == 1:
            g[2:] = deepcopy(g[:4])
        else:
            g[2:] = deepcopy(g[1:5])

        if x == 2:
            x -= 1
        if t == 1:
            g[x][y] = -1
        elif t == 2:
            g[x][y], g[x][y+1] = -1, -1
        else:
            g[x][y], g[x-1][y] = -1, -1


tc = int(input())

# blue, green 보드 만들기
b = [[-1 for _ in range(6)] for _ in range(4)]
g = [[-1 for _ in range(4)] for _ in range(6)]


# 입력에 맞춰서 각각의 보드에 블록을 위치 시킨다
ans = 0
for i in range(tc):
    t, x, y = map(int, input().split())
    move_blue(t, x, i)
    move_green(t, y, i)

cnt_b, cnt_g = 0, 0
for i in range(4):
    for j in range(2, 6):
        if b[i][j] != -1:
            cnt_b += 1
for i in range(2, 6):
    for j in range(4):
        if g[i][j] != -1:
            cnt_g += 1
print(ans)
print(cnt_b + cnt_g)
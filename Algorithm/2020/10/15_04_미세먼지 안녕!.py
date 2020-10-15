# https://www.acmicpc.net/problem/17144

haeng, yuol, time = map(int, input().split())
mapp = []
for _ in range(haeng):
    mapp.append(list(map(int, input().split())))

# 공청기 찾기
gcg = []
for i in range(haeng):
    if mapp[i][0] == -1:
        gcg.append([i, 0])

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def air_move():
    ## 위쪽 공청기
    up = gcg[0][0]

    # ▶
    temp = mapp[up][yuol - 1]
    for i in range(yuol - 1, 1, - 1):
        mapp[up][i] = mapp[up][i - 1]
    mapp[up][1] = 0

    # ▲
    temp_1 = mapp[0][yuol - 1]
    for i in range(up - 1):
        mapp[i][yuol - 1] = mapp[i + 1][yuol - 1]
    mapp[up - 1][yuol - 1] = temp

    # ◀
    temp_2 = mapp[0][0]
    for i in range(yuol -1 -1):
        mapp[0][i] = mapp[0][i + 1]
    mapp[0][yuol - 2] = temp_1

    # ▼
    # for i in range(up - 1, 1, -1):
    #     mapp[i][0] = mapp[i - 1][0]
    for i in range(1, up-1):
        mapp[i+1][0] = mapp[i][0]
    mapp[1][0] = temp_2

    ## 아래쪽 공청기
    dw = gcg[1][0]
    # ▶ ▶ ▶
    temp = mapp[dw][yuol - 1]
    for i in range(yuol - 1, 1, -1):
        mapp[dw][i] = mapp[dw][i - 1]
    mapp[dw][1] = 0

    # ▼ ▼ ▼
    temp_1 = mapp[haeng - 1][yuol - 1]
    for i in range(haeng - 1, dw + 1, -1):
        mapp[i][yuol - 1] = mapp[i - 1][yuol - 1]
    mapp[dw + 1][yuol - 1] = temp

    # ◀ ◀ ◀
    temp_2 = mapp[haeng - 1][0]
    for i in range(yuol - 2):
        mapp[haeng - 1][i] = mapp[haeng - 1][i + 1]
    mapp[haeng - 1][yuol - 2] = temp_1

    # ▲ ▲ ▲
    for i in range(dw + 1, haeng - 1):
        mapp[i][0] = mapp[i + 1][0]
    mapp[haeng - 2][0] = temp_2

def diffus():
    # 확산될 값들 저장
    tmp = [[0] * yuol for _ in range(haeng)]
    for i in range(haeng):
        for j in range(yuol):
            if mapp[i][j] >= 5:
                val = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    dif = mapp[i][j] // 5
                    if 0 <= nx < haeng and 0 <= ny < yuol and mapp[nx][ny] != -1:
                        tmp[nx][ny] += dif
                        val += dif

                tmp[i][j] -= val
    for i in range(haeng):
        for j in range(yuol):
            mapp[i][j] += tmp[i][j]


for i in range(time):
    diffus()  # 미세먼지 이동
    air_move()  # 공기청정기 작동


total = 0
for i in range(haeng):
    for j in range(yuol):
        if mapp[i][j] > 0:
            total += mapp[i][j]
print(total)
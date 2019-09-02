r, c, t = map(int, input().split())

mapp = []
for _ in range(r):
    mapp.append(list(map(int, input().split())))

air_man = []
for i in range(r):
    if mapp[i] == -1:
        air_man.append([i, 0])
    if len(air_man) == 2:
        break

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dust_temp = [[0 for _ in range(c)] for _ in range(r)]

def dust_diff():
    for y in range(r):
        for x in range(c):
            if mapp[y][x] > 4:
                expand_temp = int(mapp[y][x] / 5)
                for i in range(4):
                    temp_y = y + dy[i]
                    temp_x = x + dx[i]
                    if 0 <= temp_y < r and 0 <= temp_x < c and mapp[temp_y][temp_x] != -1:
                        dust_temp[temp_y][temp_x] += expand_temp
                        mapp[y][x] -= expand_temp

    for y in range(r):
        for x in range(c):
            mapp[y][x] += dust_temp[y][x]
            dust_temp[y][x] = 0


def air_clean():
    y, x = air_man[0]
    for i in range(y - 1, 0, -1):
        mapp[i][0] = mapp[i - 1][0]

    for i in range(x, c - 1):
        mapp[0][i] = mapp[0][i + 1]

    for i in range(0, y):
        mapp[i][c - 1] = mapp[i + 1][c - 1]

    for i in range(c - 1, x, -1):
        mapp[y][i] = mapp[y][i - 1]
    mapp[y][1] = 0

    y, x = air_man[1]
    for i in range(y + 1, r - 1):
        mapp[i][0] = mapp[i + 1][0]

    for i in range(x, c - 1):
        mapp[r - 1][i] = mapp[r - 1][i + 1]

    for i in range(r - 1, y, -1):
        mapp[i][c - 1] = mapp[i - 1][c - 1]

    for i in range(c - 1, x, -1):
        mapp[y][i] = mapp[y][i - 1]

    mapp[y][1] = 0


def cnt():
    total = 0
    for i in mapp:
        total += sum(i)
    total += 2
    print(total)

for _ in range(t):
    dust_diff()
    air_clean()
cnt()


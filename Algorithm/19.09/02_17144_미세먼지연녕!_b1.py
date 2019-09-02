r, c, t = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(r)]
machine = []

for i in range(r):
    if mp[i][0] == -1:
        machine.append([i, 0])
    if len(machine) == 2:
        break

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

dust_temp = [[0 for _ in range(c)] for _ in range(r)]

def dust_move():
    for y in range(r):
        for x in range(c):
            if mp[y][x] > 4:
                expend_dust = int(mp[y][x] / 5)
                for i in range(4):
                    cy = y + dy[i]
                    cx = x + dx[i]
                    limit = 0 <= cy < r and 0 <= cx < c
                    if limit and mp[cy][cx] != -1:
                        dust_temp[cy][cx] += expend_dust
                        mp[y][x] -= expend_dust

    for y in range(r):
        for x in range(c):
            mp[y][x] += dust_temp[y][x]
            dust_temp[y][x] = 0


def air_fresher():
    y, x = machine[0]
    for i in range(y - 1, 0, -1):
        mp[i][0] = mp[i - 1][0]

    for i in range(x, c - 1):
        mp[0][i] = mp[0][i + 1]

    for i in range(0, y):
        mp[i][c - 1] = mp[i + 1][c - 1]

    for i in range(c - 1, x, -1):
        mp[y][i] = mp[y][i - 1]
    mp[y][1] = 0

    y, x = machine[1]
    for i in range(y + 1, r - 1):
        mp[i][0] = mp[i + 1][0]

    for i in range(x, c - 1):
        mp[r - 1][i] = mp[r - 1][i + 1]

    for i in range(r - 1, y, -1):
        mp[i][c - 1] = mp[i - 1][c - 1]

    for i in range(c - 1, x, -1):
        mp[y][i] = mp[y][i - 1]

    mp[y][1] = 0


def cnt():
    total = 0
    for i in mp:
        total += sum(i)
    total += 2
    print(total)

for _ in range(t):
    dust_move()
    air_fresher()
cnt()

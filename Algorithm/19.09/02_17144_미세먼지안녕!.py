# Baekjoon
# acmicpc.net/problem/17144

# 먼지가 사방으로 퍼진다
# 퍼지고 나면 공기청정기가 공기 청정을 하는데
# 붙어있는 2칸에서 윗 칸은 반시계 방향으로 윗 동네 청정하고
# 아랫칸은 시계방향으로 아랫 동네 청정한다
# T초 지난 뒤에 남아있는 먼지의 양을 구해라!

r,c,t = map(int, input().split())

dust_li = [list(map(int, input().split())) for _ in range(r)]
# print(dust_li)

# 청정기 위치 찾기
device = []
for i in range(r):
    if dust_li[i][0] == -1:
        device.append([i, 0])
        device.append([i+1, 0])
        break
# print(device)


def dust_diff():
    global dust_li
    # 임시 리스트 만들기
    # 왜냐면, 동시에 확산되니까 확산 값만 따로 들고 있어야 합쳐지거나 중복 안됨
    temp_dust_li = [[0]*c for _ in range(r)]

    # dust_li 돌면서,,
    for i in range(r):
        for j in range(c):
            # 값이 5 이상이면 확산
            if dust_li[i][j] >= 5:
                temp_dust = dust_li[i][j] // 5

                for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
                    tmp_x = i + dx
                    tmp_y = i + dy

                    # limit 벽 만족하고 / 공기 청정기가 아니면
                    if 0 <= tmp_x < r and 0 <= tmp_y < c and dust_li[i][j] != -1:
                        # 임시 리스트에 확산시키고 // 본래 값에 빼줘
                        temp_dust_li[tmp_x][tmp_y] += temp_dust
                        dust_li[i][j] -= temp_dust

    # 순회하면서 임시에 넣었던 확산 값을 본(dust_li)에 합치기
    for i in range(r):
        for j in range(c):
            dust_li[i][j] += temp_dust_li[i][j]


def clean():
    de1 = device[0][0]
    de2 = device[1][0]

    # 윗
    for i in range(de1-2, -1, -1):
        dust_li[i + 1][0] = dust_li[i][0]

    for i in range(c-1):
        dust_li[0][i] = dust_li[0][i + 1]

    for i in range(de1):
        dust_li[i][c-1] = dust_li[i + 1][c-1]

    for i in range(c-2, -1, -1):
        dust_li[de1][i+1] = dust_li[de1][i]

    dust_li[de1][1] = 0

    # 아래
    for i in range(de2+1, r-1):
        dust_li[i][0] = dust_li[i+1][0]

    for i in range(c-1):
        dust_li[r-1][i] = dust_li[r-1][i+1]

    for i in range(r-2, de2-1, -1):
        dust_li[i+1][c-1] = dust_li[i][c-1]

    for i in range(c-2, -1, -1):
        dust_li[de2][i+1] = dust_li[de2][i]

    dust_li[de2][1] = 0


def solve():
    for _ in range(t):
        dust_diff()
        clean()

    print(sum(map(sum, dust_li)) + 2)

solve()
def print_water():
    print("******************")
    print(" r  c  s  d  z")
    for s in shark:
        print(s)
    print()

    for w in water:
        print(w)
    print()


def move(shark, water):
    # 상어의 좌표를 계산
    for idx in range(len(shark)):
        r, c, s, d, z = shark[idx]
        r -= 1
        c -= 1
        if z in water[r][c]:

            nr = r + s * direction[d][0]
            nc = c + s * direction[d][1]

            if d == 1 or d == 2:

                if 0 <= nr < R:
                    pass

                else:
                    if nr < 0:
                        nr = abs(nr)
                    if (nr // (R - 1)) % 2 == 0:
                        d = 2
                        nr = 0 + (nr % (R - 1))
                    else:
                        d = 1
                        nr = (R - 1) - (nr % (R - 1))

            else:

                if 0 <= nc < C:
                    pass
                else:
                    if nc < 0:
                        nc = abs(nc)
                    if (nc // (C - 1)) % 2 == 0:
                        d = 3
                        nc = 0 + (nc % (C - 1))
                    else:
                        d = 4
                        nc = (C - 1) - (nc % (C - 1))

            water[r][c].remove(z)  # 기존 상어 위치에서 상어 제거
            water[nr][nc].append(z)  # 새로운 위치로 상어를 옮긴다
            shark[idx] = [nr + 1, nc + 1, s, d, z]  # 상어 정보 업데이트


def eat(water, R, C):
    for i in range(R):
        for j in range(C):
            if water[i][j]:
                water[i][j] = [max(water[i][j])]  # 가장 큰 상어만 남긴다.


R, C, M = map(int, input().split())
shark = [list(map(int, input().split())) for _ in range(M)]
water = [[[] for _ in range(C)] for _ in range(R)]
direction = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}
answer = 0

if M:
    # 초기화
    for sh in shark:
        r, c, s, d, z = sh
        water[r - 1][c - 1].append(z)

    for i in range(C):
        for j in range(R):
            if water[j][i]:
                shk = water[j][i].pop(0)  # 낚시
                answer += shk
                break
        move(shark, water)
        eat(water, R, C)

print(answer)
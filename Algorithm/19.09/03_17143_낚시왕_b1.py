def hunt(c) :
    global cnt
    # i번째 열의 상어를 사냥
    for r in range(R) :
        if water[r][c] == 0 :
            continue
        else :
            # 상어가 있다면 그 상어를 잡고(크기 더함)
            cnt += water[r][c][-1]
            # 상어가 있던 자리는 0(물)로 바꿈
            water[r][c] = 0
            return
    return
# 개별 상어의 움직임(total move 보조)
def ind_move(r, c, s, d) :
    # 위
    if d == 1 :
        if r > s :
            return (r-s, c, s, d)
        else :
            s_ = s-r
            chg, left = divmod(s_, R-1)
            if chg % 2 == 0 :
                if left == 0 :
                    return (0, c, s, d)
                else :
                    return (left, c, s, 2)

            else :
                if left == 0 :
                    return (R-1, c, s, 2)
                else :
                    return (R-1-left, c, s, d)
    # 아래
    elif d == 2 :
        if (R-1) - r > s :
            return (r+s, c, s, d)

        else :
            s_ = s- ((R-1) - r)
            chg, left = divmod(s_, R-1)
            if chg % 2 == 0 :
                if left == 0 :
                    return (R-1, c, s, d)
                else :
                    return (R-1-left, c, s, 1)

            else :
                if left == 0 :
                    return (0, c, s, 1)
                else :
                    return (left, c, s, d)

    # 오른쪽
    elif d == 3 :
        if (C-1) - c > s :
            return (r, c+s, s, d)
        else :
            s_ = s- ((C-1) - c)
            chg, left = divmod(s_, C-1)
            if chg % 2 == 0 :
                if left == 0 :
                    return (r, C-1, s, d)
                else :
                    return (r, C-1-left, s, 4)

            else :
                if left == 0 :
                    return (r, 0, s, 4)
                else :
                    return (r, left, s, d)

    elif d == 4 :
        if c > s :
            return (r, c-s, s, d)

        else :
            s_ = s - c
            chg, left = divmod(s_, C-1)
            if chg % 2 == 0:
                if left == 0 :
                    return (r, 0, s, d)
                else :
                    return (r, left, s, 3)

            else :
                if left == 0 :
                    return (r, C-1, s, 3)
                else :
                    return (r, C-1-left, s, d)
# 상어의 이동
def total_move() :
    global water
    temp = [[0]*C for _ in range(R)]
    for r in range(R) :
        for c in range(C) :
            if water[r][c] == 0 :
                continue
            else :
                s, d, z = water[r][c]
                r_, c_, s_, d_ = ind_move(r, c, s, d)
                if temp[r_][c_] == 0 :
                    temp[r_][c_] = (s_, d_, z)

                else :
                    z_ = temp[r_][c_][-1]
                    # 새로 온놈이 더 크면 잡아먹고 걔가 위치
                    if z > z_ :
                        temp[r_][c_] = (s_, d_, z)
                    else :
                    # 반대로 원래 있던놈이 더 크면 잡아먹고 그놈이 위치
                        pass

    water = temp

#f = open('./17143.txt', 'r')
R, C, M = map(int, input().strip().split())
water = [[0]*C for _ in range(R)]

for _ in range(M) :
    r, c, s, d, z = map(int, input().strip().split())
    water[r-1][c-1] = (s,d,z)

cnt = 0
for c in range(C) :
    hunt(c)
    if c == C-1 :
        break
    total_move()
print(cnt)
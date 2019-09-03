# baekjoon source = "https://www.acmicpc.net/problem/17143"

def moving_shrk(shrk, a, b):
    # 방향 별로 나누기

    # 위로
    if shrk[1] == 1:
        flag = False
        for i in range(shrk[0]):
            if flag:
                if a + 1 < r:
                    a += 1
                else:
                    a -= 1
                    shrk[1] = 1
                    flag = False
            else:
                if a - 1 > -1:
                    a -= 1
                else:
                    a += 1
                    shrk[1] = 2
                    flag = True

    # 아래
    elif shrk[1] == 2:
        flag = True
        for i in range(shrk[0]):
            if flag:
                if a + 1 < r:
                    a += 1
                else:
                    a -= 1
                    shrk[1] = 1
                    flag = False
            else:
                if a - 1 > -1:
                    a -= 1
                else:
                    a += 1
                    shrk[1] = 2
                    flag = True

    # 오른쪽
    elif shrk[1] == 3:
        flag = True
        for i in range(shrk[0]):
            if flag:
                if b + 1 < c:
                    b += 1
                else:
                    b -= 1
                    shrk[1] = 4
                    flag = False
            else:
                if b - 1 > -1:
                    b -= 1
                else:
                    b += 1
                    shrk[1] = 3
                    flag = True

    # 왼쪽
    else:
        flag = False
        for i in range(shrk[0]):
            if flag:
                if b + 1 < c:
                    b += 1
                else:
                    b -= 1
                    shrk[1] = 4
                    flag = False
            else:
                if b - 1 > -1:
                    b -= 1
                else:
                    b += 1
                    shrk[1] = 3
                    flag = True
    return [a, b] + shrk

r, c, m = map(int, input().split())
sea = [[0] * c for _ in range(r)]
for i in range(m):
    s = list(map(int, input().split()))
    sea[s[0] - 1][s[1] - 1] = [s[2], s[3], s[4]]

# print(sea)

result = 0

# 상어잡기
for i in range(c):
    move = []
    # 상어 잡아서 없애기
    for j in range(r):
        if sea[j][i]:
            result += sea[j][i][2]
            sea[j][i] = 0
            break

    # 상어 움직이기
    for a in range(r):
        for b in range(c):
            if sea[a][b]:
                tmp = moving_shrk(sea[a][b], a, b)
                sea[a][b] = 0
                move.append(tmp)


    for m in move:
        if sea[m[0]][m[1]]:
            if sea[m[0]][m[1]][2] > m[4]:
                pass
            else:
                sea[m[0]][m[1]] = [m[2], m[3], m[4]]
        else:
            sea[m[0]][m[1]] = [m[2], m[3], m[4]]

print(result)

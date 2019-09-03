# baekjoon source = "https://www.acmicpc.net/problem/17143"

def move_fish(fish, a, b):
    if fish[1] == 1:
        flag = False
        for i in range(fish[0]):
            if flag:
                if a + 1 < r:
                    a += 1
                else:
                    a -= 1
                    fish[1] = 1
                    flag = False
            else:
                if a - 1 > -1:
                    a -= 1
                else:
                    a += 1
                    fish[1] = 2
                    flag = True
    elif fish[1] == 2:
        flag = True
        for i in range(fish[0]):
            if flag:
                if a + 1 < r:
                    a += 1
                else:
                    a -= 1
                    fish[1] = 1
                    flag = False
            else:
                if a - 1 > -1:
                    a -= 1
                else:
                    a += 1
                    fish[1] = 2
                    flag = True
    elif fish[1] == 3:
        flag = True
        for i in range(fish[0]):
            if flag:
                if b + 1 < c:
                    b += 1
                else:
                    b -= 1
                    fish[1] = 4
                    flag = False
            else:
                if b - 1 > -1:
                    b -= 1
                else:
                    b += 1
                    fish[1] = 3
                    flag = True
    else:
        flag = False
        for i in range(fish[0]):
            if flag:
                if b + 1 < c:
                    b += 1
                else:
                    b -= 1
                    fish[1] = 4
                    flag = False
            else:
                if b - 1 > -1:
                    b -= 1
                else:
                    b += 1
                    fish[1] = 3
                    flag = True
    return [a, b] + fish

r, c, m = map(int, input().split())
arr = [[0] * c for _ in range(r)]
for i in range(m):
    s = list(map(int, input().split()))
    arr[s[0] - 1][s[1] - 1] = [s[2], s[3], s[4]]

result = 0
for i in range(c):
    move = []
    for a in range(r):
        if arr[a][i]:
            result += arr[a][i][2]
            arr[a][i] = 0
            break

    for a in range(r):
        for b in range(c):
            if arr[a][b]:
                f = move_fish(arr[a][b], a, b)
                arr[a][b] = 0
                move.append(f)

    for m in move:
        if arr[m[0]][m[1]]:
            if arr[m[0]][m[1]][2] > m[4]:
                pass
            else:
                arr[m[0]][m[1]] = [m[2], m[3], m[4]]
        else:
            arr[m[0]][m[1]] = [m[2], m[3], m[4]]


print(result)

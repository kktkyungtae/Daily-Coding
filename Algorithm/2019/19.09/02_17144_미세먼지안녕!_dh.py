# baekjoon source = "https://www.acmicpc.net/problem/17144"
def check(x, y):
    if x < 0 or x > r - 1:
        return False
    if y < 0 or y > c - 1:
        return False
    if arr[x][y] == -1:
        return False
    return True

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
for i in range(t):
    mun = [[0] * c for _ in range(r)]
    for a in range(r):
        for b in range(c):
            if arr[a][b] == -1:
                air = [a, b]
            if arr[a][b] != 0 and arr[a][b] != -1:
                k = 0
                for z in range(4):
                    x = a + dx[z]
                    y = b + dy[z]
                    if check(x, y):
                        mun[x][y] += arr[a][b] // 5
                        k += arr[a][b] // 5
                arr[a][b] -= k

    for a in range(r):
        for b in range(c):
            arr[a][b] += mun[a][b]

    x = air[0]-2
    y = 0
    flag = True
    flag_x = True
    flag_y = True
    while True:
        if flag:
            if flag_x:
                if x - 1 > -1:
                    arr[x][y] = arr[x - 1][y]
                    x -= 1
                else:
                    flag_x = False
                    flag = False
            else:
                if x + 1 <= air[0]-1:
                    arr[x][y] = arr[x+1][y]
                    x += 1
                else:
                    flag_x = True
                    flag = False
        else:
            if flag_y:
                if y + 1 < c :
                    arr[x][y] = arr[x][y+1]
                    y += 1
                else:
                    flag_y = False
                    flag = True
            else:
                if y - 1 > 0:
                    arr[x][y] = arr[x][y-1]
                    y -= 1
                else:
                    arr[x][y] = 0
                    break

    x = air[0] + 1
    y = 0
    flag = True
    flag_x = True
    flag_y = True
    while True:
        if flag:
            if flag_x:
                if x + 1 < r:
                    arr[x][y] = arr[x + 1][y]
                    x += 1
                else:
                    flag_x = False
                    flag = False
            else:
                if x - 1 >= air[0] :
                    arr[x][y] = arr[x - 1][y]
                    x -= 1
                else:
                    flag_x = True
                    flag = False
        else:
            if flag_y:
                if y + 1 < c:
                    arr[x][y] = arr[x][y + 1]
                    y += 1
                else:
                    flag_y = False
                    flag = True
            else:
                if y - 1 > 0:
                    arr[x][y] = arr[x][y - 1]
                    y -= 1
                else:
                    arr[x][y] = 0
                    break

result = 0
for i in arr:
    result += sum(i)
print(result + 2)
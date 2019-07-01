import sys
sys.stdin = open('1_othello.txt','r')

def check_garo(x, y, stone):
    n = x
    # 오른쪽 가로 탐색
    for i in range(x+1, N+1):
        if othello[i][y] == stone:
            n = i
            break
        elif othello[i][y] == 0:
            break
    for j in range(x+1, n+1):
        othello[j][y] = stone

    n = x
    # 왼쪽 가로 탐색
    for i in range(x-1, 0, -1):
        if othello[i][y] == stone:
            n = i
            break
        elif othello[i][y] == 0:
            break
    for j in range(n, x):
        othello[j][y] = stone

def check_sero(x, y, stone):
    n = y
    # 위쪽 세로 탐색
    for i in range(y+1, N+1):
        if othello[x][i] == stone:
            n = i
            break
        elif othello[x][i] == 0:
            break
    for j in range(y+1, n+1):
        othello[x][j] = stone

    n = y
    # 아래쪽 세로 탐색
    for i in range(y-1, 0, -1):
        if othello[x][i] == stone:
            n = i
            break
        elif othello[x][i] == 0:
            break
    for j in range(n, y):
        othello[x][j] = stone

def check_daegak(x, y, stone):
    n = 0
    # 위쪽 대각 탐색
    for i in range(1, min(N-x, N-y)+1):
        if x+1 <= N and y+i <= N:
            if othello[x+i][y+i] == stone:
                n = i
                break
            elif othello[x+i][y+i] == 0:
                break
    for j in range(1, n+1):
        if x+j <= N and y+j <= N:
            othello[x+j][y+j] = stone

    n = 0
    for i in range(1, min(x, y)+1):
        if x-i > 0 and y-i > 0:
            if othello[x-i][y-i] == stone:
                n = i
                break
            elif othello[x-i][y-i] == 0:
                break
    for j in range(1, n+1):
        if x-j > 0 and y-j > 0:
            othello[x-j][y-j] = stone

    # 아래쪽 대각 탐색
    n = 0
    for i in range(1, min(x, N-y)+1):
        if x-i > 0 and y+i <= N:
            if othello[x-i][y+i] == stone:
                n = i
                break
            elif othello[x-i][y+i] == 0:
                break
    for j in range(1, n+1):
        if x-j > 0 and y+j <= N:
            othello[x-j][y+j] = stone

    n = 0
    for i in range(1, min(N-x, y)+1):
        if x+i <= N and y-i > 0:
            if othello[x+i][y-i] == stone:
                n = i
                break
            elif othello[x+i][y-i] == 0:
                break
    for j in range(1, n+1):
        if x+j <= N and y-j > 0:
            othello[x+j][y-j] = stone


T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    othello = [[0]*(N+1) for _ in range(N+1)]
    othello[(N//2)+1][(N//2)] = 1
    othello[(N//2)][(N//2)] = 2
    othello[(N//2)+1][(N//2)+1] = 2
    othello[(N//2)][(N//2)+1] = 1

    for m in range(M):
        x, y, stone = map(int, input().split())
        othello[x][y] = stone
        check_garo(x, y, stone)
        check_sero(x, y, stone)
        check_daegak(x, y, stone)

    num1 = 0
    num2 = 0

    for i in range(N+1):
        for j in range(N+1):
            if othello[i][j] == 1:
                num1 += 1
            elif othello[i][j] == 2:
                num2 += 1

    print("#{} {} {}".format(t+1, num1, num2))
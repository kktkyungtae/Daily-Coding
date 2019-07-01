import sys
sys.stdin = open('input/05_input.txt','r')

def findChemi(matrix,x,y):
    global chemi_cnt

    chemi_cnt += 1
    x_cnt = 0
    y_cnt = 0
    pre_x = x # 나중에 matrix를 지우기 위해 시작 x를 복사
    pre_y = y # 나중에 matrix를 지우기 위해 시작 y를 복사

    # matrix 검사
    # 오른쪽 검사
    while True:
        if matrix[x][y] != 0:
            y += 1
            y_cnt += 1
        elif y >= n:
            break
        else:
            break
    y = pre_y

    # 아래쪽 검사
    while True:
        if matrix[x][y] != 0:
            x += 1
            x_cnt += 1
        elif x >= n:
            break
        else:
            break
    x = pre_x
    result.append([x_cnt * y_cnt, x_cnt, y_cnt])

    # 검사한 matrix 0으로 만들기
    for i in range(x , x + x_cnt + 1):
        for j in range(y, y + y_cnt + 1):
            matrix[i][j] = 0


t = int(input())

for tc in range(t):
    n = int(input())

    matrix = []
    for _ in range(n):
        temp = list(map(int,input().split()))
        matrix.append(temp)

    result = []
    chemi_cnt = 0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                findChemi(matrix, i, j)

    result.sort() # 크기 순으로 정렬

    print("#{} {}".format(tc+1, chemi_cnt), end=' ')
    for i in range(len(result)):
        print("{} {}".format(result[i][1],result[i][2]), end=' ')
    print()



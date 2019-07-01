# 숫자 배열 회전
import sys
sys.stdin = open('input/06_input.txt','r')

t = int(input())

for t in range(t):
    n = int(input())

    matrix = []
    for i in range(n):
        matrix.append(list(map(int,input().split())))

    matrix_90 = [[0]*n for _ in range(n)]
    matrix_180 = [[0]*n for _ in range(n)]
    matrix_270 = [[0]*n for _ in range(n)]


# for 문 돌릴 때 인덱스 신경 쓰자!
    for y in range(n):
        for x in range(n-1, -1, -1):
            matrix_90[y][(n - 1) - x] = matrix[x][y]

    for y in range(n):
        for x in range(n-1, -1, -1):
            matrix_180[y][(n - 1) - x] = matrix_90[x][y]

    for y in range(n):
        for x in range(n - 1, -1, -1):
            matrix_270[y][(n - 1) - x] = matrix_180[x][y]

    print("#{}".format(t+1))
    for i in range(len(matrix)):
        for j in matrix_90[i]:
            print(j, end='')
        print(end=' ')
        for k in matrix_180[i]:
            print(k, end='')
        print(end=' ')
        for h in matrix_270[i]:
            print(h, end="")
        print()

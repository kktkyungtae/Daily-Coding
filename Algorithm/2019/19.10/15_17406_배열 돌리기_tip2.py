# Baekjoon
# https://www.acmicpc.net/problem/17406

# 배열이 주어진다
# 각 행의 합 중에서 가장 작은 값을 뽑는데,,
# 회전 연산에 따라 배열을 회전 시키고나서
# 각 행의 합 중에서 최소값을 출력한다

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
R = []

for _ in range(K):
    r, c, s = map(int, input().split())
    R.append([r-1, c-1, s])


def value(A):
    return min([sum(a) for a in A])


def rotate(A, R_):
    r, c, ss = R_
    for s in range(1, ss+1):
        tmp = A[r-s+1][c-s]

        # 가로 - 오른쪽
        for j in range(c-s, c+s+1):
            A[r-s][j], tmp = tmp, A[r-s][j]

        # 세로 - 아래로
        for i in range(r-s+1, r+s):
            A[i][c+s], tmp = tmp, A[i][c+s]

        # 가로 - 왼쪽으로
        for j in range(c+s, c-s-1, -1):
            A[r+s][j], tmp = tmp, A[r+s][j]

        # 세로 - 위로
        for i in range(r+s-1, r-s, -1):
            A[i][c-s], tmp = tmp, A[i][c-s]

    return A


def calculate(A, R):
    if len(R)==0:
        global num
        num = min(num, value(A)) if num is not None else value(A)
        return

    A_tmp = [x[:] for x in A]
    for i in range(len(R)):
        A = rotate(A, R[i])
        calculate(A, R[:i]+R[i+1:])
        A = [x[:] for x in A_tmp]
    return


num = None
calculate(A, R)
print(num)

'''

5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1

'''
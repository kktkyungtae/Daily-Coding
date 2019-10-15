def sol(n, A):
    global MIN

    if n == K:
        for i in range(N):
            MIN = min(MIN, sum(A[i]))
        return

    for i in range(K):
        if not check[i]:
            r, c, s = data[i]
            newA = [A[i][:] for i in range(N)]

            for j in range(s):

                y, x = r - s - 1 + j, c - s - 1 + j

                for dy, dx in (0, 1), (1, 0), (0, -1), (-1, 0):
                    for k in range(2 * s - 2 * j):
                        ny, nx = y + dy, x + dx
                        newA[ny][nx] = A[y][x]
                        y, x = ny, nx

            check[i] = 1
            sol(n+1, newA)
            check[i] = 0

N, M, K = map(int, input().split())
mainA = [list(map(int, input().split())) for i in range(N)]
data = [list(map(int, input().split())) for i in range(K)]
check = [0]*K
MIN = 99999

sol(0, mainA)

print(MIN)

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
# Baekjoon
# https://www.acmicpc.net/problem/17406

# 배열이 주어진다
# 각 행의 합 중에서 가장 작은 값을 뽑는데,,
# 회전 연산에 따라 배열을 회전 시키고나서
# 각 행의 합 중에서 최소값을 출력한다

import itertools

N, M, K = map(int, input().split())
Temp = [list(map(int, input().split())) for _ in range(N)]
func = [list(map(int, input().split())) for _ in range(K)]

for i in range(len(func)):
    func[i][0] -= 1
    func[i][1] -= 1

P = list(itertools.permutations(func, K))
def rotate(r, c, s):
    while s:
        tr = A[r-s][c-s]
        tc = A[r-s][c+s]
        for i in range(-s+1, s+1):
            tr = A[r-s][c+i]
            A[r-s][c+i] = tr
            tc, A[r+i][c+s] = A[r+i][c+s], tc

        tr = tc
        tc = A[r+s][c-s]
        for i in range(s-1, -s-1,  -1):
            tr, A[r+s][c+i] = A[r+s][c+i], tr
            tc, A[r+i][c-s] = A[r+i][c-s], tc

        s -= 1

ans = 99999

while P:
    R = P.pop()
    A = [Temp[i][:] for i in range(N)]

    for rot in R:
        r, c, s = rot
        rotate(r, c, s)
    for a in A:
        ans = min(sum(a), ans)

print(ans)

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
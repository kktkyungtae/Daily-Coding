import sys
sys.stdin=open('03_input.txt','r')


def backtracking(a, k, check, tree):
    global ans

    c = [0] * check

    if tree < ans:
        return
    else:
        if k == check:
            result = 1
            for i in range(1, len(a)):
                result *= man[i - 1][a[i]]
            ans = max(result, ans)
        else:
            k += 1
            ncandi = candi(a, k, check, c)
            for i in range(ncandi):
                a[k] = c[i]
                backtracking(a, k, check, tree * man[k - 1][a[k]])
                a[k] = 0


def candi(a, k, check, c):
    in_perm = [False] * check

    for i in range(1, k):
        in_perm[a[i]] = True

    for i in range(N):
        if man[k - 1][i] == 0:
            in_perm[i] = True

    ncandi = 0
    for i in range(check):
        if not in_perm[i]:
            c[ncandi] = i
            ncandi += 1
    return ncandi


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    man = [list(map(int, input().split())) for _ in range(N)]
    a = [0] * (N + 1)
    ans = 0

    for i in range(N):
        for j in range(N):
            man[i][j] = man[i][j] / 100

    backtracking(a, 0, N, 1)
    print(f'#{test_case} {"%0.6f" % (ans * 100)}')
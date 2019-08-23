import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(n, k, names) :
    names = [len(nm) for nm in names]
    cnt = [0 for i in range(21)]

    for i in range(k):
        cnt[names[i]] += 1

    res = 0

    for l in range(n-k):
        cnt[names[l]] -= 1
        cnt[names[l+k]] += 1
        res += cnt[names[l]]

    for m in range(n-k, n):
        cnt[names[m]] -= 1
        res += cnt[names[m]]

    return res

n, k = map(int, input().split())
names = [input() for i in range(n)]
print(solve(n, k, names))
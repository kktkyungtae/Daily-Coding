
n, m = map(int, input().split())
arr = [[0] * n for _ in range(m)]

n = len(arr)
for i in range(n):
    print(*arr[i])
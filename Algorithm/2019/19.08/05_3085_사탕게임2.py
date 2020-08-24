def score(row):
    run = 1
    ans = 1
    for i in range(1, len(row)):
        if row[i] == row[i-1]:
            run+= 1
        else:
            ans = max(ans, run)
            run = 1
    return max(run, ans)

def swap(i1, j1, i2, j2):
    grid[i1][j1], grid[i2][j2] = grid[i2][j2], grid[i1][j1]
    a1 = max(score(row) for row in grid)
    a2 = max(score(row) for row in zip(*grid))
    grid[i1][j1], grid[i2][j2] = grid[i2][j2], grid[i1][j1]
    return max(a1, a2)

n = int(input())
grid = [list(input()) for i in range(n)]
ans = 0

for i in range(n):
    for j in range(n-1):
        ans = max(ans, swap(i, j, i, j+1))
for i in range(n-1):
    for j in range(n):
        ans = max(ans, swap(i, j, i+1, j))
print(ans)
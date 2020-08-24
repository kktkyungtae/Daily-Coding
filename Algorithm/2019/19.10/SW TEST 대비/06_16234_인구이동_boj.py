import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# input
N, L, R = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]

# 체크할 놈들
check = [[False]*N for _ in range(N)]
moving = [[False]*N for _ in range(N)]
cnt = 0

def dfs(x, y):
    global cnt
    check[x][y] = True
    population = a[x][y]
    for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < N:
            if check[nx][ny] == False and L <= abs(a[nx][ny]-a[x][y]) <= R:
                moving[nx][ny] = True
                cnt += 1
                population += dfs(nx, ny)

    return population

def migrate(population):
    for i in range(N):
        for j in range(N):
            if moving[i][j] == True:
                a[i][j] = population
                moving[i][j] = False

def solve():
    global check, cnt
    ans = 0
    while True:
        moved = False
        check = [[False]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if check[i][j] == False:
                    cnt = 1
                    population = dfs(i, j)//cnt
                    if cnt > 1:
                        a[i][j] = population
                        migrate(population)
                        moved = True

        if moved == True:
            ans += 1
        else:
            break
    print(ans)

solve()

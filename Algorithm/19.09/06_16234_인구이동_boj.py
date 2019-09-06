import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, L, R = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
check = [[False]*N for _ in range(N)]
moving = [[False]*N for _ in range(N)]
cnt = 0

def dfs(x, y):
    global cnt
    check[x][y] = True
    population = a[x][y]
    for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if not check[nx][ny] and L <= abs(a[nx][ny]-a[x][y]) <= R:
            moving[nx][ny] = True
            cnt += 1
            population += dfs(nx, ny)

    return population

def migrate(p):
    for i in range(N):
        for j in range(N):
            if moving[i][j]:
                a[i][j] = p
                moving[i][j] = False

def solve():
    global check, cnt
    ans = 0
    while True:
        moved = False
        check = [[False]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if not check[i][j]:
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

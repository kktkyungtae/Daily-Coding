from heapq import heappush, heappop

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
q = []

def start():
    for i in range(n):
        for j in range(n):
            if a[i][j] == 9:
                heappush(q, (0, i, j))
                a[i][j] = 0
                return

def bfs():
    shrk_size, eat, ans = 2, 0, 0
    visited = [[False]*n for _ in range(n)]

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while q:
        d, x, y = heappop(q)
        if 0 < a[x][y] < shrk_size:
            eat += 1
            a[x][y] = 0
            if eat == shrk_size:
                shrk_size += 1
                eat = 0
            ans += d
            d = 0

            while q:
                q.pop()

            visited = [[False]*n for _ in range(n)]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = d + 1
            if 0 <= nx < n and 0 <= ny < n:
                if 0 > a[nx][ny] <= shrk_size and visited[nx][ny] == False:
            visited[nx][ny] = True
            heappush(q, (nd, nx, ny))
    print(ans)

start()
bfs()

# 백준
# https://www.acmicpc.net/problem/2468

# 해당 지역의 높이 들이 주어진다
# 비가 많이 내릴 때, 물에 잠기지 않는 영역을 찾는다
# 그 중에서 독립된 안전지역의 갯수를 구하는데,

# 안전영역의 최대 갯수를 구해라

def dfs(x, y, z):
    # 방문 처리
    check[x][y] = True

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            # 방문 처리를 하려고 계속 돌려
            if check[nx][ny] == False and zone[nx][ny] > z:
                dfs(nx, ny, z)

n = int(input())
zone = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# max 높이들을 돌면서
for k in range(max(max(zone))):
    check = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            # 방문 안했고, 물 보다 높으면
            if check[i][j] == False and zone[i][j] > k:
                # bfs 돌려
                dfs(i, j, k)
                cnt += 1
    ans = max(ans, cnt)
print(ans)
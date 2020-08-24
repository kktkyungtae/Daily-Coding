# 백준
# https://www.acmicpc.net/problem/2468

# 해당 지역의 높이 들이 주어진다
# 비가 많이 내릴 때, 물에 잠기지 않는 영역을 찾는다
# 그 중에서 독립된 안전지역의 갯수를 구하는데,

# 안전영역의 최대 갯수를 구해라

import collections

def bfs(x, y):
    cnt = 1
    q = collections.deque()
    q.append((x,y))
    visited[x][y] = True

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False and sea[nx][ny] != 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1 # 이건 안해도되

    # bfs 돌면서, 연결된 안전지역의 갯수를 센다!
    return cnt


n = int(input())
sea = [list(map(int, input().split())) for i in range(n)]

# 영역들 찾기
li = []
for i in range(n):
    for j in range(n):
        if sea[i][j] not in li:
            li.append(sea[i][j])

li.sort()
result = 1

for k in range(len(li)):
    rain = li[k]

    # visited는 물이 차오를 때 마다 새로 갱신
    visited = [[False] * n for _ in range(n)]


    for i in range(n):
        for j in range(n):
            if sea[i][j] <= rain:
                sea[i][j] = 0

    safe = 0
    tmp_result = []
    for i in range(n):
        for j in range(n):
            # ★★★★★ visited 조건 추가해줘야지!!
            if sea[i][j] != 0 and visited[i][j] == False:
                tmp_result.append(bfs(i, j))

    # print(tmp_result)
    result = max(result, len(tmp_result))

print(result)
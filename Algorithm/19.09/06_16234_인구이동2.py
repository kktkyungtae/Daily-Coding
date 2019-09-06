# 백준
# https://www.acmicpc.net/problem/16234

# NxN 의 땅에 한칸 마다 나라가 존재한다
# 각 나라에는 숫자가 들어있는데, 인구수 이다

# 인구이동이 시작된다
# 인접한 나라의 인구차이가 L <= 차이 <= R 이하면 이동가능
# 각 칸의 인구수는 : 이동가능한 총 인구수 / 나라의 갯수 (소수점 버림)
# 이동 뒤 이동 불가

# 인구이동이 몇 번 일어나는지 구하라

def bfs(x, y):
    global cnt
    people = 0

    q = collections.deque()
    q.append((x, y))
    visited[x][y] = True

    open_li = collections.deque()
    open_li.append((x, y))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                if visited[nx][ny] == False and l <= abs(world[x][y] - world[nx][ny]) <= r:
                    q.append((x, y))
                    open_li.append((x, y))
                    cnt += 1
                    people += world[nx][ny]

    return people

def diff():
    pass


import collections

n, l, r = map(int,input().split())
world = [list(map(int, input().split())) for _ in range(n)]

# for i in world:
#     print(i)


cnt = 0
visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if world[i][j] != 0 and visited[i][j] == False:
            cnt = 1
            p = bfs(i, j) // 2
            if cnt > 1:




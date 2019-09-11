# 백준
# https://www.acmicpc.net/problem/16236

# N x N 공간에 물고기랑 아기상어가 있다
# 처음 아기상어 크기는 2 // 1초에 상하좌우로 움직인다
# 아기상어는 지보다 큰 물고기 있는 칸은 지나갈 수 없고
# 자기 보다 작은 물고기는 먹을 수 있다
# 단, 크기가 같은 물고기는 먹을 순 없어도 지나갈 순 있다

# 먹을 수 있는 물고기가 없으면 끝
# 먹을 물고기가 1마리면 먹으러 감
# 먹을 물고기가 많으면 가까운 놈 부터 먹음
# 거리는 지나야하는 칸의 갯수의 최솟값이다
# 모인 물고기 중에서는 가장 위 / 가장 왼쪽 부터 먹는다

# 아기상어는 자신의 크기 만큼의 물고기 수를 먹으면 1씩 커진다
# 몇 초 동안 먹을 수 있는지 시간을 구해라

import collections

n = int(input())
sea = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
eat_li = [[False]*n for _ in range(n)]
eat_cnt = 0
shark_size = 2

def bfs(x, y):
    global shark_size, cnt

    q = collections.deque()
    q.append((x, y))
    visited[x][y] = True

    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False and sea[nx][ny] >= shark_size:
                    visited[nx][ny] = True
                    q.append((nx, ny))

                    if sea[nx][ny] < shark_size and sea[nx][ny] != 0:
                        shark_size += 1
                        sea[nx][ny] = 0

    return cnt


def eat():
    pass

def solve():
    global visited, cnt, shark_size
    # 아기상어 위치 찾기

    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and sea[i][j] == 9:
                bfs(i, j)

    print(cnt)





solve()

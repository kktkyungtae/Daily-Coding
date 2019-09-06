# 백준
# https://www.acmicpc.net/problem/2589

# 보물지도가 주어지고
# 지도에는 육지와 바다가 있다
# 육지만 따라가서 두개의 보물 사이의 최단 거리를 구해라
# BFS로 최단 거리를 구한다. 최단 거리 중에서 가장 긴 거리가 답

# BFS 하면서 매번 이동 거리를 저장하고, 가장 큰 이동거리를 저장.
# BFS 결과로 나오는 이동 거리 중, 가장 큰 값이 답

import collections

def bfs(x, y):
    tmp_cnt = 0
    q = collections.deque()
    q.append((x, y, 0))
    visited[x][y] = True

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while q:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and mapp[nx][ny] == 'L':
                    q.append((nx, ny, cnt + 1))
                    visited[nx][ny] = True
                    tmp_cnt = max(tmp_cnt, cnt + 1)
    return tmp_cnt


n, m = map(int, input().split())
mapp = [list(input()) for _ in range(n)]

max_result = 0
for i in range(n):
    for j in range(m):
        if mapp[i][j] == 'L':
            # visit 위치 제발 생각을 좀 더 하고 넣자!!!!
            visited = [[False] * m for _ in range(n)]
            max_result = max(max_result, bfs(i, j))

print(max_result)

# visit 초기화하는 위치를 아직도 헷갈리는 것 같은데
# 잘 생각해 보면 쉽다
# for 문으로 주어진 행렬을 돌 건데
# 육지를 하나 갔잖아
# 그럼, 방문한 육지부터 새로 bfs를 시작해야되니까
# 이때 부터 다시 visit을 시작해야지
# 제일 처음에 인풋 넣을 때 해버리면 다 visit 처리 되있으니까
# 안 돌지!
# 생각 생각합시다
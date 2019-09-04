# baejoon
# https://www.acmicpc.net/problem/2573

# 바다에 빙산이 있다는 컨셉
# 주어진 높이는 줄어든는데
# 주변 0에 노출된 수만큼 줄어든다
# 한 덩어리의 빙산이 주어지는데, 덩어리가 두 덩어리 이상으로 분리되는 시간을 출력해라

import collections

def melt():
    cnt = 0
    for i in range(n):
        for j in range(m):
            minus = 0
            if sea[i][j] != 0:
                for k in range(4):
                    tmp_x = i + dx[i]
                    tmp_y = j + dy[j]

                    if 0 <= tmp_x < n and 0 <= tmp_y < m:
                        if sea[tmp_x][tmp_y] == 0:
                            minus += 1

                copy_sea[i][j] = minus

    # 녹이기
    for i in range(n):
        for j in range(m):
            # 0아니면
            if sea[i][j] != 0:
                sea[i][j] -= copy_sea[i][j]
                copy_sea[i][j] = 0

                if sea[i][j] < 0:
                    sea[i][j] = 0
            # 0이면
            else:
                copy_sea[i][j] = 0

def check():
    sums = 0
    for i in range(n):
        for j in range(m):
            if sea[i][j] != 0:
                q.append([i, j])
                visited[i][j] = True

                while q:
                    sums = 0
                    x, y = q.popleft()
                    for i in range(4):
                        temp_x = x + dx[i]
                        temp_y = y + dy[i]

                        if 0 <= temp_x < n and 0 <= temp_y < m:
                            if sea[temp_x][temp_y] > 0 and visited[temp_x][temp_y] == False:
                                q.append([temp_x, temp_y])
                                visited[temp_x][temp_y] = True
                    sums += 1
    return sums

n, m = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)]

q = collections.deque()
visited = [[False]*m for _ in range(n)]
copy_sea = [[0]*m for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

if sum(sea) == 0:
    print(0)
else:
    


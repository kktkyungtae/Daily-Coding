import collections

# 위 > 좌 > ..
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(v):
    global start_point, shark_size, total_t, cnt
    visited = [[False] * n for _ in range(n)]

    que = collections.deque()
    que.append(v)
    visited[v[0]v[1]] = True
    food = []
    state = 0



    for i in range(4):
        temp_x = start_point[0] + dx[i]
        temp_y = start_point[1] + dy[i]

        if 0 <= temp_x < n and 0 <= temp_y < n:
            if sea[temp_x][temp_y] < shark_size:
                que.appendleft([temp_x, temp_y])


n = int(input())
sea = []
start_point = 0
shark_size = 2
total_t = 0
cnt = 0

for i in range(n):
    data = list(map(int, input().split()))
    sea.append(data)

    for j, e in enumerate(data):
        if e == 9:
            start_point = [i, j]

while(True):
    condition = bfs(start_point)
    if condition == False:
        break

print(total_t)
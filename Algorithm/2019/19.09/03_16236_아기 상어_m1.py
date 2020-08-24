import collections

def bfs(v):
    global cnt, shark_size, start_point, total_t
    q = collections.deque()
    visited = [[False]*N for _ in range(N)]
    q.append(v)
    visited[v[0]][v[1]] = True
    food = []
    state = False
    level = 0

    while q:
        level += 1
        for _ in range(len(q)):
            v = q.popleft()
            for a in range(4):
                i = v[0] + di[a]
                j = v[1] + dj[a]
                if 0 <= i < N and 0 <= j < N and not(visited[i][j]):
                    visited[i][j] = True
                    if sea[i][j] == 0 or sea[i][j] == shark_size:
                        q.append([i, j])
                    elif 0 < sea[i][j] < shark_size:
                        food.append([i, j])
                        state = True
        if state:
            break
    if state:
        food.sort(key=lambda x: [x[0], x[1]])
        sea[food[0][0]][food[0][1]] = 9
        sea[start_point[0]][start_point[1]] = 0
        start_point = food[0]
        cnt += 1
        total_t += level
        if cnt == shark_size:
            shark_size += 1
            cnt = 0
    else:
        pass
    return state

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

N = int(input())
sea = []
start_point = 0
cnt = 0
shark_size = 2
total_t = 0
for i in range(N):
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
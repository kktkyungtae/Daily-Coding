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
                if 0 <= i <= N-1 and 0 <= j <= N-1 and not(visited[i][j]):
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
from collections import deque
INF = 1e9

n = int(input())
sea = []
for i in range(n):
    sea.append(list(map(int, input().split())))

# 아기 상어의 크기 및 위치 초기화
sh_size = 2
sh_x, sh_y = 0, 0

# 아기 상어 위치 찾고, 그 위치에 아무것도 없다고 처리
for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            sh_x, sh_y = i, j
            sea[sh_x][sh_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 모든 위치까지의 '최단 거리만' 계산
def bfs():
    # -1이면 도달할 수 없다고 초기화 해버려
    dist = [[-1]*n for _ in range(n)]

    # 처음 상어가 있던 위치는 갈 수 있는 곳이니 거리는 0
    q = deque([(sh_x, sh_y)])
    dist[sh_x][sh_y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 자신 크기보다 작거나 같은 경우는 지나갈 수 있다.
                if dist[nx][ny] == -1 and sea[nx][ny] <= sh_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    # 모든 위치까지의 최단 거리 맵 반환
    return dist

# 최단 거리 테이블이 주어졌을 때, 먹을 수 있는 물고기를 찾는 경우
def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # 도달 가능하고, 먹을 수 있는 물고기일 때
            if dist[i][j] != -1 and 1 <= sea[i][j] < sh_size:
                # 가장 가까운 물고기 한 마리만 선택
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]

    if min_dist == INF: # 먹을 수 있는 물고기가 없는 경우
        return None
    else:
        # 먹을 수 있는 물고기의 위치, 최단거리
        return x, y, min_dist

result = 0
eat = 0

while True:
    # 먹을 수 있는 물고기의 위치 찾기
    value = find(bfs())

    # 먹을 수 있는 물고기가 없는 경우, 현재까지 움직인 거리 출력
    if value == None:
        print(result)
        break
    else:
        # 현재 위치 갱신 및 이동거리 변경
        sh_x, sh_y = value[0], value[1]
        result += value[2]

        # 먹은 위치는 0으로 처리
        sea[sh_x][sh_y] = 0
        eat += 1

        # 자신의 현재 크기 이상으로 먹은 경우, 크기 증가
        if eat >= sh_size:
            sh_size += 1
            eat = 0

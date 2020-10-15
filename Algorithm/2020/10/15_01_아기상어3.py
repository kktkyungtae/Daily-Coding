from collections import deque
INF = 1e9 # 1과 이의 9승! 무한대를 뜻함,, 최소 거리를 갱신하기 위해

n = int(input())
sea = []
for i in range(n):
    sea.append(list(map(int, input().split())))

# 상어 초기화
sh_x, sh_y = 0, 0
sh_size = 2

dx = [-1, 0, 1, 0]
dy = [0, 1, -1, 0]

# 상어의 위치 찾기
# 위치 저장하고, 그 위치를 0으로
for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
           sh_x, sh_y = i, j
           sea[i][j] = 0

# 갈 수 있는 곳인지 판별 및 거리
def dist():
    # 일단,, 갈 수 있는 지 없는지 체크하는 dist
    dist = [[-1]*n for _ in range(n)]
    q = deque([(sh_x, sh_y)])
    # ★★★시작 위치는 0이잔아...★★★
    dist[sh_x][sh_y] = 0

    while q:
        x, y = q.popleft()

        # 시작점을 기준으로, 좌우상하 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # sea 범위 내에서
            # ★★★ 범위 헷갈리지 말자.. n이랑 같으면 안되지 바보야
            # if 0 < nx <= n and 0 < ny <= n:
            if 0 <= nx < n and 0 < ny < n:
                # 아직 방문하지 않은 dist고, 해당 sea에 물고기가 상어보다 작다면
                if dist[nx][ny] == -1 and sea[nx][ny] <= sh_size:
                    # ★★★ 시작 지점에서 부터 1씩 증가해야 하니까,
                    # 다음 지점은 시작 시점의 값에서 1을 더해줘야지
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx, ny])

    return dist


def find(dist):
    # 일단 먹을 수 있는 물고기가 어디있는지 모르니
    # 위치 초기화, 가장 가까이 있는 물고기 위치 받을 초기화
    # ★★★ 바보야 최소 거리를 업데이트 하려면,, 초기화하는 수가 커야지!!
    px, py, min_di = 0, 0, INF

    for i in range(n):
        for j in range(n):
            # -1이 아니여서 지나갈 수 있고, 상어 크기보다 작고 + !!! 일단 1보다는 커야지
            if dist[i][j] != -1 and sea[i][j] < sh_size and 1 <= sea[i][j]:
                # 그리고,, 그 고기가 있는 최소위치를 항상 초기화 해줘야지
                if min_di > dist[i][j]:
                    px, py = i, j
                    min_di = dist[i][j]

    # ★★★ 먹을 수 있는 고기가 없다는 건,,
    # min_di가 초기화가 안되었다는 거잖아!! 생각을 해 생각!
    if min_di == INF:
        return False
    else:
        # 먹을 수 있는 고기가 있는 거니까, 위치랑 거리를 넘겨
        return px, py, min_di

result = 0
eat = 0
while True:
    value = find(dist())

    if value == False:
        print(result)
        break

    else:
        px, py, min_di = value[0], value[1], value[2]
        result += min_di
        sh_x, sh_y = px, py

        # ★★★ 자꾸 조건을 까먹지 말어..
        # ★★★ 먹고 나서를 생각해야지!!

        # ★★★ 바보야.. 이것도 틀렸잖아!! 왜 먹은 걸 그 크기만큼 늘려
        # 여기서 먹는 건,, 갯수야
        # eat += sea[px][py] XXX
        eat += 1
        sea[px][py] = 0

        # 먹은게 지금 지 크기보다 커지면, 상어 레벨업 +1
        if eat >= sh_size:
            sh_size += 1
            # ★★★ 먹은 수는 다시 초기화 해줘야지 레벨업 했으면...
            # 자꾸 조건을 빠트리면, 시험치러가서 큰일난다잉...
            eat = 0

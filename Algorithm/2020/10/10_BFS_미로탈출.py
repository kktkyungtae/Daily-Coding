# 주어진 2차 배열에
# 0은 괴물이 있어서 못가는 곳
# 1은 갈 수 있는 길이다
# 탈출할 수 있는 최단 길이를 구하라

from collections import deque

s, g = map(int, input().split())
mapp = []
for i in range(s):
    mapp.append(list(map(int, input())))

def bfs(x, y):
    q = deque()
    # 일단, 시작점을 큐에 넣는다!
    q.append((x, y))

    # 큐가 빌때까지
    while q:
        x, y = q.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로의 공간 벗어나면 무시
            if nx < 0 or nx >= s or ny < 0 or ny >= g:
                continue
            if mapp[nx][ny] == 0:
                continue
            if mapp[nx][ny] == 1:
                mapp[nx][ny] = mapp[x][y] + 1
                q.append((nx, ny))

    return mapp[s-1][g-1]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))


# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
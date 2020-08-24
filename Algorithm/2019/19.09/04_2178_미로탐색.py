# baekjoon
# https://www.acmicpc.net/problem/2178

# 주어진 n,m 까지 가는 최소 칸수를 구해라
import collections

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]

# print(miro)

# 상하좌우 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 큐 만들기
q = collections.deque()

# 방문 처리
visited = [[False] * m for _ in range(n)]
result = [[0] * m for _ in range(n)]

# 시작점
# 큐에 넣고 / visited 처리하고 / 칸 수 세기
q.append((0, 0))
visited[0][0] = True
result[0][0] = 1

while q:
    x, y = q.popleft()
    for k in range(4):
        tmp_x = x + dx[k]
        tmp_y = y + dy[k]
        if 0 <= tmp_x < n and 0 <= tmp_y < m:
            if visited[tmp_x][tmp_y] == False and miro[tmp_x][tmp_y] == 1:
                q.append((tmp_x, tmp_y))
                result[tmp_x][tmp_y] = result[x][y] + 1
                visited[tmp_x][tmp_y] = True

print(result[n - 1][m - 1])
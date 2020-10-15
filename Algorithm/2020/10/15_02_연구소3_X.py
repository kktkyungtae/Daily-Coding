# 이상한거 따라 쳐가지고 이게 뭐여!!

from collections import deque
import itertools
from itertools import chain

mp, vrs = map(int, input().split())
mapp = []
for i in range(mp):
    mapp.append(list(map(int, input().split())))

# ★★★ 웬만하면 리스트에서 뺏다가 넣는거면 q로 구현하자 ★★★
vrs_xy = deque()
for i in range(mp):
    for j in range(mp):
        if mapp[i][j] == 2:
            vrs_xy.append([i,j])

def bfs(v_c):
    # 갔는지 안갔는지랑, 거리 재려고 dist
    dist = [[-1] * mp for _ in range(mp)]
    q = deque()
    # v_c 조합을 q에 넣고, 그 위치를 0으로
    for com in v_c:
        q.append(com)
        dist[com[0]][com[1]] = 0

    max_di = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < mp and 0 <= ny < mp and dist[nx][ny] != -1:
                dist[nx][ny] += dist[x][y]
                q.append([nx, ny])
                if mapp[nx][ny] == 0:
                    max_di = max(max_di, dist[nx][ny])

    # no_vist = list(chain(*dist))
    # block = list(chain(*mapp))
    # if no_vist.count(-1) == block.count(1):
    #     result.append(max_di)
    #
    no_vist = list(sum(dist, []))
    if no_vist.count(-1) == list(sum(mapp, [])).count(1):
    # 방문 안한 곳이, 벽의 갯수와 같다면!
        result.append(max_di)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = []
vi_ch = list(itertools.combinations(vrs_xy, vrs))
for i in vi_ch:
    result.append(bfs(i))

if result:
    print(result)
else:
    print(-1)
# Baekjoon
# https://www.acmicpc.net/problem/17142

# 연구소에 바이러스를 퍼트리는 데 걸리는 최소 시간을 구하는 문제
# 바이러스를 놓을 수 있는 칸은 2
# 빈칸 0에 바이러스를 모두 퍼트려야한다
# 바이러스를 모두 퍼트리는데 걸리는 최소 시간을 구해라
# 모두 퍼트릴 수 없으면 -1 출력하라

import itertools
import collections

def bfs(vp):
    global virus_count
    q = collections.deque(vp)
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    visited = [[False] * n for _ in range(n)]
    level = 0

    if virus_count:
        for e in vp:
            visited[e[0]][e[1]] = True

        while q:
            level += 1
            for _ in range(len(q)):
                v = q.popleft()
                for i in range(4):
                    nx = v[0] + dx[i]
                    ny = v[1] + dy[i]

                    if 0 <= nx < n and 0 <= ny < n:
                        if visited[nx][ny] == False and Map[i][j] != 1:
                            visited[nx][ny] = True

                            if Map[nx][ny] == 0:
                                visited -= 1
                            if virus_count == 0:
                                return level

                            q.append((nx, ny))
        return -1
    else:
        return 0



n, m = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]

virus = []
virus_reset = 0
ones = 0

ans = 99999

for i in range(n):
    for j in range(n):
        if Map[i][j] == 0:
            ones += 1
        if Map[i][j] == 2:
            virus.append((i,  j))

for virus_pick in itertools.combinations(virus, m):
    virus_count = virus_reset
    t = bfs(virus_pick)

    if t != -1:
        if ans > t:
            ans = t

if ans == 99999:
    print(-1)
else:
    print(ans)



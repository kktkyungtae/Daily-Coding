# baejoon
# https://www.acmicpc.net/problem/2573

# 바다에 빙산이 있다는 컨셉
# 주어진 높이는 줄어든는데
# 주변 0에 노출된 수만큼 줄어든다
# 한 덩어리의 빙산이 주어지는데, 덩어리가 두 덩어리 이상으로 분리되는 시간을 출력해라

import collections

def numbering(x, y):
    global visit
    q = collections.deque()
    q.append((x, y))
    mapp2 = [[0]*g for _ in range(s)]
    mapp2[x][y] = k

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < g and 0 <= ny < s:
                if mapp[nx][ny] != 0 and visit[nx][ny] == False:
                    mapp2[nx][ny] = k


def melt():
    for i in range(s):
        for j in range(g):
            if mapp[i][j] > 0:
                mapp[i][j] -= 1


s, g = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(s)]
flag = False
k = 1

def solve():
    global k
    visit = [[False] * g for _ in range(s)]
    while k < 2:
        for i in range(s):
            for j in range(g):
                if mapp[i][j] != 0 and visit[i][j] == False:
                    numbering(i, j)
                    k += 1
                    melt()

    return k

print(solve())
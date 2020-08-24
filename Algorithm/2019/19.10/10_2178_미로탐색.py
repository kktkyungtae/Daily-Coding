# baekjoon
# https://www.acmicpc.net/problem/2178

# 미로가 있는데, 이동할 수 있는 것은 1
# 이동할 수 없는 것은 0
# (1,1)에서 (N,M) 까지 가는 최소한의 길이를 구하라

import collections

s, g = map(int, input().split())
mapp = [list(map(int, input())) for _ in range(s)]
check = [[False]*g for _ in range(s)]
q = collections.deque()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(s):
    for j in range(g):
        if mapp[i][j] == 1 :
            if check[i][j] == False:
                q.append((i, j))
                check[i][j] = True

                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < s and 0 <= ny < g:
                            if mapp[nx][ny] == 1 and check[nx][ny] == False:
                                mapp[nx][ny] = mapp[x][y] + 1
                                check[nx][ny] = True
                                q.append((nx, ny))


print(mapp[s-1][g-1])

'''
4 6
101111
101010
101011
111011
'''
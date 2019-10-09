# baekjoon
# https://www.acmicpc.net/problem/2583

# 주어진 영역에 사각형들을 덮을 건데,
# 덮고 나서 안덮힌 구역의 수 및 각각의 넓이를 구하라

import collections

m, n, k = map(int, input().split())
q = collections.deque()
mapp = [[-1]*m for _ in range(n)]
check = [[False] * m for _ in range(n)]

for _ in range(k):
    q.append(list(map(int, input().split())))

k = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 사각형 그리기
def bfs():
    while q:
        li = q.popleft()
        x, y, x1, y1 = li[0], li[1], li[2], li[3]

        for i in range(x, x1):
            for j in range(y, y1):
                mapp[i][j] = 1

# 구역 나누면서 면적 구하기
def bbfs(x, y):
    check[x][y] = True
    mapp[x][y] = k
    ans = 1
    qq = collections.deque()
    qq.append((x, y))

    while qq:
        x, y = qq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if mapp[nx][ny] == -1 and check[nx][ny] == False:
                    mapp[nx][ny] = k
                    check[nx][ny] = True
                    qq.append((nx, ny))
                    ans += 1

    return ans

bfs()

result = []
for i in range(n):
    for j in range(m):
        if mapp[i][j] == -1 and check[i][j] == False:
            result.append(bbfs(i, j))
            k += 1

result.sort()

if k == 0:
    print('0')
else:
    print(k-1)

for i in result:
    print(i, end=' ')


'''
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
'''
# baekjoon
# https://www.acmicpc.net/problem/2667

# 붙어있는 단지의 수를 구해라
# 대각선은 붙어있는거 아녀

import collections


def bfs(x, y):
    cnt = 1
    q = collections.deque()
    q.append((x, y))
    # 갔으니 0으로
    apt[x][y] = 0

    while q:
        x, y = q.popleft()
        for i, j in (1,0), (-1,0), (0,1), (0,-1):
            nx = x + i
            ny = y + j

            if 0 <= nx < t and 0 <= ny < t:
                if apt[nx][ny] == '1':
                    q.append((nx, ny))
                    apt[nx][ny] = '0'
                    cnt += 1

    return cnt


t = int(input())
apt = [list(input()) for _ in range(t)]
# print(apt)

cnt = 0
result = []
for i in range(t):
    for j in range(t):
        if apt[i][j] == '1':
            result.append(bfs(i, j))

print(len(result))
result.sort()
for i in result:
    print(i)
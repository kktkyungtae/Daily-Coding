# 백준
# https://www.acmicpc.net/problem/2468

# 해당 지역의 높이 들이 주어진다
# 비가 많이 내릴 때, 물에 잠기지 않는 영역을 찾는다
# 그 중에서 독립된 안전지역의 갯수를 구하는데,

# 안전영역의 최대 갯수를 구해라

import collections

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# def check(rain):
#     tmp_result = []
#     # 기준보다 작으면 0 으로 바꾸기
#
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] <= rain:
#                 arr[i][j] = 0
#
#     vist = [[False] * n for _ in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] != 0:
#                 tmp_result.append(bfs(i, j))
#     print(len(tmp_result))
#     return len(tmp_result)

def bfs(x, y):
    global vist
    q = collections.deque()

    q.append((x, y))
    vist[x][y] = True
    cnt = 1

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if vist[nx][ny] == False and arr[nx][ny] != 0:
                    q.append((nx, ny))
                    vist[nx][ny] = True
                    cnt += 1

    return cnt

min_li = []
for i in range(n):
    for j in range(n):
        if arr[i][j] not in min_li:
            min_li.append(arr[i][j])

min_li.sort()
# print(min_li)

cnt = 0
result = 1
# print(max(result))
for a in range(len(min_li)):
    rain = min_li[a]

    tmp_result = []
    # 기준보다 작으면 0 으로 바꾸기

    for i in range(n):
        for j in range(n):
            if arr[i][j] <= rain:
                arr[i][j] = 0

    vist = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and vist[i][j] == False:
                tmp_result.append(bfs(i, j))

    # for b in arr:
    #     print(b)
    # print(tmp_result)

    result = max(result,len(tmp_result))

print(result)
# Baekjoon
# https://www.acmicpc.net/submit/16236/14931737

# 2차원 배열에 물고기 M 마리랑 아기상어 1마리가 있다
# 처음 아기상어 크기는 2 / 상하좌우로 한 칸씩 움직인다
# 아기상어는 자기보다 큰 물고기 있는 칸은 갈 수 없다
# 아기상어는 자기보다 작은 물고기는 먹을 수 있다

# 물고기를 먹으러 바다를 찾아다니는 아기상어
# 여러 물고기 중에 가장 왼쪽에 있는 물고기 부터 먹고
# 아기상어 자신의 크기만큼의 물고기를 먹으면 크기가 1씩 커진다
# 먹을 만틈 다 먹었을 때,, 몇 초 걸리는지 출력하라

import heapq

# 공간의 크기
n = int(input())
Sea = [list(map(int, input().split())) for _ in range(n)]
q = []

def init():
    for i in range(n):
        for j in range(n):
            # 아기상어 있는 위치
            if Sea[i][j] == 9:
                # 이동거리, x좌표, y좌표
                heapq.heappush(q, (0, i, j))
                Sea[i][j] = 0
                return

def bfs():
    body, eat, ans = 2, 0, 0
    visited = [[False] * n for _ in range(n)]
    
    while q:
        # d는 이동거리
        d, x, y = heapq.heappop(q)
        if 0 < Sea[x][y] < body:
            eat += 1
            Sea[x][y] = 0
            
            if eat == body:
                body += 1
                eat = 0
            
            ans += d
            d = 0

            while q:
                q.pop()
            visited = [[False] * n for _ in range(n)]

        for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
            nd, nx, ny = d + 1, x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if 0 < Sea[nx][ny] > body or visited[nx][ny] == True:
                continue
            visited[nx][ny] = True
            heapq.heappush(q, (nd, nx, ny))
    print(ans)

init()
bfs()


'''

6
6 0 6 0 6 1
0 0 0 0 0 2
2 3 4 5 6 6
0 0 0 0 0 2
0 2 0 0 0 0
3 9 3 0 0 1

14
'''
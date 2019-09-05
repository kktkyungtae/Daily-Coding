# SW Expert Academy
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# 주어진 디저트 리스트가 있는데
# 대각선으로 리스트들을 연결할 수 있다
# 연결한 것 중에 중복안되게 묶어서
# 가장 많이 디저트를 먹을 수 있도록 루트를 짜고
# 연결된 디저트 종류가 몇개인지 출력해라 / 못 먹는 경우는 -1

import collections

def bfs(x, y):
    q = collections.deque()
    q.append((x, y))
    # visit[x,y] = True
    dx = [1, 1, -1, -1]
    dy = [-1, -1, 1, 1]



    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x +



tc = int(input())
for t in range(tc):
    n = int(input())
    snack = [list(map(int, input().split())) for _ in range(n)]

    q = collections.deque()
    # 대각선의 시작을 결정

    result = []
    for i in range(n):
        for j in range(1, n-1):
            # visit = [[False]*n for _ in range(n)]
            bfs(i, j)

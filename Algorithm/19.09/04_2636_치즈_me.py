# baekjoon
# https://www.acmicpc.net/problem/2636

# 치즈가 마지막으로 남아 있을 때 시간
# 마지막에 남아 있는 치즈의 수를 구하는 문제

# 치즈를 둘러싸고 있는 마지막 껍데기는
# 공기중에 노출되었다 보고
# 1초 마다 사라진다

# sol) 0인 부분을 큐에 넣고
# 0 주변을 둘러 보면서 1이상인 놈을 +1 해준다
# 그래서 2 이상이 되면 지운다

import collections

def bfs():
    q = collections.deque()
    # 0,0 은 무조건 0이니까 넣고 시작
    q.append((0,0))
    visit = [[False]*m for _ in range(n)]
    visit[0][0] = True

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]

            if 0 <= tmp_x < n and 0 <= tmp_y < m:
                if visit[tmp_x][tmp_y] == False:
                    if chiz[tmp_x][tmp_y] >= 1:
                        chiz[tmp_x][tmp_y] += 1
                    else:
                        # 0이면 큐에 넣기!
                        q.append((tmp_x, tmp_y))
                        visit[tmp_x][tmp_y] = True

def melt():
    global remain
    flag = False
    cnt = 0
    for i in range(n):
        for j in range(m):
            if chiz[i][j] >= 2:
                chiz[i][j] = 0
                flag = True

                # 녹일 때 마다 녹인 갯수를 올리니까
                cnt += 1

    if cnt > 0:
        remain = cnt
    return flag


n, m = map(int, input().split())
chiz = [list(map(int, input().split())) for _ in range(n)]
times = 0
remain = 0

while True:
    bfs()
    if melt() == True:
        times += 1
    else:
        break

print(times)
print(remain)

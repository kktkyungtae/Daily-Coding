# baekjoon
# https://www.acmicpc.net/problem/2636

# 치즈가 마지막으로 남아 있을 때 시간
# 마지막에 남아 있는 치즈의 수를 구하는 문제

# 치즈를 둘러싸고 있는 마지막 껍데기는
# 공기중에 노출되었다 보고
# 1초 마다 사라진다
import collections

n, m = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]
# print(mapp)

visited = [[False]*m for _ in range(n)]
copy_map = [[0]*m for _ in range(n)]

#
q = collections.deque()
# 주변에 뭐있는지 보는
what = collections.deque()

# 둘러보기
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0

# 시작점 찾기
for i in range(n):
    for j in range(m):
        if mapp[i][j] == 1:
            q.append([i, j])
            break
start = q.popleft()
visited[start[0]][start[1]] = True

def change():
    global cnt
    for i in range(n):
        for j in range(m):
            if mapp[i][j] == 1:
                mapp[i][j] = 'c'
                # 처음 만나는 놈은 무조건 겉에 꺼니까
                for k in range(4):
                    tmp_i = i + dx[k]
                    tmp_j = j + dy[k]
                    if 0 <= tmp_i < m and 0 <= tmp_j < n:
                        # what에 주변에 있는 좌표들을 다 넣고
                        what.append([tmp_i, tmp_j])

                # 주변 검증
                while what:
                    tmp_q = what.popleft()
                    nx = tmp_q[0]
                    ny = tmp_q[1]
                    zero = 0
                    one = 0
                    c_num = 0

                    # 0이면 걍 pass
                    if mapp[nx][ny] == 0:
                        zero += 1

                    # 1이면 , 테두리 인지 속에 있는 것인지 확인
                    elif mapp[nx][ny] == 1:
                        one += 1
                        # for i in range(4):
                        #     tmp_nx = nx + dx[i]
                        #     tmp_ny = ny + dy[i]
                        #     if 0 <= tmp_nx < n and 0 <= tmp_ny < m:

                    elif mapp[nx][ny] == 'c':
                        c_num += 1

                    else:
                        break

                    if zero >= 2 or c_num >= 2 and zero >= 1:
                        mapp[i][j] = 'c'
    print(mapp)
    # 테두리는 다 0으로 만들기
    for i in range(n):
        cnt += 1
        for j in range(m):
            if mapp[i][j] == 'c':
                mapp[i][j] = 0

change()
print(cnt)



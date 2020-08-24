# 백준
# https://www.acmicpc.net/problem/16234

# NxN 의 땅에 한칸 마다 나라가 존재한다
# 각 나라에는 숫자가 들어있는데, 인구수 이다

# 인구이동이 시작된다
# 인접한 나라의 인구차이가 L <= 차이 <= R 이하면 이동가능
# 각 칸의 인구수는 : 이동가능한 총 인구수 / 나라의 갯수 (소수점 버림)
# 이동 뒤 이동 불가

# 인구이동이 몇 번 일어나는지 구하라

# input
n, l, r = map(int,input().split())
world = [list(map(int, input().split())) for _ in range(n)]

# check 할 놈들
visit = [[False]*n for _ in range(n)]
movie_chk = [[False]*n for _ in range(n)]
cnt = 0

def dfs(x, y):
    global cnt
    visit[x][y] = True
    shift_num = world[x][y]

    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if visit[nx][ny] == False and l <= abs(world[x][y] - world[nx][ny]) <= r:
                movie_chk[nx][ny] = True
                cnt += 1
                # 재귀
                shift_num += dfs(nx, ny)

    return shift_num

# 여기서 move_chk 에 True 인 나라 인구이동
def moving(shift_num):
    for i in range(n):
        for j in range(n):
            if movie_chk[i][j] == True:
                world[i][j] = shift_num

                # 이동 시켰으면 다시 False 로
                movie_chk[i][j] = False

# 실행할 놈
# 조건을 줄 건데, 그 조건이 만족하기 전까지는
# 계속 돌릴 거라서 함수로
def solve():
    global visit, cnt
    result = 0
    while True:

        # 요놈으로 solve 조정
        moved_end = False

        # 첫 시작은 visit 과 함께
        visit = [[False]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if visit[i][j] == False:
                    cnt = 1
                    shift_num = dfs(i, j)// cnt
                    if cnt > 1:
                        world[i][j] = shift_num
                        moving(shift_num)
                        moved_end = True

        if moved_end == True:
            result += 1
        else:
            break

    print(result)


solve()

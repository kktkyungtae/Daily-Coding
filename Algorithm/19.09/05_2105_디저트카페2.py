# SW Expert Academy
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# 주어진 디저트 리스트가 있는데
# 대각선으로 리스트들을 연결할 수 있다
# 연결한 것 중에 중복안되게 묶어서
# 가장 많이 디저트를 먹을 수 있도록 루트를 짜고
# 연결된 디저트 종류가 몇개인지 출력해라 / 못 먹는 경우는 -1

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]


# k는 방향, n은 진행한 칸수
def solve(x, y, dir, cnt):
    global nx, ny, maxV
    # 출발점에 도착한경우
    if dir == 3 and x == nx and y == dy:
        if maxV < cnt:
            maxV = cnt
    elif x < 0 or x >= N or y < 0 or y >= N:
        return
    # 숫자가 겹친경우
    elif snack[x][y] in result:
        return
    else:
        result.append(snack[x][y])
        # 오른쪽 방향 그대로 가거나 왼쪽으로 꺾었을 경우에
        if dir == 0 or dir == 1:
            solve(x + dx[dir], y + dy[dir], dir, cnt + 1)
            # dir+1방향
            solve(x + dx[dir + 1], y + dy[dir + 1], dir + 1, cnt + 1)
        elif dir == 2:
            # 출발점을 향하는게 아님
            if x + y != dx + dy:
                solve(x + dx[2], y + dy[2], dir, cnt + 1)
            else:
                solve(x + dx[3], y + dy[3], dir + 1, cnt + 1)
        # dir가 3일때는 직진한다.
        else:
            solve(x + dx[3], y + dy[3], dir, cnt + 1)

        result.remove(snack[x][y])


T = int(input())
for tc in range(T):
    N = int(input())
    snack = []
    for i in range(N):
        snack.append(list(map(int, input().split())))

    maxV = -1
    result = []
    for i in range(N):
        for j in range(1, N - 1):
            si = i
            sj = j
            result.append(snack[i][j])
            solve(i + 1, j + 1, 0, 1)
            result.remove(snack[i][j])

    print("#{} {}".format(tc + 1, maxV))
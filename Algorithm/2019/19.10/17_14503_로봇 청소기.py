# Baekjoon
# https://www.acmicpc.net/problem/14503

# 로봇 청소기가 청소하는 영역의 개수를 구해라
# 방향은 북(0), 동(1), 남(2), 서(3) 순서로 둔다.
# 로봇은 왼쪽으로만 돌기 때문에, 북(0)→서(3), 동(1)→북(0), 남(2)→동(1), 서(3)→남(2)으로 방향이 바뀐다.
# 따라서 방향 전환은 (다음 방향) = (현재 방향 + 3) % 4 로 나타낼 수 있다.
# 입력에서 청소되지 않은 칸은 (0), 벽은 (1)로 주어지므로, 이를 구분하기 위해 청소한 칸은 (2)로 바꾼다.
# 1. 위에 주어진 데로 4번 회전을 하면서 청소가 가능한 칸이 있는지 확인한다.
# 2. 청소할 수 있다면, 그 칸으로 전진하고 방향은 왔던 방향을 유지한다. 과정 1번부터 다시 반복한다.
# 3. 한 칸도 청소할 수 없다면, 회전하기 전의 처음 방향 상태가 된다. 이 방향에서 뒤 칸이 벽(1)인지 확인한다.
# 4. 만약 벽이 아니라면, 청소가 이미 된 칸(2)이므로, 뒤로 한 칸 후진한다. 과정 1번부터 다시 반복한다.
# 5. 벽이라면, 종료하고 청소한 영역의 개수를 출력한다.

n, m = map(int, input().split())
x, y, d = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]

Map[x][y] = 2

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solve(x, y, d, ans):
    while True:
        flag = False

        for _ in range(4):
            nd = (d + 3) % 4
            nx = x + dx[nd]
            ny = y + dy[nd]
            d = nd

            if Map[nx][ny] == 0:
                Map[nx][ny] = 2
                ans += 1
                x, y = nx, ny
                flag = True
                break

        if flag == False:
            if Map[x-dx[d]][y-dy[d]] == 1:
                return ans
            else:
                x, y = x - dx[d], y - dy[d]

print(solve(x, y, d, 1))
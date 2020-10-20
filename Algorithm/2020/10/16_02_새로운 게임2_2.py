# https://www.acmicpc.net/problem/17837
# 1. chess_map에 말의 번호를 쌓인 순서대로 저장하고 chess에는 말의 좌표, 방향을 저장한다
# 2. 말의 번호 순서대로 move 함수에 입력하여 이동한다
# 3. 다음 칸이 2인 경우를 먼저 처리한다
#    방향을 전환해도 2이거나 범위 밖이면 return한다
# 4. chess_set은 입력받은 번호에 해당하는 체스말과 그 위에 쌓인 체스말을 저장한다
# 5. 다음 칸이 1이면 chess_set을 뒤집는다
# 6. chess_set의 체스말을 순서대로 꺼내 다음 칸에 저장하고 이동한 체스말의 좌표를 갱신한다
# 7. 쌓인 말의 수가 4를 넘으면 1을 return한다
# 8. 1을 받으면 그동안 기록한 cnt를 출력한다

import sys

input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move(chess_num):
    x, y, z = chess[chess_num]
    nx = x + dx[z]
    ny = y + dy[z]

    if not 0 <= nx < n or not 0 <= ny < n or a[nx][ny] == 2:
        if 0 <= z <= 1:
            nz = (z+1) % 2
        else:
            nz = (z-1) % 2 + 2
        chess[chess_num][2] = nz
        nx = x + dx[nz]
        ny = y + dy[nz]
        if not 0 <= nx < n or not 0 <= ny < n or a[nx][ny] == 2:
            return 0

    chess_set = []
    for i, key in enumerate(chess_map[x][y]):
        if key == chess_num:
            chess_set.extend(chess_map[x][y][i:])
            chess_map[x][y] = chess_map[x][y][:i]
            break

    if a[nx][ny] == 1:
        chess_set = chess_set[-1::-1]

    for i in chess_set:
        chess_map[nx][ny].append(i)
        chess[i][:2] = [nx, ny]

    if len(chess_map[nx][ny]) >= 4:
        return 1
    return 0

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
chess_map = [[[] for _ in range(n)] for _ in range(n)]
chess = [0 for _ in range(k)]

for i in range(k):
    x, y, z = map(int, input().split())
    chess_map[x-1][y-1].append(i)
    chess[i] = [x-1, y-1, z-1]
print(chess_map)

chess_seet = []
for i, key in enumerate(chess_map[0][1]):
    chess_seet.extend(chess_map[0][1][i:])
print(chess_map)
cnt = 1
while cnt <= 1000:
    for i in range(k):
        flag = move(i)
        if flag:
            print(cnt)
            sys.exit()
    cnt += 1
print(-1)
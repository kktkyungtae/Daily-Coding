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

# 체스판의 크기 n, 말의 갯수 k
n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


# chess_map: 말의 번호를 순서대로 쌓는 리스트
chess_map = [[[] for _ in range(n)] for _ in range(n)]
# chess: 말의 좌표 및 방향 저장
chess = [0 for _ in range(k)]
# 하긴.. 방향이랑 좌표랑 다 들고 다니면서 확인하는 것 보다 따로 들고 다닐 거는 따로!
# 이게 풀이를 시작하기 전에 정확하게 내 풀이 방향성을 정해서 해야되고
# 좀 더 효율적이고, 직관적이고, 짜기 쉽게 해야하는데.. 이게 어렵지

for i in range(k):
    x, y, z = map(int, input().split())
    # 저장할 때 부터 요래! 굿굿
    # 저장할 때 부터 요래! 굿굿
    # k개의 말이 움직이는 순서대로 나열되어 있으니까
    # i는 말의 번호고, 그 말이 있는 위치에 찍어준다.. 대박
    chess_map[x-1][y-1].append(i)
    chess[i] = [x-1, y-1, z-1]

cnt = 1
while cnt <= 1000:
    for i in range(k):
        flag = move(i)
        if flag:
            print(cnt)
            sys.exit()
    cnt += 1
print(-1)
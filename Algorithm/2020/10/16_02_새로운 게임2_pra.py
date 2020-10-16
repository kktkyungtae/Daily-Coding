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
    # k개의 말이 움직이는 순서대로 나열되어 있으니까
    # i는 말의 번호고, 그 말이 있는 위치에 찍어준다.. 대박
    chess_map[x-1][y-1].append(i)
    chess[i] = [x-1, y-1, z-1]

print(chess_map)
print(chess)
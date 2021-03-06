# 백준
# https://www.acmicpc.net/problem/17136

# 다섯가지의 색종이가 있다.
# 1x1 / 2x2 / 3x3 / 4x4 / 5x5
# 이 색종이들을 10 x 10 종이 위에 붙일 건데 (0 1 로 구성)
# 1을 다 덮어야 되고
# 0은 덮으면 안된다
# 색종이가 종이 경계를 나가서는 안되고 / 겹쳐서도 안된다
# 1이 적힌 모든 칸을 붙이는데 필요한 색종이 최소 값을 구해라

paper = [list(map(int, input().split())) for _ in range(10)]

one = 0
for i in range(10):
    for j in range(10):
        if paper[i][j] == 1:
            one += 1

if one == 0:
    print(one)

else:

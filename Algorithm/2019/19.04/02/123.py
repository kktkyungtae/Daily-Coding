# 참외밭의 넓이
# 1. 제일 큰 가로 * 제일 큰 세로
# 2. 큰 가로와 이웃하지 않는 세로 * 큰 세로와 이웃하지 않는 가로
# 3. 값 1 - 값 2
# 참고) 이웃하지 않는 변은 인덱스 3차이

# 동쪽 - 1  서쪽 - 2
# 남쪽 - 3  북쪽 - 4

import sys

density = int(sys.stdin.readline())

squares = [0] * 6

for _ in range(6):
    squares[_] = list(map(int, sys.stdin.readline().split()))

max_w = 0
idx_w = 0
max_h = 0
idx_h = 0
# 제일 큰 가로와 세로의 값과 인덱스 구하기
for _ in range(6):
    if squares[_][0] == 1 or squares[_][0] == 2:
        if squares[_][1] > max_w:
            max_w = squares[_][1]
            idx_w = _
    else:
        if squares[_][1] > max_h:
            max_h = squares[_][1]
            idx_h = _

# 제일 작은 가로와 세로 구하기
min_h = squares[idx_w - 3][1]
min_w = squares[idx_h - 3][1]

# 면적 구하기
area = max_w * max_h - min_w * min_h

# 답 출력
print(density * area)

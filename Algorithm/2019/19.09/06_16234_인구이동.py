# 백준
# https://www.acmicpc.net/problem/16234

# NxN 의 땅에 한칸 마다 나라가 존재한다
# 각 나라에는 숫자가 들어있는데, 인구수 이다

# 인구이동이 시작된다
# 인접한 나라의 인구차이가 L <= 차이 <= R 이하면 이동가능
# 각 칸의 인구수는 : 이동가능한 총 인구수 / 나라의 갯수 (소수점 버림)
# 이동 뒤 이동 불가

# 인구이동 몇번 일어나는지 구하라

import collections

# n, l, r
n, l, r = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(n)]

# wall = [[False]*(2*n -1) for _ in range(2*n-1)]
gap = [[0]*n for _ in range(n)]
wall = [[False]*(2*n-1) for _ in range(2*n-1)]
copy_world = [[0]*(2*n-1) for _ in range(2*n-1)]
visit = [[False]*(2*n-1) for _ in range(2*n-1)]

# 길 추가한 나라 확장
for i in range(n):
    for j in range(n):
        if world[i][j] != 0:
            copy_world[i+i][j+j] = world[i][j]

# 차이를 보고 길 판단
def open():
    lets = False
    # 두 변 사이의 차이 : 가로
    for i in range(n):
        for j in range(n-1):
            tmp = abs(world[i][j] - world[i][j+1])
            if  l <= tmp <= r:
                wall[i+1][j] = True

    # 두변 사이의 차이 : 세로
    for i in range(n-1):
        for j in range(n):
            tmp = abs(world[j][i] - world[j][i-1])
            if  l <= tmp <= r:
                wall[j][i+1] = True

    if wall in True:
        return not lets
    else:
        return lets

# 인구 있는 곳 True 찍기
def pick():
    # 길 + 나라 만들기
    for i in range(n):
        for j in range(n):
            if world[i][j] != 0:
                wall[i + i][j + j] = True



for i in world:
    print(i)
print()

for i in copy_world:
    print(i)
print()

for i in wall:
    print(i)

while True:
    if
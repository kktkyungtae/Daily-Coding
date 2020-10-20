# https://www.acmicpc.net/problem/19235

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

blue_z = [[0]*6 for _ in range(4)]
green_z = [[0]*4 for _ in range(4)]

for i in range(len(matrix)):
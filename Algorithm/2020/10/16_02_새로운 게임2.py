# https://www.acmicpc.net/problem/17837

n, k = map(int, input().split())
mapp = []
for _ in range(n):
    mapp.append(list(map(int, input().split())))

ks = []
for _ in range(k):
    ks.append(list(map(int, input().split())))

for i in ks:
    i[0] -= 1
    i[1] -= 1

direction = [[0,0], [0, 1], [-1, 0], [-1, 0], [0, 1]]

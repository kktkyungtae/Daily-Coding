from sys import stdin

t = int(input())
li = []
for _ in range(t):
    li.append(list(map(int, input().split())))

li.sort()

idx = [0] * li[-1][0]

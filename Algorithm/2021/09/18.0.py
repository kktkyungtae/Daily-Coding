import sys
input = sys.stdin.readline

data = []
n = int(input())
for i in range(n):
    data.append(list(map(int, input().split())))

print(data)

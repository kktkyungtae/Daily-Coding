import sys

x = [0]*21
ans = 0
n, k = map(int, input().split())
name = []

for _ in range(n):
    name.append(len(sys.stdin.readline()[:-1]))

for i in range(k):
    x[name[i]] += 1

for i in range(n):
    x[name[i]] -= 1
    if(i+k < n):
        x[name[i+k]] += 1
    ans += x[name[i]]

print(ans)

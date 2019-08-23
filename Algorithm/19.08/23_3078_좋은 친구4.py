from sys import*
from collections import deque
input = lambda:stdin.readline().strip()

n, k = map(int, input().split())
arr = []
res = 0
for i in range(21):
    arr.append(deque())

for i in range(n):
    length = len(input())
    chk = 0
    for j in arr[length]:
        if i-j > k:
            chk += 1
        else:
            break
    for j in range(chk):
        arr[length].popleft()
    res += len(arr[length])
    arr[length].append(i)

print(res)

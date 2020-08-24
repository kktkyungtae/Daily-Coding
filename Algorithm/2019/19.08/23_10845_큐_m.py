# Baekjoon

# 큐를 만들어라

nums = int(input())

from collections import deque

dos = []
for i in range(nums):
    temp = list(input().split())
    dos.append(temp)

ans = deque()

for j in dos:
    if len(j) == 2:
        if j[0] == 'push':
            ans.append(int(j[1]))
    else:
        if j[0] == 'front':
            print(ans[0])
        elif j[0] == 'back':
            print(ans[-1])
        elif j[0] == 'size':
            print(len(ans))
        elif j[0] == 'empty':
            if len(ans) == 0:
                print(1)
            else:
                print(0)
        else:
            if len(ans) == 0:
                print(-1)
            else:
                print(ans[0])
                ans.popleft()


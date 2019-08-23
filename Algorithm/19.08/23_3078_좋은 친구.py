from collections import deque
import sys
input=sys.stdin.readline
N,K=map(int,input().split())
Que = [deque([]) for _ in range(21)]
ans=0
for i in range(N):
	L=len(input().rstrip())
	while Q[L] and i-Que[L][0]>K:Que[L].popleft()
	ans+=len(Que[L])
	Que[L].append(i)
print(ans)
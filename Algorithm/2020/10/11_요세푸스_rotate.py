# deque에는 rotate() 메서드가 있다
# 인자가 음수면 왼쪽으로 회전하고
# 인자가 양수면 오른쪽을 회전한다
# table = deque([a,b,c])
# table.rotate(1) >> [c, a, b]
# table.rotate(-1) >> [b, c, a]

from collections import deque
N, K = map(int, input().split())
q = deque([i for i in range(1, N+1)])
res = []
while q:
    q.rotate(-K+1)
    res.append(q.popleft())

print("<"+", ".join(map(str, res))+">")

# 군인 코드 짱짱

import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().strip().split())

edge = [[] for ii in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    edge[a].append(b)
    edge[b].append(a)

for i in range(n + 1):  # 오름차순으로 정렬
    edge[i].sort()


def DFS():
    result = deque()
    stack = deque([v])
    visit = [0 for i in range(n + 1)]
    while stack:
        node = stack.popleft()
        if visit[node]:
            pass
        else:
            visit[node] = 1
            result.append(node)
            stack = deque(edge[node]) + stack
    return result


def BFS():
    result = deque()
    que = deque([v])
    visit = [0 for i in range(n + 1)]
    visit[v] = 1
    while que:
        node = que.popleft()
        result.append(node)
        for i in edge[node]:
            if visit[i]:
                continue
            visit[i] = 1
            que.append(i)
    return result


print(" ".join(map(str, DFS())))
print(" ".join(map(str, BFS())))


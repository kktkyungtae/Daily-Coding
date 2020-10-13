# 이거... DFS에서 stack이 q로 구현되어 있는게
# 아마도 낮은차수? 방문해야 되서 그런거 같애
# 처음에 sort했고, DFS 돌떄도 오름차순으로 해야되니까
# 뒤에 방문한 곳을 앞에 넣고 popleft 하는 듯
# 그런 느낌적 느낌

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
    stack = []
    visit = [0 for i in range(n + 1)]
    while stack:
        node = stack.pop()
        if visit[node]:
            pass
        else:
            visit[node] = 1
            result.append(node)
            stack = stack + edge[node]
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


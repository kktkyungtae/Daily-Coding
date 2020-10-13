# BFS와 DFS 탐색 결과를 출력하시오

from collections import deque

jj, gs, start = map(int, input().split())
graph = [[] for _ in range(jj + 1)]

for j in range(gs):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# for a in range(len(graph)):
#     sorted(graph[a])

## 이 sort 하나 때문에 계속 틀렸잖아!!!!
for i in range(jj+1):
    graph[i].sort()

def dfs(graph, s, visted):
    #현재 노드를 방문처리
    visted[s] = True
    print(s, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[s]:
        if not visted[i]:
            dfs(graph, i, visted)

def bfs(graph, start, vvisited):
    # deque에서 int는 ((int)) 안돼...
    q = deque([start])
    vvisited[start] = True

    while q:
        k = q.popleft()
        print(k, end=' ')

        for i in graph[k]:
            if not vvisited[i]:
                q.append(i)
                vvisited[i] = True


visted = [False] * len(graph)
vvisited = [False] * len(graph)

dfs(graph, start, visted)
print()
bfs(graph, start, vvisited)
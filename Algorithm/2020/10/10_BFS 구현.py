from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

def bfs(graph, s, visited):
    queue = deque([s])
    visted[s] = True

    # 큐가 차있는 동안만!
    while queue:
        check = queue.popleft()
        # 방문 순서 출력
        print(check, end = ' ')

        # 아직 방문하지 않은 인접한 원소들 큐에 삽입
        for i in graph[check]:
            if not visted[i]:
                queue.append(i)
                visited[i] = True

visted = [0*False for i in range(len(graph))]
bfs(graph, 1, visted)
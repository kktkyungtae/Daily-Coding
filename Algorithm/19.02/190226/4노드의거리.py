T = int(input())

for t in range(T):
    V, E = map(int, input().split())
    tree = [[] * (V + 1) for x in range(V+1)]

    for e in range(E):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    S, G = map(int, input().split())

    visited = [False] * (V+1)

    queue = [[S, 0]]
    visited[S] = True
    result = 0

    while queue:
        node = queue.pop(0)

        if node[0] == G:
            result = node[1]

        for n in tree[node[0]]:
            if not visited[n]:
                queue.append([n, node[1] + 1])
                visited[n] = True

    print(f"#{t + 1} {result}")
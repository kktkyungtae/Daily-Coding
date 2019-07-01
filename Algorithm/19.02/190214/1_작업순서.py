import sys
sys.stdin = open("작업순서.txt","r")

for t in range(10):
    V, E = map(int, input().split())
    temp_edge = list(map(int, input().split()))
    li_edge = [[] for v in range(V)]
    
    for e in range(0, E*2, 2):
        li_edge[temp_edge[e]-1].append(temp_edge[e+1]-1)

    in_degree = [0 for v in range(V)]

    for edge in li_edge:
        for e in edge:
            in_degree[e] += 1

    result = ''
    stack = []

    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            stack.append(i)

    while stack:
        node_v = stack.pop()
        node_k = []
        for k in li_edge[node_v]:
            in_degree[k] -= 1
            node_k.append(k)

        for k in node_k:
            if in_degree[k] == 0:
                stack.append(k)
        
        result += str(node_v+1) + ' '

    print(f"#{t+1} {result}")
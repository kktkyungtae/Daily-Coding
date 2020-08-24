import sys
sys.stdin = open("그래프경로.txt","r")

T = int(input())

for t in range(T):
    V, E = map(int, input().split())
    li_edge = [[] for v in range(V)]
    result = '0'

    for e in range(E):
        v_start, v_end = map(int, input().split())
        li_edge[v_start-1].append(v_end-1)

    S, G = map(int, input().split())

    stack = []
    stack.append(S-1)

    while stack:
        breaker = False
        node_v = stack.pop()
        
        for node_k in li_edge[node_v]:
            if node_k == (G-1):
                result = '1'
                braker = True
                break
            else:
                stack.append(node_k)

        if breaker:
            break

    print(f"#{t+1} {result}")
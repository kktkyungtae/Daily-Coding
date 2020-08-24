import sys
sys.stdin = open("그래프경로.txt", "r")

top = -1
result = False
def dfs(st,en):
    
    global top
    global result
    if not visited[st]:
        top += 1
        stack[top] = st

    visited[st] = True

    if True == visited[en]:
        return True

    for i in range(len(matrix)):
        if matrix[st][i] and not visited[i]:
            result = dfs(i,en)
            if result:
                break
    
    if stack[0] != 0:
        i = stack.pop(top)
        top -= 1
        dfs(i,en)
    
    if result:
        return 1
    return 0

T = int(input())
for test_case in range(1, T+1):
    V,E = list(map(int,input().split()))
    number = [0]*E*2
    matrix = [[0] * (V+1) for x in range(V+1)]
    visited, stack = [0]*(V+1),[0]*(V+1)
    top = -1
    result = False
    i = 0
    for _ in range(E):
        number[i], number[i+1] =  list(map(int,input().split()))
        i += 2

    S,G = list(map(int,input().split()))
    
    for i in range(0, len(number), 2):
        matrix[number[i]][number[i+1]] = 1
    
    print(f'#{test_case} {dfs(S,G)}')
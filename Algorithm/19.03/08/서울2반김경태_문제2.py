T = int(input())

for test_case in range(T):
    N = int(input())
    som = []
    for n in range(N):
        som.append(list(map(int,input().split())))

    visited = [[False]*N for i in range(N)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0 ,0]
    result = []

    for i in range(N):
        for j in range(N):
            if not som[i][j]:
                visited[i][j] = True

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                stack = []
                stack.append((i, j, som[i][j]))
                visited[i][j] = True
                max_h = som[i][j]

                while stack:
                    value = stack.pop()

                    for k in range(4):
                        x = value[0] + dx[k]
                        y = value[1] + dy[k]

                        if 0 <= x < N and 0 <= y < N:
                            if not visited[x][y]:
                                stack.append((x, y, som[x][y]))
                                visited[x][y] = True
                                if max_h < som[x][y]:
                                    max_h = som[x][y]

                result.append(max_h)

    if result :
        print("#{} {} {}".format(test_case+1, len(result), max(result)))
T = int(input())

for t in range(T):
    N = int(input())
    maze = []
    for n in range(N):
        msg = input()
        maze.append([int(x) for x in msg])

    visited = [[False] * N for x in range(N)]

    start = ()
    end = ()

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 1:
                visited[i][j] = True
            elif maze[i][j] == 2:
                start = (i, j, 0)
            elif maze[i][j] == 3:
                end = (i, j, 0)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0

    if start and end:
        queue = []
        queue.append(start)
        visited[start[0]][start[1]] = True

        while queue:
            x, y, cnt = queue.pop(0)

            if x == end[0] and y == end[1]:
                result = cnt
                break

            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]

                if new_x >= 0 and new_y >= 0 and new_x < N and new_y < N:
                    if not visited[new_x][new_y]:
                        queue.append((new_x, new_y, cnt + 1))
                        visited[new_x][new_y] = True

    print(f"#{t + 1} {0 if result == 0 else result - 1}")
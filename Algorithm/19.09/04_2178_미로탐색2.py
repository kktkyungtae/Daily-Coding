import collections

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def bfs(v):
    # q = [v]
    q = collections.deque(v)
    level = 0
    state = False
    while q:
        level += 1
        for _ in range(len(q)):
            v = q.pop(0)
            if v == (N, M):
                state = True
                break
            if maze[v[0]][v[1]] == '1':
                maze[v[0]][v[1]] = '0'
                for a in range(4):
                    if maze[v[0]+di[a]][v[1]+dj[a]] == '1':
                        q.append((v[0]+di[a], v[1]+dj[a]))
        if state:
            break
    print(level)

N, M = map(int, input().split())
# maze = [['0'] * (M + 2)]  + [list('0'+input()+'0') for _ in range(N)] + [['0'] * (M + 2)]
maze = [list(map(int, input())) for _ in range(N)]

print(maze)
bfs((1,1))
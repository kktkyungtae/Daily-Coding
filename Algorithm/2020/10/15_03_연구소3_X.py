import itertools
def bfs(case):
    global result
    remain_cnt, min_d = 0, 0
    b = [[-1] * N for _ in range(N)]
    q = []
    for c in case:
        (cx,cy) = m[c]
        q.append(m[c])
        b[cy][cx] = 0

    while(q):
        (px,py) = q.pop(0)
        for way in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            next_x = px + way[0]
            next_y = py + way[1]
            if (0<=next_x<N and 0<=next_y<N):
                if(x[next_y][next_x] != 1 and b[next_y][next_x] == -1):
                    b[next_y][next_x] = b[py][px] + 1
                    q.append((next_x,next_y))
                    if(x[next_y][next_x] == 0):
                        remain_cnt += 1
                        min_d = b[next_y][next_x]
    if(r_cnt == remain_cnt):
        result = min(result, min_d)

N, M = map(int, input().split())
x = [[0]*N for _ in range(N)]
m = [0]*10
m_cnt, r_cnt = 0, 0
result = 999999
for i in range(N):
    in_row = list(map(int, input().split()))
    for j in range(N):
        x[i][j] = in_row[j]
        if(x[i][j] == 2):
            m[m_cnt] = (j, i)
            m_cnt+=1
        elif(x[i][j] == 0):
            r_cnt+=1
combi = list(itertools.combinations(list(range(m_cnt)), M))
for case in combi:
    bfs(case)

print(result if result != 999999 else -1)
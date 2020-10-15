#
from collections import deque

sero, garo = map(int, input().split())
mapp = []
for _ in range(sero):
    mapp.append(list(map(int, input())))

def bfs():
    q = deque()
    q.append([0,0])
    vsit[0][0] = True

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]

            if tmp_x >= sero or tmp_x < 0 or tmp_y >= garo or tmp_y <0:
                continue
            if mapp[tmp_x][tmp_y] == 1 and vsit[tmp_x][tmp_y] == False:
                vsit[tmp_x][tmp_y] = True
                q.append((tmp_x, tmp_y))
                mapp[tmp_x][tmp_y] = mapp[x][y]+1

    return mapp[sero-1][garo-1]

vsit = [[False] *garo for i in range(sero)]
print(bfs())
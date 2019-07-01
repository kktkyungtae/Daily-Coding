import sys
sys.stdin = open('1_othello.txt','r')


def get_goro(x,y,bw):
    # 오른쪽
    t = x
    for i in range(x+1,N+1):

        if ground_li[i][y] == bw:
            t = i
            break
        elif ground_li[i][y] == 0:
            break

    for j in range(x+1,t+1):
        ground_li[j][y] = bw

    # 왼쪽
    t = x
    for i in range(x-1,0,-1):

        if ground_li[i][y] == bw:
            t = i
            break
        elif ground_li[i][y] == 0:
            break

    for j in range(t,x):
        ground_li[j][y] = bw



def get_sero(x,y,bw):
    # 위
    t = y
    for i in range(y+1,N+1):
        if ground_li[x][i] == 0:
            break
        elif ground_li[x][i] == bw:
            t = i
            break
    for j in range(x+1,t+1):
        ground_li[x][j] = bw


    t = y
    # 아래
    for i in range(y-1,0,-1):
        if ground_li[x][i] == 0:
            break
        elif ground_li[x][i] == bw:
            t = i
            break
    for j in range(t,y):
        ground_li[x][j] = bw


def get_daegak(x,y,bw):
    # 위 - 오른쪽
    t = 0
    for i in range(1, min(N-x,N-y)+1):
        if x+1 <= N and y+i <=N:
            if ground_li[x+i][y+i] == 0:
                break
            elif ground_li[x+i][y+i] == bw:
                t = i
                break
    for j in range(1, t+1):
        if x+j <= N and y+j <=N:
            ground_li[x+j][y+j] = bw

    # 위 - 왼쪽
    t = 0
    for i in range(1, min(x, y) + 1):
        if x-i > 0 and y - i > 0:
            if ground_li[x-i][y-i] == 0:
                break
            elif ground_li[x-i][y-i] == bw:
                t = i
                break
    for j in range(1, t+1):
        if x-y > 0 and y - j > 0:
            ground_li[x-j][y-j] = bw


    # 아래 - 오른쪽
    t = 0
    for i in range(1, min(x,N-y)+1):
        if x-1 > 0 and y+i <=N:
            if ground_li[x-i][y+i] == 0:
                break
            elif ground_li[x-i][y+i] == bw:
                t = i
                break
    for j in range(1, t+1):
        if x-j > 0  and y+j <=N:
            ground_li[x-j][y+j] = bw

    # 아래 - 왼쪽
    t = 0
    for i in range(1, min(N-x, y) + 1):
        if x + i <= N and y - i > 0:
            if ground_li[x+i][y-i] == 0:
                break
            elif ground_li[x+i][y-i] == bw:
                t = i
                break
    for j in range(1, t+1):
        if x + j <= N and y - j > 0:
            ground_li[x+j][y-j] = bw

T = int(input())

for tc in range(T):
    N, M = map(int,input().split())
    ground_li = [[0]*(N+1) for _ in range(N+1)]
    ground_li[(N//2)+1][(N//2)] = 1
    ground_li[(N//2)][(N//2)] = 2
    ground_li[(N//2)+1][(N//2)+1] = 2
    ground_li[(N//2)][(N//2)+1] = 1

    for j in range(M):
        x,y,bw = map(int,input().split())
        ground_li[x][y] = bw
        get_daegak(x,y,bw)
        get_goro(x,y,bw)
        get_sero(x,y,bw)

    xx = 0
    yy = 0

    for i in range(N+1):
        for j in range(N+1):
            if ground_li[i][j] == 1:
                xx+=1
            elif ground_li[i][j] == 2:
                yy+=1


    print('#{} {} {}'.format(tc+1,xx,yy))
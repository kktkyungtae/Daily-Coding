# 점수표에 따른 축구팀 짜기

import sys
sys.stdin = open('14889_input.txt','r')

T = int(input())
    for tc in range(T):
    N = int(input())
    s_mat = []
    for i in range(N):
        s_mat.append(list(map(int,input().split())))

    start = []
    link = []
    sl_plus = []
    result = []
    for g in range(N-1):
        for s in range(1+g,N):
            start.append(s_mat[g][s])

    for s in range(N-1):
        for g in range(1+s,N):
            link.append(s_mat[g][s])

    for k in range(0,len(start)):
        sl_plus.append(abs(link[k]+start[k]))

    for m in range(len(start)//2):
        result.append(abs((sl_plus[m] - sl_plus[len(start)-1-m])))

    print(min(result))


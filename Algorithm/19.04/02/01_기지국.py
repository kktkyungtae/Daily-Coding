# a:1 b:2 c:3 기지국 상하좌우 커버리지

import sys
sys.stdin = open('input/01_input.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())

    mapp = []
    for i in range(N+1):
        temp_map = list(map(str,input()))
        mapp.append(temp_map)

    for s in range(N+1):
        for g in range(N):

            if mapp[s][g] == 'A':
                dx = [0, 1, 0, -1]
                dy = [1, 0, -1, 0]
                for i in range(len(dx)):
                    if 0 <= g + dx[i] <= N and 0 <= s + dy[i] <= N + 1:
                        if mapp[s + dx[i]][g + dy[i]] == 'H':
                            mapp[s + dx[i]][g + dy[i]] = 'X'

            elif mapp[s][g] == 'B':
                dx = [0, 1, 0, -1, 0, 2, 0, -2]
                dy = [1, 0, -1, 0, 2, 0, -2, 0]
                for i in range(len(dx)):
                    if 0 <= g + dx[i] <= N and 0 <= s + dy[i] <= N + 1:
                        if mapp[s + dx[i]][g + dy[i]] == 'H':
                            mapp[s + dx[i]][g + dy[i]] = 'X'

            elif mapp[s][g] == 'C':
                dx = [0, 1, 0, -1, 0, 2, 0, -2, 0, 3, 0, -3]
                dy = [1, 0, -1, 0, 2, 0, -2, 0, 3, 0, -3, 0]
                for i in range(len(dx)):
                    if 0 <= g + dx[i] <= N and 0 <= s + dy[i] <= N + 1:
                        if mapp[s + dx[i]][g + dy[i]] == 'H':
                            mapp[s + dx[i]][g + dy[i]] = 'X'

    H_cnt = 0
    for h in range(N+1):
        for k in range(N):
            if mapp[h][k] == 'H':
                H_cnt += 1

    print("#{} {}".format(tc+1, H_cnt))

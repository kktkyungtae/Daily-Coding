import sys
sys.stdin=open('input/08.txt','r')

T = int(input())

for t in range(T):
    N, K = map(int, input().split())

    matrix = []
    for n in range(N):
        matrix.append(list(map(int, input().split())))

    result = 0

    # 가로 검색
    for i in range(N):
        cnt = 0
        blank_cnt = []
        for j in range(N):
            if matrix[i][j] == 1:
                cnt += 1
            else:
                blank_cnt.append(cnt)
                cnt = 0
        blank_cnt.append(cnt)
        for c in blank_cnt:
            if c == K:
                result += 1

    # 세로 검색
    for j in range(N):
        cnt = 0
        blank_cnt = []
        for i in range(N):
            if matrix[i][j] == 1:
                cnt += 1
            else:
                blank_cnt.append(cnt)
                cnt = 0
        blank_cnt.append(cnt)
        for r in blank_cnt:
            if r == K:
                result += 1

    print("#{} {}".format(t + 1, result))
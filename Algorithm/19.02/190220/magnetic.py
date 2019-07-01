import sys
sys.stdin = open('magnetic.txt','r')

for t in range(10):
    li = []
    N = int(input())
    for i in range(N):
        li.append(list(map(int, input().split())))

    li_N = [-1] * N
    li_S = [-1] * N

    for i in range(N):
        for j in range(N):
            if li_N[j] == -1 and li[i][j] == 1:
                li_N[j] = i

    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if li_S[j] == -1 and li[i][j] == 2:
                li_S[j] = i

    result = 0
    for x in range(N):
        if li_N[x] == -1 or li_S[x] == -1:
            continue
        else:
            now = 1
            for y in range(li_N[x], li_S[x] + 1):
                if now == 1 and li[y][x] == 2:
                    result += 1
                    now = 2
                elif li[y][x] == 1:
                    now = 1

    print(f"#{t + 1} {result}")
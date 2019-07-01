T = int(input())

for tc in range(T):
    N,K = map(int,input().split())

    game_pan = []
    for s in range(N):
        li = list(map(int,input().split()))
        game_pan.append(li)

    result = 0
    min_1 = 0
    r_daegak = 0
    l_daegak = 0

    for x in range((N-K)+1):
        for y in range((N - K) + 1):
            for r in range(1,K):
                r_daegak += game_pan[x+r][y+r]
        for y in range((N-K)+1,N):
            for l in range(1,K):
                l_daegak += game_pan[x-l][y-l]
        min_1 = r_daegak - l_daegak

    if result > min_1:
        result = min_1

    print('#{} {}'.format(tc+1, result))
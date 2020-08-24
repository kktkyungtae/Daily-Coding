import sys
sys.stdin = open('전기버스.txt', 'r')

T = int(input())

for t in range(T):
    K, N, M = map(int, input().split())
    li_M = list(map(int, input().split()))

    charge = 0
    now = 0
    error_break = False

    while (now != N):
        for i in range(K):
            if now + K - i in li_M:
                now = now + K - i
                charge += 1
                break
            elif i == K - 1:
                error_break = True
                break

            if now + K - i == N:
                now = now + K - i
                break
        if error_break:
            charge = 0
            break

    print(f"#{t + 1} {charge}")
import sys
sys.stdin = open('04_input.txt','r')

T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    ki = list(map(int, input().split()))
    minval = sum(ki)

    for i in range(1<<N):
        result = 0
        for j in range(N):
            if i & (1 << j):
                result += ki[j]
        if result == B:
            minval = result
            break
        elif result > B:
            if result < minval:
                minval = result
        elif result < B:
            continue
    print("#{} {}".format(tc+1, minval-B))
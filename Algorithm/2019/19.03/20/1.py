# 정은

import sys
sys.stdin = open('input.txt','r')

keys = ['0001101', '0011001', '0010011', '0111101', '0100011',
        '0110001', '0101111', '0111011', '0110111', '0001011']

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    G = []
    for i in range(N):
        G.append(input())

    r = []
    for i in G:
        j = len(i)
        while j > 0:
            if int(i) == 0: break
            if i[j - 7:j] in keys:
                r.append(keys.index(i[j - 7:j]))
                j -= 7
                continue
            j -= 1
        else:
            break

    sum1 = result = ans = 0

    for i in range(len(r)):
        if i % 2 == 1:
            sum1 += r[i]
        else:
            result += r[i]
    result += sum1 * 3

    if result % 10 == 0:
        for i in r:
            ans += i
    else:
        ans = 0
    print(f"#{t} {ans}")
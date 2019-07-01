# 한성

import sys
sys.stdin = open('input.txt','r')


pattern = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    li = []
    for n in range(N):
        li.append(list(input()))

    code = ''

    for n in range(N):
        if '1' in li[n]:
            for i in range(M - 1, -1, -1):
                if li[n][i] == '1':
                    code = ''.join(li[n][i - 55:i + 1])
                    break
            break

    result = []
    for i in range(0, len(code), 7):
        result.append(pattern.get(''.join(code[i:i + 7])))

    num = 0
    for i in range(len(result)):
        if i == len(result) - 1:
            num += result[i]
        elif i % 2:
            num += result[i]
        else:
            num += result[i] * 3

    if not num % 10:
        print("#{} {}".format(t + 1, sum(result)))
    else:
        print("#{} 0".format(t + 1))
# 늘어지는 소리 만들기

import sys
sys.stdin = open('input/04_input.txt','r')

t = int(input())
for tc in range(t):
    strs = list(str(input())) # 문자열을 리스트로 한 문자씩 나눠서 받기

    h = int(input())
    inserts = list(map(int, input().split()))
    inserts.sort()
    inserts.reverse()

    cnt = 0
    temp = 0
    while h != cnt:
        for i in inserts:
            strs.insert(i,'-')
            cnt += 1
            temp += 1

    print("#{}".format(tc+1), end= ' ')
    for j in strs:
        print(j, end='')
    print()
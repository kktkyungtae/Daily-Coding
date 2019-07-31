# Baekjoon

# 주어진 괄호 문자열이 VPS 인지 아닌지 판단해라

from collections import deque
vps = deque()

tc = int(input())
for t in range(tc):
    lists = list(input())

    if lists.count('(') == lists.count(')'):
        for i in lists:
            if i == '(':
                vps.append(i)
            else:
                if vps:
                    vps.pop()
                else:
                    vps.append(i)
    elif lists[0] == '(':
        print('NO')
    else:
        print('NO')


    if len(vps) == 0:
        print('YES')
    else:
        print('NO')
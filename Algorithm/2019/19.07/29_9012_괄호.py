# Baekjoon

# 주어진 괄호 문자열이 VPS 인지 아닌지 판단해라

from collections import deque


tc = int(input())
for t in range(tc):
    vps = deque()
    lists = list(input())

    for s in lists:
        if s == '(':
            vps.append(s)
        elif s == ')':
            if len(vps) == 0:
                vps.append(s) # 추가 해도 된다. 왜냐면 못 빼면 어짜피 vps가 아닌 거니까
            elif vps[-1] == '(': # 이 부분을 생각 못했다.
                vps.pop() # 뺄 때 그냥 빼는게 아니라 아다리가 맞을 때만 빼는게 맞는 방법이었다.

    if len(vps) == 0:
        print('YES')
    else:
        print('NO')
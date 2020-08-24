# # Baekjoon
#
# # 숫자를 뒤집기 + (0)번째 버리기 해서 출력해라
#
# from collections import deque
#
# tc = int(input())
# for t in range(tc):
#     func = list(input())
#     lens = int(input())
#     li_tmp = deque(eval(input()))
#
#     reverse = 0
#     delete = 0
#
#     for i in func:
#         if i == 'R':
#             if lens > 0: # 문자가 있으면
#                 reverse += 1
#             else: # 문자가 없으면
#                 print('error')
#                 break
#         else:
#             if len(li_tmp) > 0:
#                 li_tmp.popleft()
#             else:
#                 print('error')
#                 break
#
#
#
#

# print("["+",".join(d)+"]")

# Baekjoon

# 숫자를 뒤집기 + (0)번째 버리기 해서 출력해라

from collections import deque

tc = int(input())
while tc > 0:
    func = input()
    lens = int(input())
    li = deque(s for s in input()[1:-1].split(',') if s)
    reverse = False
    error = False
    for op in func:
        if op == 'R':
            reverse = not reverse
        elif op == 'D':
            if not li:
                error = True
                break
            if reverse:
                li.pop()
            else:
                li.popleft()
        else:
            pass

    result = list(li if not reverse else reversed(li))
    ans = (f'[{",".join(result)}]' if not error else 'error')
    print(ans)
    tc -= 1

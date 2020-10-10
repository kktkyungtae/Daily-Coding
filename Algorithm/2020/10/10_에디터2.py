from collections import deque

words = input()
tc = int(input())
left = deque(words)
right = deque()

def solution(act):
    if len(act) == 3:
        left.append(act[2])
    else:
        if act == 'L': # 커서 왼쪽으로
            if left:
                tmp = left.pop()
                right.appendleft(tmp)
        elif act == 'D': # 커서 오른쪽으로
            if right:
                tmp = right.popleft()
                left.append(tmp)
        else:
            if left:
                left.pop()

for i in range(tc):
    act = input()
    solution(act)

print("".join(left + right))
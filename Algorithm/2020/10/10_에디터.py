# Baekjoon

from collections import deque

word = input()
tc = int(input())
left = deque(word)
right = deque()

edit = []
def something(inp):
    if len(inp) == 3:
        first, second, third = inp[0], inp[1], inp[2]
        left.append(third)
        # 새로운 사실!! 문자열은 리스트로 안받아도 0,1,2 인덱스로 부를 수 있다!!
    else:
        if inp == 'L':  # 커서 왼쪽으로 옮기기
            if len(left) != 0:
                tmp = left.pop()
                right.appendleft(tmp)
        elif inp == 'D':  # 커서 오른쪽으로 옮기기
            if right:
                tmp = right.popleft()
                left.append(tmp)
        else:
            if left:  # 왼쪽에 있는 문자 삭제
                left.pop()


for t in range(tc):

    inp = input()
    something(inp)



print("".join(left + right))
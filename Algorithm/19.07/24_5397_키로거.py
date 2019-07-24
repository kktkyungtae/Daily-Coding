from collections import deque

tc = int(input())
for i in range(tc):
    word = input()
    left = deque()
    right = deque()
    for x in word:
        if x == '<':
            if left :
                tmp = left.pop()
                right.appendleft(tmp)
        elif x == '>': #아.. 비밀번호니까 right에 저장되있는 것이 없으면
            if right:
                tmp = right.popleft() # 마지막에 입력한 문자가 어짜피 마지막 문자
                left.append(tmp) # 그래서 있으면 뽑아서 걍 붙여주면 돼
        elif x == '-':
            if left:
                left.pop()
        else:
            left.append(x)

    print("".join(left + right))
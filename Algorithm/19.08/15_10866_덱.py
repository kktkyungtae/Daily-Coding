from collections import deque

li = deque()

for _ in range(int(input())):
    temp_do = list(input().split(' '))
    if temp_do[0] == 'push_back':
        li.append(temp_do[1])
    elif temp_do[0] == 'push_front':
        li.appendleft(temp_do[1])
    elif temp_do[0] == 'pop_front':
        if len(li) == 0:
            print(-1)
        else:
            print(li.popleft())
    elif temp_do[0] == 'pop_back':
        if len(li) == 0:
            print(-1)
        else:
            print(li.pop())
    elif temp_do[0] == 'size':
        print(len(li))
    elif temp_do[0] == 'empty':
        if len(li) == 0:
            print(-1)
        else:
            print(0)
    elif temp_do[0] == 'front':
        if len(li) == 0:
            print(-1)
        else:
            print(li[0])
    elif temp_do[0] == 'back':
        if len(li) == 0:
            print(-1)
        else:
            print(li[-1])

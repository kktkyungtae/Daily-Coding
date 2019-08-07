# Baekjoon

# 1. pop(0)
# 2. 왼쪽으로 한칸씩 밀기
# 3. 오른쪽으로 한칸씩 밀기
# 원하는 숫자를 1. 하고 싶은데 2,3 최소로 몇번 돌려야하냐

from collections import deque

n, m = map(int, input().split())
pick = deque(map(int, input().split()))

num_li = deque(i for i in range(1, n + 1))

cnt = 0
while len(pick) != 0:
    if pick[0] == num_li[0]:
        cnt += 0
        pick.popleft()
        num_li.popleft()
    else:
        p = num_li.index(pick[0]) + 1
        k = (len(num_li) // 2) - 1
        if p > k:
            while pick[0] != num_li[0]:
                num_li.appendleft(num_li.pop())
                cnt += 1
            pick.popleft()
            num_li.popleft()
        elif p < k:
            while pick[0] != num_li[0]:
                num_li.append(num_li.popleft())
                cnt += 1
            pick.popleft()
            num_li.popleft()
        else:
            while pick[0] != num_li[0]:
                num_li.append(num_li.popleft())
                cnt += 1
            pick.popleft()
            num_li.popleft()

print(cnt)


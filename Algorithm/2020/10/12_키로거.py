# https://www.acmicpc.net/problem/5397
# <, >, - 주어지는데
# 입력된 비밀번호를 찾는 프로그램을 만들어
from collections import deque

tc = int(input())

words = []
for t in range(tc):
    word = list(map(str, input()))
    words.append(word)

# result = []
for i in range(tc):
    tmp_left = deque()
    tmp_right = deque()
    for j in range(len(words[i])):
        if words[i][j] == '<':
            if len(tmp_left) == 0:
                continue
            else:
                k = tmp_left.pop()
                tmp_right.appendleft(k)
        elif words[i][j] == '>':
            if len(tmp_right) == 0:
                continue
            else:
                h = tmp_right.popleft()
                tmp_left.append(h)
        elif words[i][j] == '-':
            if len(tmp_left) != 0:
                tmp_left.pop()
            else:
                continue
        else:
            tmp_left.append(words[i][j])

    # 조인을 잘 쓰자!! 바보야
    print("".join(tmp_left + tmp_right))


# 2
# <<BP<A>>Cd-
# ThIsIsS3Cr3t
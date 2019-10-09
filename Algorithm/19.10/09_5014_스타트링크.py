# baekjoon
# https://www.acmicpc.net/problem/5014

# 총 F층인 건물에서 G 층에서 출발해 S층 까지 가야한다
# 엘리베이터 버튼은 위로 U층, 아래로 D 층 밖에 누를 수 없을때
# 몇 번 눌러야 도착할 수 있는지 출력해라
# 갈 수 없다면 use the stairs 출력

import collections
f, s, g, u, d = map(int, input().split())
check = [False]*(f+1)
count = 0
state = False

q = collections.deque()
q.append(s)
check[s] = True

while q:
    for _ in range(len(q)):
        x = q.popleft()
        if x == g:
            state = True
            break
        else:
            for i in range(2):
                if i == 0:
                    next = x + u
                    if next <= f and check[next] == False:
                        check[next] = True
                        q.append(next)
                else:
                    next = x - d
                    if next >= 0 and check[next] == False:
                        check[next] = True
                        q.append(next)

    if state == True:
        break
    count += 1


if state == True:
    print(count)
else:
    print("use the stairs")

'''
10 1 10 2 1

100 2 1 1 0
'''
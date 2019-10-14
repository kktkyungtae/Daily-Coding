# BackJoon
# https://www.acmicpc.net/problem/17471

# 주어진 구역을 2개의 선거구로 나누어야하는데
# 한 선거구에 포함된 구역은 전부 연결되어 있어야한다

def bfs(li):
    q = collections.deque()
    q.append(li[0])
    visit = [False] * (n + 1)
    visit[li[0]] = True

    total = 0
    while q:
        x = q.popleft()
        total += ns[x]

        for j in li:
            if con_map[x][j] == 1 and visit[j] == False:
                q.append(j)
                visit[j] = True

    for i in li:
        if visit[i] == False:
            return 0
    return total

import collections, itertools

n = int(input())
ns = list(map(int, input().split()))
connect = [list(map(int, input().split())) for _ in range(n)]
con_map = [[0] * n for _ in range(n)]

n_li = list(range(n))

for i in range(n):
    for j in range(1, len(connect[i])):
        con_map[i][connect[i][j]-1] = 1

# for i in con_map:
#     print(i)

r = 1
ans = 999999
for i in range(n//2):
    temp_a = list(itertools.combinations(n_li, r))
    temp_b = list(itertools.combinations(n_li, n - r))
    r += 1

    for j in range(len(temp_a)):
        a = bfs(temp_a[j])
        b = bfs(temp_b[~j])

        if a * b != 0:
            if ans > abs(a-b):
                ans = abs(a - b)



if ans == 999999:
    print(-1)
else:
    print(ans)

'''
6
5 2 3 4 1 2
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2
'''
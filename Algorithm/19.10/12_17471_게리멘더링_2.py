import itertools, collections

def bfs(area):
    q = collections.deque()
    q.append(area[0])
    v = [False] * (n + 1)
    v[area[0]] = True

    total = 0
    while q:
        i = q.popleft()
        total += a[i]

        for j in area:
            if g[i][j] == 1 and v[j] == False:
                q.append(j)
                v[j] = True

    for i in area:
        if v[i] == False:
            return 0
    return total

n = int(input())
a = list(map(int, input().split()))
b = [list(map(int, input().split())) for _ in range(n)]

# 구역 나열
section = list(range(len(a)))

# 연결된 구역 나타내기
g = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(1, len(b[i])):
        g[i][b[i][j]-1] = 1


ans = 9 * 10000
r = 1
for i in range(n//2):
    c = list(itertools.combinations(section, r))
    d = list(itertools.combinations(section, len(section)-r))
    r += 1

    for j in range(len(c)):
        A = bfs(c[j])
        B = bfs(d[~j])

        if A * B != 0:
            if ans > abs(A-B):
                ans = abs(A-B)

if ans == 9 * 10000:
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

6
1 1 1 1 1 1
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2
'''
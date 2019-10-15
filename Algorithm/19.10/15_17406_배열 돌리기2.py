# Baekjoon
# https://www.acmicpc.net/problem/17406

# 배열이 주어진다
# 각 행의 합 중에서 가장 작은 값을 뽑는데,,
# 회전 연산에 따라 배열을 회전 시키고나서
# 각 행의 합 중에서 최소값을 출력한다

import itertools, collections

# n 가로 갯수 // m 세로 갯수
n, m, k = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]
func = [list(map(int, input().split())) for _ in range(k)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def trans(y, x, func, func_x):
    for kk in range(1, func + 1):
        idx = []
        t = collections.deque()
        ty, tx = y - kk, x - kk


        for k in range(4):
            for j in range(kk*2):
                ny, nx = ty + dy[k], tx + dx[k]
                idx.append((ny, nx))
                t.append(func_x[ny][nx])

        t.appendleft(t.pop())

        for i in range(len(t)):
            func_x[idx[i][0]][idx[i][1]] = t[i]

    return func_x


ans = 99999
for func_idx in itertools.permutations(range(k), k):
    tmp_mapp = [[x for x in mapp[k]] for k in range(n)]

    for j in range(k):
        tmp_mapp = trans(func[func_idx[j]][0] - 1 , func[func_idx[j]][1] - 1, func[func_idx[j]][2] , tmp_mapp)

    ans = min(ans, min([sum(tmp_mapp[i]) for i in range(n)]))

print(ans)


'''

5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1

'''
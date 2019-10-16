# Baekjoon
# https://www.acmicpc.net/problem/17406

# 배열이 주어진다
# 각 행의 합 중에서 가장 작은 값을 뽑는데,,
# 회전 연산에 따라 배열을 회전 시키고나서
# 각 행의 합 중에서 최소값을 출력한다

import itertools

def trans(r, c, s):
    pass

n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
func = [list(map(int, input().split())) for _ in range(k)]

ans = 99999

for i in range(len(func)):
    func[i][0] -= 1
    func[i][1] -= 1

per_func = list(itertools.permutations(func, k))

while per_func:
    tmp_ch = per_func.pop()
    new_A = [A[i][:] for i in range(n)]

    for rcs in tmp_ch:
        r, c, s = rcs
        trans(r, c, s)

    for i in new_A:
        ans = min(sum(i), ans)

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
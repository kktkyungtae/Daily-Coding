# Baekjoon
# https://www.acmicpc.net/problem/17406

# 배열이 주어진다
# 각 행의 합 중에서 가장 작은 값을 뽑는데,,
# 회전 연산에 따라 배열을 회전 시키고나서
# 각 행의 합 중에서 최소값을 출력한다

import itertools

def trans(r, c, s):
    gijun = [r - d, c - d]
    p = 2 * s

    for dj in range(1, 2 * d + 1):
        arr[gijun[0]][gijun[1]], arr[gijun[0]][gijun[1] + dj] = arr[gijun[0]][gijun[1] + dj], arr[gijun[0]][gijun[1]]

    for di in range(1, 2 * d + 1):
        arr[gijun[0]][gijun[1]], arr[gijun[0] + di][gijun[1] + p] = arr[gijun[0] + di][gijun[1] + p], arr[gijun[0]][gijun[1]]

    for dj in range(1, 2 * d + 1):
        arr[gijun[0]][gijun[1]], arr[gijun[0] + p][gijun[1] + p - dj] = arr[gijun[0] + p][gijun[1] + p - dj], arr[gijun[0]][gijun[1]]

    for di in range(1, 2 * d):
        arr[gijun[0]][gijun[1]], arr[gijun[0] + p - di][gijun[1]] = arr[gijun[0] + p - di][gijun[1]], arr[gijun[0]][gijun[1]]

n, m, k = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
func = [list(map(int, input().split())) for _ in range(k)]

ans = 99999

for i in range(len(func)):
    func[i][0] -= 1
    func[i][1] -= 1

for tmp_ch in itertools.permutations(func, k):
    arr = [Map[i][:] for i in range(n)]

    for r, c, s in tmp_ch:
        for d in range(s, 0, -1):
            trans(r, c, d)

    for i in arr:
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
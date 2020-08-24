# Baekjoon
# https://www.acmicpc.net/problem/17406

# 배열이 주어진다
# 각 행의 합 중에서 가장 작은 값을 뽑는데,,
# 회전 연산에 따라 배열을 회전 시키고나서
# 각 행의 합 중에서 최소값을 출력한다

import itertools

def turn(r, c, d):
   pos = [r-d, c-d]
   p = 2*d
   for dj in range(1, 2*d+1):
       arr[pos[0]][pos[1]], arr[pos[0]][pos[1]+dj] = arr[pos[0]][pos[1]+dj], arr[pos[0]][pos[1]]
   for di in range(1, 2*d+1):
       arr[pos[0]][pos[1]], arr[pos[0]+di][pos[1]+p] = arr[pos[0]+di][pos[1]+p], arr[pos[0]][pos[1]]
   for dj in range(1, 2*d+1):
       arr[pos[0]][pos[1]], arr[pos[0]+p][pos[1]+p-dj] = arr[pos[0]+p][pos[1]+p-dj], arr[pos[0]][pos[1]]
   for di in range(1, 2*d):
       arr[pos[0]][pos[1]], arr[pos[0]+p-di][pos[1]] = arr[pos[0]+p-di][pos[1]], arr[pos[0]][pos[1]]

N, M, K = map(int, input().split())

origin_arr = [list(map(int, input().split())) for _ in range(N)]
operation = [list(map(int, input().split()))for _ in range(K)]
ans = float('inf')

for turn_order in itertools.permutations(operation, K):
   arr = [[a for a in e] for e in origin_arr]

   for r, c, s in turn_order:
       r -= 1; c -= 1

       for d in range(s, 0, -1):
           turn(r, c, d)

   ans = min(min([sum(e) for e in arr]), ans)

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
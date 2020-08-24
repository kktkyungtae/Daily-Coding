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
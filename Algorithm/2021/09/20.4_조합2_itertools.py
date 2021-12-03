# itertools

from itertools import combinations
print(list(combinations([1,2,3,4], 3)))



# 백준 15649

n, m = map(int, input().split())

arr = [str(i) for i in range(1, n+1)]

for e in list(combinations(arr, m)):
    print(" ".join(e))
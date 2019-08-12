# Baekjoon

# 가방에 물건을 담을 건데,
# 가치가 가장 높게 담을 거다
# 대신, 무게도 고려해서 담아야한다

import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
dp = [-1 for _ in range(K+1)]
dp[0] = 0
for _ in range(N):
    w, v = map(int, input().split())
    for u in range(K-w, -1, -1):
        if dp[u] == -1:
            continue
        else:
            dp[u+w] = max(dp[u+w], dp[u]+v)
print(max(dp))
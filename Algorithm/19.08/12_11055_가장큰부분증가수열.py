# Baekjoon
# 수열에서 증가하는 수열 중에서 합이 가장 큰 것을 구해라

import sys
sys.stdin = open('input2.txt')

n = int(input())
a = list(map(int, input().split()))
dp = [-1]*n


for i in range(n):
    dp[i] = a[i]
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]+a[i]:
            dp[i] = dp[j] + a[i]

print(max(dp))
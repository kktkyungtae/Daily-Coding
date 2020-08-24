# Baekjoon

# 제곱수로 표현할 수 있는 항의 갯수 중에
# 최소항을 구해라

N = int(input())
dp = [0 for i in range(N+1)]
for i in range(1, N+1):
    dp[i] = i
    for j in range(1, i+1):
        if j*j > i:
            break
        else:
            dp[i] = min(dp[i], dp[i-j*j] + 1)
print(dp[N])

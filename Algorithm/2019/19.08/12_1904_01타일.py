# Baekjoon

# 길이가 N인 수열의 갯수를 구하라
# 단, 고를 수 있는 숫자는 00, 1

# n = int(input())
#
# dp = [0] * (n+1)
#
# dp[1] = 1
# dp[2] = 2
#
# for i in range(3, n+1) :
# 	dp[i] = (dp[i-2] + dp[i-1]) % 15746
#
# print(dp[n] % 15746)


a, b = 0, 1

for i in range(int(input())):
    a, b = b, (a+b) % 15746

print(b)

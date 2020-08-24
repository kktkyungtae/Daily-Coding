# 10
# 1 100 2 50 60 3 5 6 7 8

nums = int(input())
num_li = list(map(int,input().split()))
dp = [-1 for _ in range(nums)]

for i in range(nums):
    dp[i] = num_li[i]
    for j in range(i):
        if num_li[i] > num_li[j] and dp[i] < dp[j] + num_li[i]:
            dp[i] = dp[j] + num_li[i]
            # print(num_li)
            # print(dp)
            # print('-')

print(max(dp))
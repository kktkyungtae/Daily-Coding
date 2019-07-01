import sys
sys.stdin = open("종이붙이기.txt","r")

T = int(input())

for t in range(T):
    N = int(input())//10
    dp = []

    for x in range(N):
        dp.append(0)

    dp[0] = 1
    dp[1] = 3

    for i in range(2,len(dp)):
        dp[i] = dp[i-1] + dp[i-2]*2
    print(dp)
    print(f"#{t+1} {dp[N-1]}")
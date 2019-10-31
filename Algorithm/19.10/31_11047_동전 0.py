# Baekjoon
# https://www.acmicpc.net/problem/11047

# 주어진 동전들로 원하는 값을 만들어 내라

n, k = map(int, input().split())

dongjoen = [int(input()) for _ in range(n)]
real = []

for i in dongjoen:
    if i <= k:
        real.append(i)

cnt = 0
temp = 0
real.reverse()

for i in range(len(real)):
    if real[i] <= k:
        temp = k//real[i]
        k = k - temp*real[i]
        cnt += temp

    elif k == 0:
        break

print(cnt)

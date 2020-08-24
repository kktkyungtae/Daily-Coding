N, K = map(int,input().split())
money = []

for i in range(N):
    money.append(int(input()))

money.reverse()

result = 0
temp = 0
for i in range(len(money)):
    if money[i] <= K:
        temp = K//money[i]
        K = K - temp*money[i]
        result += temp
    elif K == 0:
        break

print(result)





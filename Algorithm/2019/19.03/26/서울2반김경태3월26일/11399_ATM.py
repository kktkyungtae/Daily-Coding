N = int(input())
wait = list(map(int, input().split()))

wait.sort()

temp, sums = 0,0

for w in wait:
    temp = temp + w
    sums += temp

print(sums)


# 피보나치 수열을 완성하시오.

n = 10

lists = [1,1]

for i in range(1, n-1):
    lists.append(lists[i-1] + lists[i])

print(lists)
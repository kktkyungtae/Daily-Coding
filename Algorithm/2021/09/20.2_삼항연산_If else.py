# 최적화 된 if문

n, p = map(int, input().split())

res1 = 0
res2 = 0

if n > p:
    res1 = n
else:
    res1 = p

print(res1)

res2 = n if n < p else p
print(res2)
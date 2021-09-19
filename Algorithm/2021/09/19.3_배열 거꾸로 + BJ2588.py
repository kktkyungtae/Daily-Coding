
arr = [0, 1, 2, 3, 4]
print(arr)

# 배열 거꾸로
arr.reverse()
print(arr)

n = int(input())
p = int(input())

n_p = [int(i) for i in str(p)]
n_p.reverse()

for i in n_p:
    print(n * i)
print(n*p)
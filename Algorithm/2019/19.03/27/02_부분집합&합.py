a=[1,3,4,2,4,5,2,23]
n = len(a)

for i in range(1<<n):
    nums = []
    for j in range(n):
        if i & (1<<j):
            nums.append(a[j])
        print(nums)


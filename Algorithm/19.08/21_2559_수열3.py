nums, lens = map(int, input().split())
on_li = list(map(int, input().split()))

max_sum = 0

if lens == 1:
    print(max(on_li))
else:
    for i in range(nums - lens +1):
        if max_sum < on_li[i] + on_li[i + lens-1]:
            max_sum = on_li[i] + on_li[i + lens-1]

print(max_sum)

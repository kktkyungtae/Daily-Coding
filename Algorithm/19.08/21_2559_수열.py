# Baekjoon
# 정해진 수열의 합 중 큰 수를 뽑아라

nums, lens = map(int, input().split())
on_li = list(map(int, input().split()))

i = 0
temp_sum = sum(on_li[0:lens])
max_sum = temp_sum

if lens == 1:
    print(max(on_li))
else:
    while True:
        temp_sum -= on_li[i]
        if i + lens >= nums:
            break
        temp_sum += on_li[i+lens]
        if max_sum < temp_sum:
            max_sum = temp_sum
        i+=1

    print(max_sum)

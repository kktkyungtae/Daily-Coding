# 7개의 자연수가 주어질 때, 홀수인 자연수를 모두 골라 합을 구하고
# 고른 홀수 중 최솟값을 찾아라

nums = []
for i in range(7):
    num_li = int(input())
    if num_li % 2 != 0:
        nums.append(num_li)
    else:
        pass

if len(nums) == 0:
    print('-1')
else:
    print(sum(nums))
    print(min(nums))
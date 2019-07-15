# 주어진 5개의 숫자의 평균과 중간값을 구하라

num_li = []
for i in range(5):
    nums = int(input())
    num_li.append(nums)

num_li.sort()
print(sum(num_li)//5)
print(num_li[2])
# Baekjoon
# 정해진 수열의 합 중 큰 수를 뽑아라



nums, lens = map(int, input().split())
on_li = list(map(int, input().split()))
d = [0]

for i in range(nums):
    d.append(d[i] + on_li[i])
print(on_li)
print(d)
r = 0

for i in range(lens, nums+1):
    r = max(r, d[i]-d[i-lens])
print(r)
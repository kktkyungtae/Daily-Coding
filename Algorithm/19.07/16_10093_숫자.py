# 두 양의 정수가 주어질 때
# 사이에 있는 모든 정수를 출력하라
# 갯수
# 두 숫자 사이의 수를 오름차 순으로

nums = list(map(int,input().split()))

if nums[0] < nums[1]:
    print(nums[1]-nums[0]-1)
    for i in range(nums[0]+1,nums[1],1):
        print(i,end=" ")
elif nums[0] > nums[1]:
    print(nums[0]-nums[1]-1)
    for i in range(nums[1]+1,nums[0],1):
        print(i,end=" ")
else:
    print('0')

# Baekjoon
# 조세퍼스 순열
# 주어진 N, K 는 N은 인원수, K는 번쨰 사람을 지우라는 뜻
# 지울때 K 번째 사람을 지우고 거기서 부터 새로 시작

from collections import deque

n, k = map(int,input().split())

nums = deque(i for i in range(1, n+1))
result = deque()
print(nums[0])

while len(nums) != 0:
    for j in range(k):
        nums.popleft()
        result.append(nums[0])

print(result)

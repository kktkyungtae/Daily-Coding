# Baekjoon
# 조세퍼스 순열
# 주어진 N, K 는 N은 인원수, K는 번쨰 사람을 지우라는 뜻
# 지울때 K 번째 사람을 지우고 거기서 부터 새로 시작

# n = 7, k = 3
# [1, 2, 3, 4, 5, 6, 7]     L: 7, I: 0
# [1, 2, 4, 5, 6, 7]        L: 6, I: 2  > 3
# [1, 2, 4, 5, 7]           L: 5, I: 4  > 6
# [1, 4, 5, 7]              L: 4, I: 1  > 2
# [1, 4, 5]                 L: 3, I: 3  > 7
# [1, 4]                    L: 2, I: 2  > 5
# [4]                       L: 1, I: 0  > 1
# []                        L: 0, I: 0  > 4 -> 조건 탈출

# (0 + 2) % 7 = 2
# (2 + 2) % 6 = 4
# (4 + 2) % 5 = 1
# (1 + 2) % 4 = 3
# (3 + 2) % 3 = 2
# (2 + 2) % 2 = 0
# (0 + 2) % 1 = 0
# (현재 인덱스 + (k-1)) % 현재 배열 길이 = 다음 인덱스


N, K = map(int,input().split())

nums = [i for i in range(1, N+1, 1)]

result = []
j = 0

for t in range(N):
    j = (j+K-1) % len(nums)
    result.append(nums[j])
    nums.remove(nums[j])
    print(j)

print('<%s>'%(', '.join(map(str, result))))



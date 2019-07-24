# Baekjoon
# 조세퍼스 순열
# 주어진 N, K 는 N은 인원수, K는 번쨰 사람을 지우라는 뜻
# 지울때 K 번째 사람을 지우고 거기서 부터 새로 시작

N, K = map(int,input().split())

nums = [i for i in range(1, N+1, 1)]

result = []

while len(nums) != 0:
    if K == 1:
        result += nums
        break
    else:
        for j in range(K-1):
            nums.append(nums.pop(0))
        result.append(nums.pop(0))

print('<%s>'%(', '.join(map(str, result))))



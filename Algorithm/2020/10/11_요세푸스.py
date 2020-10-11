# 요세푸스 순열
# n명이 원으로 앉아있을 때, k번째 사람을 제거하고
# n명이 모두 제거될 때 까지 진행

n, K = map(int, input().split())
q = [x for x in range(1, n+1)]

j = 0
result = []
for _ in range(n):
    j = (j + K-1) % len(q)
    result.append(q[j])
    q.remove(q[j])

# print('<%s>'%(', '.join(map(str, result))))
print("<"+", ".join(map(str, result))+">")
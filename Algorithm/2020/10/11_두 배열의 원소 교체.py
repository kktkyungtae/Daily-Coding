# 주어진 A,B 배열이 있다
# 두 배열의 수를 교체할 수 있는 횟수를 정해줄 때,
# A의 배열의 합이 가장 큰 것을 출력해라

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

#
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5
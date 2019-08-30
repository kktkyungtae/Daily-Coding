N = int(input())

li = [0] * 1001

max_idx = []
max_value = 0
garo = 0

for n in range(N):
    a, b = map(int, input().split())
    li[a] = b

    if garo < a:
        garo = a
    if max_value < b:
        max_value = b
        max_idx.clear()
        max_idx.append(a)
    elif max_value == b:
        max_idx.append(a)

max_idx.sort()

result = (max_idx[-1] - max_idx[0] + 1) * max_value

temp = 0

for i in range(max_idx[0]):
    if li[i] > temp:
        temp = li[i]
    result += temp

temp = 0

for i in range(garo, max_idx[-1], -1):
    if li[i] > temp:
        temp = li[i]
    result += temp

print(result)
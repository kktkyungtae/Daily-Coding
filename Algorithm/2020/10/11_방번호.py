# 구성해야 하는 방번호가 주어진다
# 0-9까지 있는 숫자 세트가 있다
# 방번호를 구성하기 위해 필요한 최소 세트 수는?

num = list(map(int, input()))

count = [0*i for i in range(10)]

for i in num:
    for j in range(10):
        if j == i:
            count[i] += 1
        else:
            continue

count[6], count[9] = (count[6] + count[9]) // 2 + (count[6] + count[9]) % 2, (count[6] + count[9]) // 2 + (count[6] + count[9]) % 2

print(max(count))

# 세 자연수가 주어질 때, 그 들의 곱인 수에서
# 0에서 9까지의 수가 몇번 쓰였는지 출력해라

num = []
for i in range(3):
    num.append(int(input()))

c = str(num[0] * num[1] * num[2])

print(c)

for i in range(0, 10):
    print(c.count(str(i)))
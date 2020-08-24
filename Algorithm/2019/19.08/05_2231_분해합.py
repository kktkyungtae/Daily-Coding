# Baekjoon

# 주어진 분해합의 생성자를 구하라
# 123의 분해합은 123 + 1 + 2 + 3 = 129 이고
# 129의 생성자는 123 이다.

nums = int(input())

for i in range(1, nums + 1):
    num_list = list(map(int, str(i)))
    result = i + sum(num_list)

    if result == nums:
        print(i)
        break
    if i == nums:
        print(0)

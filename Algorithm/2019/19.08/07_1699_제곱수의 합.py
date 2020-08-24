# Baekjoon

# DP
# 입력된 수의 제곱수들의 합의 최소갯수를 출력해라
# 7 = 2^2 + 1^2 + 1^2 +1^2 : 4

num = int(input())
cnt = 0
num_li = list(i for i in range(1, num))

print(num_li)
print(num_li[2]*num_li[2])

def minus(num):


while num != 0:
    half = num // 3
    if num_li[half]*num_li[half] > num:
        half -= 1
    elif num_li[half]*num_li[half] == num:
        print(1)
        break
    else:
        if num - num_li[half] > 4:
            num -= num_li[half]

        else:
            print(4)
            break
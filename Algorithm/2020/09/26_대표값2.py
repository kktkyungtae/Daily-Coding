# 다섯개의 숫자의 평균과 중간값을 출력해라

num_li = []

for i in range(5):
    a = int(input())
    num_li.append(a)

num_li.sort()

print(sum(num_li)//5)
print(num_li[2])
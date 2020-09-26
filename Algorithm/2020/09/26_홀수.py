# 7개의 수 중에 홀수의 합과 그 홀수 중에 최소값을 출력해라

num_li = []
for i in range(7):
    a = int(input())
    num_li.append(a)

hole_li = []
for j in num_li:
    if j % 2 != 0:
        hole_li.append(j)

hole_li.sort()

if len(hole_li) == 0:
    print(-1)
else:
    print(sum(hole_li))
    print(hole_li[0])
# https://www.acmicpc.net/problem/10804
# 20개의 숫자를
# 주어진 10개의 구간에서 역배치하여 출력하라

n_li = []
for i in range(1,21):
    n_li.append(i)

c_li = []
for j in range(10):
    c_li.append(list(map(int, input().split())))

for k in range(10):
    n_li[c_li[k][0]-1:c_li[k][1]] = reversed(n_li[c_li[k][0]-1:c_li[k][1]])

for l in n_li:
    print(l, end =' ')
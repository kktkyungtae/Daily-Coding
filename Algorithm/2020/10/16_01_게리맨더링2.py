from collections import deque
import itertools

n = int(input())
mapp = []
for _ in range(n):
    mapp.append(list(map(int, input().split())))

# 기준점 구하기
x, y, d1, d2 = 1, 1, 1, 1
dl = max(d1, d2)
x_li = []
y_li = []
for i in range(n - d1 - d2):
    x_li.append(i)
for i in range(1, n - d2):
    y_li.append(i)

# 기준점 list
gijoon = deque()
for i in x_li:
    for j in y_li:
        gijoon.append([i, j])

# d 조합 구하기
d_li = []

for i in range(1, n - 1):
    d_li.append(i)

di_com = list(itertools.permutations(d_li, 2))


while gijoon:
    xx, yy = gijoon.popleft()

    print(xx, yy)
    for i in di_com:
        d_1, d_2 = i[0], i[1]
        nanugi = [[-1] * n for _ in range(n)]
        if xx < 0 or xx + d_2 > n and yy < 0 and yy + d_2 > n:
            continue
        else:
            if xx + d_1 + d_2 < n and yy + d_1 + d_2 < n:
                nanugi[xx][yy] = 0

                for k in range(1, d_1 + 1):
                    nanugi[xx + k][yy - k] = 0

                for kk in range(1, d_2 + 1):
                    nanugi[xx + d_1 + kk][yy - d_1 + kk] = 0

                for kkk in range(1, d_1 + 1):
                    nanugi[xx + d_1 + d_2 - kkk][yy - d_1 + d_2 + kkk] = 0

                for kkkk in range(1, d_2 + 1):
                    nanugi[xx + d_2 - kkkk][yy + d_2 - kkkk] = 0

        print(i)
        for i in nanugi:
            print(i)
        print()

# BackJoon
# https://www.acmicpc.net/problem/17471

# 주어진 구역을 2개의 선거구로 나누어야하는데
# 한 선거구에 포함된 구역은 전부 연결되어 있어야한다

import itertools

area = int(input())
people = list(map(int, input().split()))

connect = []
for i in range(area):
    temp = list(map(int, input().split()))
    temp.pop(0)
    connect.append(temp)

areas = [ _ for _ in range(area)]

combi_area = list(itertools.combinations(areas, 2))

for k in combi_area:
    print(k)

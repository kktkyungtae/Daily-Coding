# BackJoon
# https://www.acmicpc.net/problem/17471

# 주어진 구역을 2개의 선거구로 나누어야하는데
# 한 선거구에 포함된 구역은 전부 연결되어 있어야한다
#
import itertools

n = 6
section = [1,2,3,4,5,6]

r = 1

c = list(itertools.combinations(section, r))
d = list(itertools.combinations(section, len(section)-r))

print(len(c))
for i in c:
    print(i)
print()

print(len(d))
for i in d:
    print(i)
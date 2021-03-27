# https://www.acmicpc.net/problem/20057
# 삼성 기출..
# 2020하반기 모래 뭐시기

n = int(input())
mapp = []
for i in range(n):
    mapp.append(list(map(int, input().split())))

flag = [[-1 for _ in range(n+4)] for _ in range(n+4)]
zero_map = [[0 for _ in range(n+4)] for _ in range(n+4)]

for i in range(2, n+2):
    flag[i][2:n+2] = mapp[i-2][:]
    zero_map[i][2:n+2] = mapp[i-2][:]

for i in mapp:
    print(i)
print()

for i in flag:
    print(i)
print()

# 5
# 7 7 7 7 7
# 7 7 7 7 7
# 7 7 7 7 7
# 7 7 7 7 7
# 7 7 7 7 7


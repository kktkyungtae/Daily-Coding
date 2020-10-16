N = int(input())
map_list = [list(map(int, list(input()))) for _ in range(N)]
t_N = N // 2
change = -1
answer = 0
for i in range(N//2):
    for j in range(i - N // 2, N - t_N):
        map_list[i][j] = 0

for i in map_list:
    print(i)

#
# 5
# 14054
# 44250
# 02032
# 51204
# 52212
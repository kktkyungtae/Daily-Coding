# a=[[1,2],[3,4],[5,6],[7,8]]
#
# print(a)
#
# for i in zip(*a):
#     print(i)
#



n = int(input())
grid = [list(input()) for i in range(n)]
ans = 0

print(grid)

for i in zip(*grid):
    print(i)
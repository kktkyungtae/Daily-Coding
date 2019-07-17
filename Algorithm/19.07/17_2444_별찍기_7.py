# Backjoon
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

star = int(input())
blank = star

for i in range(1,star+1):
    print(' '*(blank-i),end='')
    print('*'*(2*i-1))

for j in range(1,star):
    print(' '*j,end='')
    print('*'*(2*(blank-j)-1))

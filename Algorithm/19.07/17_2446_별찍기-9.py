# Backjoon
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********

star = int(input())
blank = star

for i in range(star):
    print(' '*i, end='')
    print('*'*(2*(star-i)-1))

for j in range(2,star+1):
    print(' '*(star-j), end='')
    print('*'*(2*j-1))
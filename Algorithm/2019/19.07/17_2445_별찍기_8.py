# Backjoon
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

star = int(input())
blank = star

for i in range(1,star+1):
    print('*'*i, end = '')
    print(' '*(2*(star)-2*i), end = '')
    print('*' * i)
for j in range(1,star):
    print('*'*(star-j), end ='')
    print(' ' * (2 * j), end='')
    print('*' * (star - j))
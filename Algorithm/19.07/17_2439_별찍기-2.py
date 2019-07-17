# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 앞에 빈공간이 있다
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#     *
#    **
#   ***
#  ****
# *****

star = int(input())

for k in range(1,star+1):
    print(' '*(star-k), end='')
    print('*'*k)
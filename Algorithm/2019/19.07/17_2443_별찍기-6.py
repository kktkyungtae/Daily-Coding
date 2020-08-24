# Baekjoon
# 첫째 줄에는 별 2×N-1개, 둘째 줄에는 별 2×N-3개, ..., N번째 줄에는 별 1개를 찍는 문제
# 별은 가운데를 기준으로 대칭이어야 한다.
# *********
#  *******
#   *****
#    ***
#     *

star = int(input())
blank = star

for i in range(star):
    print(' '*i, end ='')
    print('*'*(2*(blank-i)-1))

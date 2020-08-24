# Baekjoon
# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, N번째 줄에는 별 1개를 찍는 문제
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# *****
# ****
# ***
# **
# *

star = int(input())

for i in range(star,0,-1):
    print('*'*i)
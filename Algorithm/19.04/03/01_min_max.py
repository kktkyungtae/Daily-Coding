# 큰 값과 작은 값의 차이를 구하라

import sys
sys.stdin = open('01_input.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())

    num_list = list(map(int,input().split()))

    print("#{} {}".format(tc +1, max(num_list) - min(num_list)))
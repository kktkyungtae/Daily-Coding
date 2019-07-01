from itertools import combinations

import sys
sys.stdin = open('input/01_input.txt','r')

t = int(input())
for tc in range(t):
    n = int(input())

    stone_li = list(map(int,input().split()))

    des_li = []
    mins = 0
    for i in range(len(stone_li)):
        des_li.append(abs(0 - stone_li[i]))

    mins = min(des_li)

    print("#{} {} {}".format(tc+1, mins, des_li.count(mins)))




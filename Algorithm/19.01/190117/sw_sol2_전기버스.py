# [2019.01.17_문제2_Electric Bus]
# k = 충전 후 이동할 수 있는 정류장 수
# N = 종점 까지의 정류장 수
# M = 충전기가 있는 정류장 수

import sys
sys.stdin = open('전기버스_input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    knm = list(map(int,input().split()))
    k,n,m = knm[0],knm[1],knm[2]
    charge = list(map(int,input().split()))
    charge.append(charge[-1]+k)
    cnt, standard, i = 0,0,0

    while standard + k < n:
        if standard+k < charge[i]:
                cnt = 0
                break
        elif standard+k == charge[i]:
            standard = charge[i]
            cnt += 1
        else:
            if standard + k < charge[i+1]:
                standard = charge[i]
                cnt += 1
        i += 1
    
    print(f'#{test_case} {cnt}')
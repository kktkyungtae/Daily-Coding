# 주어진 행렬에서
# 각 행과 대각선에 있는 숫자들의 합중에 최대값을 출력하라.

import sys
sys.stdin=open('09_input.txt','r')

for tc in range(10):
    t = int(input())

    matt = []
    for i in range(100):
        temp_matt = list(map(int,input().split()))
        matt.append(temp_matt)

    result = []
    temp1_result = []

    # 가로
    temp = 0
    for g in range(100):
        for s in range(100):
            temp += matt[g][s]
        temp1_result.append(temp)
        temp = 0
    result.append(max(temp1_result))

    # 세로
    temp = 0
    temp2_result = []
    for g in range(100):
        for s in range(100):
            temp += matt[s][g]
        temp2_result.append(temp)
        temp = 0
    result.append(max(temp2_result))

    # 오른쪽 대각선
    temp = 0
    temp3_result = []
    for g in range(100):
        temp += matt[g][g]
    temp3_result.append(temp)
    result.append(max(temp3_result))

    # 왼쪽 대각선
    temp=0
    temp4_result = []
    for g in range(100):
        temp += matt[g][99-g]
    temp4_result.append(temp)
    result.append(max(temp4_result))

    print("#{} {}".format(tc+1,max(result)))

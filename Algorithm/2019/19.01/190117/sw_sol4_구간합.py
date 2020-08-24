# [2019.01.17_문제4_구간합]
# N개의 숫자 중에 이웃한 3가지의 숫자의 합이 가장 큰 수와 가장 작은 수의 차를 구하라

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
# 다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

###### 구간 M개의 합들의 list를 만들고 거기서 min max 골라서 차를 구한다  ######
###### 숫자의 크기 순으로 나열한 뒤에 앞에 세개 뒤에 세개 ######

import sys
sys.stdin = open('구간합_input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    
    p = list(map(int,input().split()))
    num = list(map(int,input().split()))
    n,m = p[0],p[1]
    min_result = sum(num[:m])
    max_result = sum(num[:m])

    for i in range(1,n-m+1):
        if min_result > sum(num[i:m+i]):
            min_result = sum(num[i:m+i])
        if max_result < sum(num[i:m+i]):
            max_result = sum(num[i:m+i])

    print(f'#{test_case} {max_result - min_result}')

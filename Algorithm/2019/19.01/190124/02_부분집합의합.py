# def my_sum(a):
#     sum1 = 0
#     for i in range(len(a)):
#         sum1 += i
#     return sum1

import sys
sys.stdin = open("부분집합의합", "r")


T = int(input())
for t in range(1,T+1):
    N, K = map(int,input().split())
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    n = len(A)
    cnt = 0
    for i in range(1<<n):  # 부분 집합 수
        result = []        # 부분 집합들을 담을 배열
        for j in range(n): # 원소의 수
            if i & (1<<j): # i의 j번째 비트가 1이면, j번째 원소를 result에 append
                result.append(A[j])
        if(len(result)==N and sum(result)==K):
            cnt += 1
    print(f'#{t} {cnt}')


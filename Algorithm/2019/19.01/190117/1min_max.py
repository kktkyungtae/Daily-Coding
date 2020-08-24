"""
>문제 : SW Expert Academy LIST1 연습문제
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

>입력
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

>출력
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
"""
import sys
sys.stdin = open("input.txt", "r")

# def my_min(n):
#     result = n[0]
#     for i in n:
#         if i < result:
#             result = i
#     return result
#
# def my_max(n):
#     result = n[0]
#     for i in n:
#         if i > result:
#             result = i
#     return result

# 2
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    print("#{} {}".format(tc, max(nums)-min(nums)))

# 3
# def my_sub(n):
#     min1 = n[0]
#     max1 = n[0]
#     for i in n:
#         if i < min1 : min1 = i
#         if i > max1 : max1 = i
#     return max1-min1

# T = int(input())
# for tc in range(1,T+1):
#     n = int(input())
#     nums = list(map(int, input().split()))
#     a = my_sub(nums)
#     print(f'#{tc} {a}')
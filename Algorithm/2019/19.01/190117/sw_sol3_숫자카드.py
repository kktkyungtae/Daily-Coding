# [2019.01.17_문제3_num-card]
# 0-9 까지 적힌 N장의 카드 중에서
# 가장 많은 수가 적인 카드의 장수와 번호를 출력하시오.
# [조건] : 장수가 같을 경우 더 큰 숫자를 출력한다.

import sys
sys.sdtin = open('3_num-card_input.text','r')

T = int(input())
for test_case in range(1,T+1):
    a = input()
    n = list(map(int, input()))
    cnt = 0
    num = 0
    for i in range(10):
        if n.count(i) >= cnt:
            cnt = n.count(i)
            num = i

    print(f"#{test_case} {num} {cnt}")
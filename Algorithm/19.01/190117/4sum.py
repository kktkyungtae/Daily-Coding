"""
>문제 : SW Expert Academy LIST1 연습문제
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.

이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6
이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12
답은 12와 6의 차인 6을 출력한다.

>입력
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )

다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

>출력
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
"""
import sys
sys.stdin = open("input4.txt", "r")

T = int(input())
for tc in range(1,T+1):
    a, b = list(map(int,input().split()))
    c = list(map(int, input().split()))
    max1=0
    min1=sum(c)
    for i in range(a-(b-1)):
        t = 0
        for j in range(b):
            t += c[i+j]
        if(t>max1):
            max1=t
        if(t<min1):
            min1=t
    print(f'#{tc} {max1 - min1}')


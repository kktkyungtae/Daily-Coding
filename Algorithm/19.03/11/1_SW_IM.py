# 스위치 켜고 끄기
# 배열의 배수의 숫자를 바꾸는데, 주어진 배열을 만들 수 있는 최소 횟수를 구하여라
import sys
sys.stdin = open('1_SW_input.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())
    button = list(map(int,input().split()))
    button.insert(0,0)
    zero = [0 for i in range(len(button))]

    diff = []
    cnt = 0
    for i in range(len(button)):

        if button[i] == zero[i]:
            pass
        else:
            if zero[i] == 1:
                zero[i] = 0
                cnt +=1
            else:
                zero[i] = 1
                cnt +=1
    print(cnt)




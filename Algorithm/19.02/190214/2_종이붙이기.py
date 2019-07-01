import sys
sys.stdin = open("종이붙이기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(int(input())/10)

    num = [0,1,3]

    for i in range(3,N+1):
        if i%2:
            num.append(num[i-2] * 4 + 1)
        else:
            num.append(num[i-2] * 4 - 1)
    
    print(f'#{test_case} {num[N]}')
    



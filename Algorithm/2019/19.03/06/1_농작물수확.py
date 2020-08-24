import sys
sys.stdin = open('1_input.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())
    total_li = []
    sums = []
    result = []
    for i in range(N):
        input_first = input()
        li = [str(x) for x in input_first]
        total_li.append(li)

    for j in range(0,N//2+1):
        sums.append(total_li[N//2 + j][j:N-j])
    for j in range(1,N//2+1):
        sums.append(total_li[N//2 -j][j:-j])

    print('#{} {}'.format(tc+1,sums))
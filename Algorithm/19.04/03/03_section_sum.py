import sys
sys.stdin = open('03_input.txt','r')

T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    num_list = list(map(int,input().split()))

    sum_li= []
    for i in range(0,N-M+1):
        sum_num = sum(num_list[i:i+M])
        sum_li.append(sum_num)

    max_num = max(sum_li)
    min_num = min(sum_li)

    gap = max_num - min_num

    print("#{} {}".format(tc+1, gap))
import sys
sys.stdin = open('1_input.txt','r')

T = int(input())
for tc in range(T):
    N = int(input())
    shift = list(map(int,input().split()))
    start = shift[0:2]
    finish = shift[2:]
    gap = []
    gap.append(finish[0]-start[0])
    gap.append(finish[1]-start[1])

    dx = [3,2,3,2,-3,-2,-3,-2]
    dy = [2,3,-2,-3,2,3,-2,-3]

    n = len(dx)
    len_list = []
    for i in range(0, (1 << n)):
        x_list = []
        y_list = []

        for j in range(0, n):
            if i & (1 << j):
                x_list.append(dx[j])
                y_list.append(dy[j])
        if sum(x_list) == gap[0]  and sum(y_list) == gap[1]:
            len_list.append(len(x_list))
    print("#{} {}".format(tc+1,min(len_list)))
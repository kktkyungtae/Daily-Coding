import sys
sys.stdin = open('09_input.txt','r')

# 중점인 상이 주어지고
# 상은 상하좌우로 한칸 및 대각선 2칸 이동할 수 있다.
# 상이 최소 이동해서 목적지까지 가는 횟수를 구하여라
# [입력]
# 01. test case
# 02. N : 게임판의 크기
# 03. 상의 위치와 목적지의 좌표


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
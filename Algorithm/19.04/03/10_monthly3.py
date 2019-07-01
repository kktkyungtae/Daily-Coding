import sys
sys.stdin = open('3_input.txt','r')

# 로봇과 과자의 갯수와
# 과자들의 위치
# 로봇의 위치가 주어진다.
# 각 로봇들이 최소의 거리로 각 과자의 좌표에 도달할 때,
# 그 최소 거리를 구하시오.


T = int(input())
for tc in range(T):
    N = int(input()) # 갯수
    sn = list(map(int,input().split()))
    ro = list(map(int,input().split()))

    snacks = []
    robots = []
    for i in range(0,2*N,2):
        snacks.append(sn[i:i+2])

    for i in range(0,2*N,2):
        robots.append(ro[i:i+2])

    gap = []
    for i in range(N):
        for j in range(N):
            a=abs(snacks[i][0] - robots[j][0]) + abs(snacks[i][1] - robots[j][1])
            gap.append(a)

    gap_div = []
    for i in range(0, len(gap), N):
        gap_div.append(gap[i:i + N])

# [[2, 2, 3], [3, 5, 6], [5, 3, 4]]
# [[8, 11, 4, 13], [10, 13, 4, 7], [14, 17, 8, 5], [5, 8, 7, 10]]
# [[2, 6, 10, 14], [2, 2, 6, 10], [6, 2, 2, 6], [10, 6, 2, 2]]

    for i in range(len(gap_div)):

import sys
sys.stdin=open('10_input.txt','r')

t = int(input())
for tc in range(t):
    n = int(input())

    section = [[0]*10 for _ in range(10)]

    xy_lists = []
    for i in range(n):
        xy_li = list(map(int,input().split()))
        xy_lists.append(xy_li)

    for k in range(n):
        for g in range(xy_lists[k][1], xy_lists[k][3]+1):
            for s in range(xy_lists[k][0], xy_lists[k][2]+1):
                section[g][s] += xy_lists[k][4]


    cnt = 0
    for i in range(10):
        for j in range(10):
            if section[i][j] == 3:
                cnt+=1
    print("#{} {}".format(tc+1,cnt))
import sys
sys.stdin=open('input/09.txt','r')

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())

    mtx = []
    for i in range(n):
        mtx.append(list(map(int, input().split())))

    sum_li = []
    for i in range(n-m+1):
        for j in range(n-m+1):
            temp_sum = 0
            for x in range(m):
                for y in range(m):
                    temp_sum += mtx[i+x][j+y]
            sum_li.append(temp_sum)


    print("#{} {}".format(tc+1, max(sum_li)))








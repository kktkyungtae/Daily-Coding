import sys
sys.stdin=open('input/08.txt','r')

t = int(input())

for tc in range(t):
    n, k = map(int,input().split())

    matrix = []
    for i in range(n):
        matrix.append(list(map(int,input().split())))

    # 가로 탐색
    result = 0
    for i in range(n):
        cnt = 0
        blank_li = []
        for j in range(n):
            if matrix[i][j] == 1:
                cnt += 1
            else:
                blank_li.append(cnt)
                cnt = 0
        blank_li.append(cnt)
        for c in blank_li:
            if k == c:
                result += 1

    for j in range(n):
        cnt = 0
        blank_li = []
        for i in range(n):
            if matrix[i][j] == 1:
                cnt += 1
            else:
                blank_li.append(cnt)
                cnt = 0
        blank_li.append(cnt)
        for r in blank_li:
            if k == r:
                result += 1

    print("#{} {}".format(tc+1, result))


#1 1
#2 2
#3 2
#4 0
#5 9
#6 1
#7 37
#8 0
#9 84
#10 8
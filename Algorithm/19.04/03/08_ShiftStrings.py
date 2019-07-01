import sys
sys.stdin=open('08_input.txt','r')

t = int(input())

for tc in range(t):
    a, b = map(int,input().split())
    a_li = list(map(int,input().split()))
    b_li = list(map(int,input().split()))

    temp = 0
    if a - b < 0:
        c = abs(a - b)
        c_li = []
        for s in range(c+1):
            for i in range(a):
                temp += a_li[i] * b_li[i+s]
            c_li.append(temp)
            temp = 0
        print("#{} {}".format(tc+1,max(c_li)))
    elif a - b > 0:
        c = abs(a - b)
        c_li = []
        temp = 0
        for s in range(c+1):
            for i in range(b):
                temp += b_li[i] * a_li[i+s]
            c_li.append(temp)
            temp = 0
        print("#{} {}".format(tc + 1, max(c_li)))
    else:
        c_li = []
        temp = 0
        for i in range(len(a_li)):
            temp += b_li[i] * a_li[i+s]
            c_li.append(temp)
            temp = 0
        print("#{} {}".format(tc + 1, max(c_li)))

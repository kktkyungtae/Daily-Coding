import sys
sys.stdin=open('11_input.txt','r')

t = int(input())
for tc in range(t):
    n = int(input())

    num_li = list(map(int,input().split()))
    num_li.sort()

    result = []
    for i in range(n):
        num_li.reverse()
        result.append(num_li.pop(0))

    result = result[:10]
    print("#{}".format(tc+1), end=' ')
    for j in result:
        print(j, end=' ')
    print()
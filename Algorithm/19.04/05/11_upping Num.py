import sys
sys.stdin=open('input/11.txt','r')

t = int(input())
for tc in range(t):
    n = int(input())

    num_li = list(map(int, input().split()))

    temp_li = []
    for i in range(n-1):
        temp_li.append(str(num_li[i]*num_li[i+1]))


    result = []
    for j in range(len(temp_li)):
        str_li = list(temp_li)
        if len(str_li[j]) == 1:
            pass
        elif len(str_li[j]) > 1:
            de_li = list(str_li[j])
            for k in range(len(de_li)-1):
                if de_li[k] <= de_li[k+1]:
                    result.append(temp_li[j])
                else:
                    break

    ans = []
    for i in result:
        ans.append(int(i))

    print("#{} {}".format(tc+1,max(ans)))





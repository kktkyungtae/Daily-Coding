import sys
sys.stdin = open('06_input.txt','r')

for tc in range(10):
    N = int(input())

    view = list(map(int,input().split()))

    result = 0
    for i in range(2, N-2):
        left_view = max(view[i-1],view[i-2])
        right_view = max(view[i+1],view[i+2])
        total_view = max(left_view,right_view)
        if view[i] - total_view > 0:
            result += view[i] - total_view
        else:
            pass

    print("#{} {}".format(tc+1,result))
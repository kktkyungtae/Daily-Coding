import sys
sys.stdin=open('input/10.txt','r')

t = int(input())
for tc in range(t):
    n = int(input())

    farm = []
    for i in range(n):
        msg = input()
        farm.append([int(x) for x in msg])

    # 중간 값
    mid = n // 2

    if n == 1:
        print("#{} {}".format(tc+1, farm[0]))

    elif n > 1:
        result = 0
        shift = 0
        for x in range(0, mid + 1):
            if shift == 0:
                result += farm[0][mid]
                shift += 1
            else:
                result += sum(farm[x][mid-shift:mid+shift])
                shift += 1

        shift = 0
        for y in range(n-1, mid, -1):
            if shift == 0:
                result += farm[y][mid]
                shift += 1
            else:
                result += sum(farm[y][mid - shift:mid + shift])
                shift += 1

        print("#{} {}".format(tc+1,result))
# # 1
# # 5
# # 14054
# # 44250
# # 02032
# # 51204
# # 52212
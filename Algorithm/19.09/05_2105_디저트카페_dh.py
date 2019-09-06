import sys

sys.stdin = open("sample.txt", "r")

TC = int(input())
num_list=[0]*20

dx = [1,1,-1,-1]
dy = [1,-1,-1,1]

def is_range(a,b):
    if a<0 or a>=n:
        return False
    if b<0 or b>=n:
        return False
    return True

def find_desert(x,y):
    global max_num
    possible = [n-x,y]
    for a in range(1,n-x+1):
        for b in range(1,y+1):
            check_list=[False]*101
            flag = 0
            temp_x = x
            temp_y = y
            # check_list[num_list[x][y]] = True
            # temp_x = temp_x + dx[flag]
            # temp_y = temp_y + dy[flag]
            # print("여기는 {} {}".format(a,b))
            for c in range(a):
                if is_range(temp_x, temp_y):
                    if check_list[num_list[temp_x][temp_y]]==False:
                        # print(temp_x,temp_y)
                        check_list[num_list[temp_x][temp_y]]=True
                        temp_x = temp_x + dx[flag]
                        temp_y = temp_y + dy[flag]
                    else:
                        flag = 5
                        break
                else:
                    flag = 5
                    break
            if flag == 5:
                continue
            flag += 1
            for c in range(b):
                if is_range(temp_x, temp_y):
                    if check_list[num_list[temp_x][temp_y]] == False:
                        # print(temp_x, temp_y)
                        check_list[num_list[temp_x][temp_y]] = True
                        temp_x = temp_x + dx[flag]
                        temp_y = temp_y + dy[flag]
                    else:
                        flag = 5
                        break
                else:
                    flag = 5
                    break
            if flag == 5:
                continue
            flag += 1
            for c in range(a):
                if is_range(temp_x, temp_y):
                    if check_list[num_list[temp_x][temp_y]] == False:
                        # print(temp_x, temp_y)
                        check_list[num_list[temp_x][temp_y]] = True
                        temp_x = temp_x + dx[flag]
                        temp_y = temp_y + dy[flag]
                    else:
                        flag = 5
                        break
                else:
                    flag = 5
                    break
            if flag == 5:
                continue
            flag += 1
            for c in range(b):
                if is_range(temp_x, temp_y):
                    if check_list[num_list[temp_x][temp_y]] == False:
                        # print(temp_x, temp_y)
                        check_list[num_list[temp_x][temp_y]] = True
                        temp_x = temp_x + dx[flag]
                        temp_y = temp_y + dy[flag]
                    else:
                        flag = 5
                        break
                else:
                    flag = 5
                    break
            if flag == 5:
                continue

            # print("도착? : {} {}".format(temp_x,temp_y))

            max_num = max(max_num, sum(check_list))

for tc in range(1,TC+1):
    result = 0
    n = int(input())

    check_list = [0]*100

    for a in range(n):
        num_list[a] = list(map(int,input().split()))

    max_num = 0

    for a in range(n-2):
        for b in range(1,n-1):
            # print(a,b)
            # print("체크")
            find_desert(a,b)

    # print(num_list)
    if max_num == 0:
        max_num = -1

    print("#{} {}".format(tc,max_num))
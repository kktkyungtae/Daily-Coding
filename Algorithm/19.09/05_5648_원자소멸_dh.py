T = int(input())
def is_not_range(a,b):
    if a<0 or a>=4001:
        return True
    if b<0 or b>=4001:
        return True
    return False

check_list = [[0]*4001 for a in range(4001)]
# print(check_list)
for tc in range(1, T + 1):
    result = 0

    n = int(input())
    num_list=[0]*n
    #상하좌우 0 1 2 3
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for a in range(n):
        # [x,y ,이동방향, 보유에너지]
        temp = list(map(int,input().split()))
        num_list[a] = [2*temp[0]+2000,2*temp[1]+2000,temp[2],temp[3]]

    time = 4002

    # print(num_list)
    while time:
        time -=1
        candi = []
        for a in range(n):
            if num_list[a][2] == 4 or num_list[a][2] == 5:
                continue
            num_list[a][0] += dx[num_list[a][2]]
            num_list[a][1] += dy[num_list[a][2]]
            # print(num_list[a])
            if is_not_range(num_list[a][0],num_list[a][1]):
                num_list[a][2]=5
                continue
            if check_list[num_list[a][0]][num_list[a][1]] == time:
                if [num_list[a][0],num_list[a][1]] in candi:
                    # print("여기찍힘?")
                    continue
                else :
                    candi.append([num_list[a][0],num_list[a][1]])
                # print(num_list[a])
                # print(candi)
            else :
                check_list[num_list[a][0]][num_list[a][1]] = time

        for a in range(n):
            if num_list[a][2]!=5:
                check_list[num_list[a][0]][num_list[a][1]] = 0

        # print(candi)
        # if not candi:
        #     print(candi)
        for a in range(len(candi)):
            for b in range(n):
                if candi[a][0] == num_list[b][0] and candi[a][1] == num_list[b][1]:
                    result += num_list[b][3]
                    num_list[b][2] = 4
                    # print(num_list[b])

    print("#{} {}".format(tc,result))